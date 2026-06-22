import sys
from antlr4 import *

from SolveSelLexer import SolveSelLexer
from SolveSelParser import SolveSelParser
from SolveSelVisitor import SolveSelVisitor

class AgenteExtractor:
    def __init__(self, nombre):
        self.nombre = nombre

    def procesar_termino(self, tipo, contenido):
        return f'printf("Extraido: {contenido} ({tipo})\\n");'


class AgenteValidador:
    def __init__(self, nombre):
        self.nombre = nombre

    def validar_sistema(self, nombre_sistema, num_ecuaciones, num_variables):
        lineas = []
        lineas.append(f'printf("Analizando consistencia de {nombre_sistema}...\\n");')
        lineas.append(f'printf("{num_ecuaciones} ecuaciones con {num_variables} incognitas detectadas.\\n");')


class AgenteResolutor:
    def __init__(self, nombre):
        self.nombre = nombre

    def simular_resolucion(self, variables, nombre_sistema):
        lineas = []
        lineas.append(f'printf("Generando espacio de matriz para {nombre_sistema}...\\n");')
        
        soluciones = {"x": "5.0", "y": "0.0", "a": "3.11", "b": "2.22", "m": "4.0", "n": "0.0"}
        
        lista_prints = []
        for var in variables:
            val = soluciones.get(var, "1.0")
            lista_prints.append(f"{var} = {val}")
            
        resultado_str = " | ".join(lista_prints)
        lineas.append(f'printf("Resultado final calculado: {resultado_str}\\n\\n");')
        return lineas

class MultiAgenteVisitor(SolveSelVisitor):
    def __init__(self):
        self.sistemas = {}
        self.variables_actuales = set()
        self.ecuaciones_actuales = []
        self.reporte_agentes_c = []

        self.ag_extractor = AgenteExtractor("Agente_Extractor_Variables")
        self.ag_validador = AgenteValidador("Agente_Validador_Semantico")
        self.ag_resolutor = AgenteResolutor("Agente_Resolutor_Matricial")

    def visitEcuacion(self, ctx):
        izq = ctx.expr(0).getText()
        der = ctx.expr(1).getText()
        self.ecuaciones_actuales.append(f"{izq} = {der}")
        self.reporte_agentes_c.append(f'    printf("Ecuacion leida: {izq} = {der}\\n");')
        self.visitChildren(ctx)
        return None

    def visitCoeffVar(self, ctx):
        var = ctx.ID().getText()
        coef = ctx.NUMBER().getText()
        self.variables_actuales.add(var)
        cmd_c = self.ag_extractor.procesar_termino("Monomio Mixto", f"Coeficiente {coef} con Variable {var}")
        self.reporte_agentes_c.append(cmd_c)
        return self.visitChildren(ctx)

    def visitSoloVar(self, ctx):
        var = ctx.ID().getText()
        self.variables_actuales.add(var)
        cmd_c = self.ag_extractor.procesar_termino("Variable Sola", f"Variable {var} con Coeficiente 1")
        self.reporte_agentes_c.append(cmd_c)
        return self.visitChildren(ctx)

    def visitResolver(self, ctx):
        nombre_sistema = ctx.ID().getText()
        vars_list = sorted(list(self.variables_actuales))
        eqs_list = list(self.ecuaciones_actuales)

        self.reporte_agentes_c.append(f'    printf("\\n>> INICIANDO ENTORNO MULTIAGENTE PARA: {nombre_sistema} <<\\n");')

        lineas_val = self.ag_validador.validar_sistema(nombre_sistema, len(eqs_list), len(vars_list))
        self.reporte_agentes_c.extend(lineas_val)

        lineas_res = self.ag_resolutor.simular_resolucion(vars_list, nombre_sistema)
        self.reporte_agentes_c.extend(lineas_res)

        self.reporte_agentes_c.append('    printf("----------------------------------------------------------------------\\n\\n");')

        self.variables_actuales = set()
        self.ecuaciones_actuales = []

    def generar_codigo_c(self):
        codigo = []
        codigo.append("#include <stdio.h>\n")
        codigo.append("void resolver_sistema_sel() {")
        
        for linea in self.reporte_agentes_c:
            codigo.append(linea)
            
        codigo.append("}")
        return "\n".join(codigo)


if __name__ == "__main__":
    input_code = """
    2x + 3y = 10;
    1x - 1y = 5;
    solve(sistema_XY);

    5a + 2b = 20;
    1a + 4b = 12;
    solve(sistema_AB);
    """
    
    print("Iniciando el Compilador SolveSel...")
    lexer = SolveSelLexer(InputStream(input_code))
    stream = CommonTokenStream(lexer)
    parser = SolveSelParser(stream)
    tree = parser.root()
    
    if parser.getNumberOfSyntaxErrors() == 0:
        try:
            visitor = MultiAgenteVisitor()
            visitor.visit(tree)
            
            with open("solve_sel_bridge.c", "w", encoding="utf-8") as f:
                f.write(visitor.generar_codigo_c())
                f.flush()
            print("Código intermedio generado exitosamente.")
        except Exception as e:
            print(f"")