; ModuleID = 'solve_sel_sin_optimizaciones.ll'
source_filename = "solve_sel_bridge.c"
target datalayout = "e-m:w-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-windows-msvc19.51.36248"

$printf = comdat any

$__local_stdio_printf_options = comdat any

$_vfprintf_l = comdat any

$"??_C@_0BM@NLNLBMNN@Ecuacion?5leida?3?52x?$CL3y?5?$DN?510?6?$AA@" = comdat any

$"??_C@_0CI@LOHGINBE@Extraido?3?5Coeficiente?52?5con?5Vari@" = comdat any

$"??_C@_0CI@FAOGFBMC@Extraido?3?5Coeficiente?53?5con?5Vari@" = comdat any

$"??_C@_0BL@KHNIMGH@Ecuacion?5leida?3?51x?91y?5?$DN?55?6?$AA@" = comdat any

$"??_C@_0CI@FEPAFAHG@Extraido?3?5Coeficiente?51?5con?5Vari@" = comdat any

$"??_C@_0CI@FFDCDKEB@Extraido?3?5Coeficiente?51?5con?5Vari@" = comdat any

$"??_C@_0DH@MOIFILGJ@?6?$DO?$DO?5INICIANDO?5ENTORNO?5MULTIAGENT@" = comdat any

$"??_C@_0CK@IDICNHMI@Analizando?5consistencia?5de?5siste@" = comdat any

$"??_C@_0CL@LAOGCLBB@2?5ecuaciones?5con?52?5incognitas?5de@" = comdat any

$"??_C@_0CJ@JJBEAIFL@Estado?3?5Sistema?5determinado?1comp@" = comdat any

$"??_C@_0DA@MOBHEL@Generando?5espacio?5de?5matriz?5para@" = comdat any

$"??_C@_0CP@POMFJAFD@Resultado?5final?5calculado?3?5x?5?$DN?55@" = comdat any

$"??_C@_0EJ@DPLKABPD@?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9@" = comdat any

$"??_C@_0BM@FOOHJJMM@Ecuacion?5leida?3?55a?$CL2b?5?$DN?520?6?$AA@" = comdat any

$"??_C@_0CI@EMKPBPIP@Extraido?3?5Coeficiente?55?5con?5Vari@" = comdat any

$"??_C@_0CI@KPMHKLLC@Extraido?3?5Coeficiente?52?5con?5Vari@" = comdat any

$"??_C@_0BM@DPMKKALJ@Ecuacion?5leida?3?51a?$CL4b?5?$DN?512?6?$AA@" = comdat any

$"??_C@_0CI@EHAHMIIJ@Extraido?3?5Coeficiente?51?5con?5Vari@" = comdat any

$"??_C@_0CI@KBLLBHDH@Extraido?3?5Coeficiente?54?5con?5Vari@" = comdat any

$"??_C@_0DH@FFNCKACM@?6?$DO?$DO?5INICIANDO?5ENTORNO?5MULTIAGENT@" = comdat any

$"??_C@_0CK@BINFPMIN@Analizando?5consistencia?5de?5siste@" = comdat any

$"??_C@_0DA@JLJJDMAO@Generando?5espacio?5de?5matriz?5para@" = comdat any

$"??_C@_0DB@LDMAFDPM@Resultado?5final?5calculado?3?5a?5?$DN?53@" = comdat any

@"??_C@_0BM@NLNLBMNN@Ecuacion?5leida?3?52x?$CL3y?5?$DN?510?6?$AA@" = linkonce_odr dso_local unnamed_addr constant [28 x i8] c"Ecuacion leida: 2x+3y = 10\0A\00", comdat, align 1
@"??_C@_0CI@LOHGINBE@Extraido?3?5Coeficiente?52?5con?5Vari@" = linkonce_odr dso_local unnamed_addr constant [40 x i8] c"Extraido: Coeficiente 2 con Variable x\0A\00", comdat, align 1
@"??_C@_0CI@FAOGFBMC@Extraido?3?5Coeficiente?53?5con?5Vari@" = linkonce_odr dso_local unnamed_addr constant [40 x i8] c"Extraido: Coeficiente 3 con Variable y\0A\00", comdat, align 1
@"??_C@_0BL@KHNIMGH@Ecuacion?5leida?3?51x?91y?5?$DN?55?6?$AA@" = linkonce_odr dso_local unnamed_addr constant [27 x i8] c"Ecuacion leida: 1x-1y = 5\0A\00", comdat, align 1
@"??_C@_0CI@FEPAFAHG@Extraido?3?5Coeficiente?51?5con?5Vari@" = linkonce_odr dso_local unnamed_addr constant [40 x i8] c"Extraido: Coeficiente 1 con Variable x\0A\00", comdat, align 1
@"??_C@_0CI@FFDCDKEB@Extraido?3?5Coeficiente?51?5con?5Vari@" = linkonce_odr dso_local unnamed_addr constant [40 x i8] c"Extraido: Coeficiente 1 con Variable y\0A\00", comdat, align 1
@"??_C@_0DH@MOIFILGJ@?6?$DO?$DO?5INICIANDO?5ENTORNO?5MULTIAGENT@" = linkonce_odr dso_local unnamed_addr constant [55 x i8] c"\0A>> INICIANDO ENTORNO MULTIAGENTE PARA: sistema_XY <<\0A\00", comdat, align 1
@"??_C@_0CK@IDICNHMI@Analizando?5consistencia?5de?5siste@" = linkonce_odr dso_local unnamed_addr constant [42 x i8] c"Analizando consistencia de sistema_XY...\0A\00", comdat, align 1
@"??_C@_0CL@LAOGCLBB@2?5ecuaciones?5con?52?5incognitas?5de@" = linkonce_odr dso_local unnamed_addr constant [43 x i8] c"2 ecuaciones con 2 incognitas detectadas.\0A\00", comdat, align 1
@"??_C@_0CJ@JJBEAIFL@Estado?3?5Sistema?5determinado?1comp@" = linkonce_odr dso_local unnamed_addr constant [41 x i8] c"Estado: Sistema determinado/compatible.\0A\00", comdat, align 1
@"??_C@_0DA@MOBHEL@Generando?5espacio?5de?5matriz?5para@" = linkonce_odr dso_local unnamed_addr constant [48 x i8] c"Generando espacio de matriz para sistema_XY...\0A\00", comdat, align 1
@"??_C@_0CP@POMFJAFD@Resultado?5final?5calculado?3?5x?5?$DN?55@" = linkonce_odr dso_local unnamed_addr constant [47 x i8] c"Resultado final calculado: x = 5.0 | y = 0.0\0A\0A\00", comdat, align 1
@"??_C@_0EJ@DPLKABPD@?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9@" = linkonce_odr dso_local unnamed_addr constant [73 x i8] c"----------------------------------------------------------------------\0A\0A\00", comdat, align 1
@"??_C@_0BM@FOOHJJMM@Ecuacion?5leida?3?55a?$CL2b?5?$DN?520?6?$AA@" = linkonce_odr dso_local unnamed_addr constant [28 x i8] c"Ecuacion leida: 5a+2b = 20\0A\00", comdat, align 1
@"??_C@_0CI@EMKPBPIP@Extraido?3?5Coeficiente?55?5con?5Vari@" = linkonce_odr dso_local unnamed_addr constant [40 x i8] c"Extraido: Coeficiente 5 con Variable a\0A\00", comdat, align 1
@"??_C@_0CI@KPMHKLLC@Extraido?3?5Coeficiente?52?5con?5Vari@" = linkonce_odr dso_local unnamed_addr constant [40 x i8] c"Extraido: Coeficiente 2 con Variable b\0A\00", comdat, align 1
@"??_C@_0BM@DPMKKALJ@Ecuacion?5leida?3?51a?$CL4b?5?$DN?512?6?$AA@" = linkonce_odr dso_local unnamed_addr constant [28 x i8] c"Ecuacion leida: 1a+4b = 12\0A\00", comdat, align 1
@"??_C@_0CI@EHAHMIIJ@Extraido?3?5Coeficiente?51?5con?5Vari@" = linkonce_odr dso_local unnamed_addr constant [40 x i8] c"Extraido: Coeficiente 1 con Variable a\0A\00", comdat, align 1
@"??_C@_0CI@KBLLBHDH@Extraido?3?5Coeficiente?54?5con?5Vari@" = linkonce_odr dso_local unnamed_addr constant [40 x i8] c"Extraido: Coeficiente 4 con Variable b\0A\00", comdat, align 1
@"??_C@_0DH@FFNCKACM@?6?$DO?$DO?5INICIANDO?5ENTORNO?5MULTIAGENT@" = linkonce_odr dso_local unnamed_addr constant [55 x i8] c"\0A>> INICIANDO ENTORNO MULTIAGENTE PARA: sistema_AB <<\0A\00", comdat, align 1
@"??_C@_0CK@BINFPMIN@Analizando?5consistencia?5de?5siste@" = linkonce_odr dso_local unnamed_addr constant [42 x i8] c"Analizando consistencia de sistema_AB...\0A\00", comdat, align 1
@"??_C@_0DA@JLJJDMAO@Generando?5espacio?5de?5matriz?5para@" = linkonce_odr dso_local unnamed_addr constant [48 x i8] c"Generando espacio de matriz para sistema_AB...\0A\00", comdat, align 1
@"??_C@_0DB@LDMAFDPM@Resultado?5final?5calculado?3?5a?5?$DN?53@" = linkonce_odr dso_local unnamed_addr constant [49 x i8] c"Resultado final calculado: a = 3.11 | b = 2.22\0A\0A\00", comdat, align 1
@__local_stdio_printf_options._OptionsStorage = internal global i64 0, align 8

; Function Attrs: noinline nounwind optnone uwtable
define dso_local void @resolver_sistema_sel() local_unnamed_addr #0 {
  %1 = call i32 (ptr, ...) @printf(ptr noundef @"??_C@_0BM@NLNLBMNN@Ecuacion?5leida?3?52x?$CL3y?5?$DN?510?6?$AA@")
  %2 = call i32 (ptr, ...) @printf(ptr noundef @"??_C@_0CI@LOHGINBE@Extraido?3?5Coeficiente?52?5con?5Vari@")
  %3 = call i32 (ptr, ...) @printf(ptr noundef @"??_C@_0CI@FAOGFBMC@Extraido?3?5Coeficiente?53?5con?5Vari@")
  %4 = call i32 (ptr, ...) @printf(ptr noundef @"??_C@_0BL@KHNIMGH@Ecuacion?5leida?3?51x?91y?5?$DN?55?6?$AA@")
  %5 = call i32 (ptr, ...) @printf(ptr noundef @"??_C@_0CI@FEPAFAHG@Extraido?3?5Coeficiente?51?5con?5Vari@")
  %6 = call i32 (ptr, ...) @printf(ptr noundef @"??_C@_0CI@FFDCDKEB@Extraido?3?5Coeficiente?51?5con?5Vari@")
  %7 = call i32 (ptr, ...) @printf(ptr noundef @"??_C@_0DH@MOIFILGJ@?6?$DO?$DO?5INICIANDO?5ENTORNO?5MULTIAGENT@")
  %8 = call i32 (ptr, ...) @printf(ptr noundef @"??_C@_0CK@IDICNHMI@Analizando?5consistencia?5de?5siste@")
  %9 = call i32 (ptr, ...) @printf(ptr noundef @"??_C@_0CL@LAOGCLBB@2?5ecuaciones?5con?52?5incognitas?5de@")
  %10 = call i32 (ptr, ...) @printf(ptr noundef @"??_C@_0CJ@JJBEAIFL@Estado?3?5Sistema?5determinado?1comp@")
  %11 = call i32 (ptr, ...) @printf(ptr noundef @"??_C@_0DA@MOBHEL@Generando?5espacio?5de?5matriz?5para@")
  %12 = call i32 (ptr, ...) @printf(ptr noundef @"??_C@_0CP@POMFJAFD@Resultado?5final?5calculado?3?5x?5?$DN?55@")
  %13 = call i32 (ptr, ...) @printf(ptr noundef @"??_C@_0EJ@DPLKABPD@?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9@")
  %14 = call i32 (ptr, ...) @printf(ptr noundef @"??_C@_0BM@FOOHJJMM@Ecuacion?5leida?3?55a?$CL2b?5?$DN?520?6?$AA@")
  %15 = call i32 (ptr, ...) @printf(ptr noundef @"??_C@_0CI@EMKPBPIP@Extraido?3?5Coeficiente?55?5con?5Vari@")
  %16 = call i32 (ptr, ...) @printf(ptr noundef @"??_C@_0CI@KPMHKLLC@Extraido?3?5Coeficiente?52?5con?5Vari@")
  %17 = call i32 (ptr, ...) @printf(ptr noundef @"??_C@_0BM@DPMKKALJ@Ecuacion?5leida?3?51a?$CL4b?5?$DN?512?6?$AA@")
  %18 = call i32 (ptr, ...) @printf(ptr noundef @"??_C@_0CI@EHAHMIIJ@Extraido?3?5Coeficiente?51?5con?5Vari@")
  %19 = call i32 (ptr, ...) @printf(ptr noundef @"??_C@_0CI@KBLLBHDH@Extraido?3?5Coeficiente?54?5con?5Vari@")
  %20 = call i32 (ptr, ...) @printf(ptr noundef @"??_C@_0DH@FFNCKACM@?6?$DO?$DO?5INICIANDO?5ENTORNO?5MULTIAGENT@")
  %21 = call i32 (ptr, ...) @printf(ptr noundef @"??_C@_0CK@BINFPMIN@Analizando?5consistencia?5de?5siste@")
  %22 = call i32 (ptr, ...) @printf(ptr noundef @"??_C@_0CL@LAOGCLBB@2?5ecuaciones?5con?52?5incognitas?5de@")
  %23 = call i32 (ptr, ...) @printf(ptr noundef @"??_C@_0CJ@JJBEAIFL@Estado?3?5Sistema?5determinado?1comp@")
  %24 = call i32 (ptr, ...) @printf(ptr noundef @"??_C@_0DA@JLJJDMAO@Generando?5espacio?5de?5matriz?5para@")
  %25 = call i32 (ptr, ...) @printf(ptr noundef @"??_C@_0DB@LDMAFDPM@Resultado?5final?5calculado?3?5a?5?$DN?53@")
  %26 = call i32 (ptr, ...) @printf(ptr noundef @"??_C@_0EJ@DPLKABPD@?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9?9@")
  ret void
}

; Function Attrs: noinline nounwind optnone uwtable
define linkonce_odr dso_local i32 @printf(ptr noundef %0, ...) local_unnamed_addr #0 comdat {
  %2 = alloca ptr, align 8
  %3 = alloca i32, align 4
  %4 = alloca ptr, align 8
  store ptr %0, ptr %2, align 8
  call void @llvm.va_start.p0(ptr %4)
  %5 = load ptr, ptr %4, align 8
  %6 = load ptr, ptr %2, align 8
  %7 = call ptr @__acrt_iob_func(i32 noundef 1)
  %8 = call i32 @_vfprintf_l(ptr noundef %7, ptr noundef %6, ptr noundef null, ptr noundef %5)
  store i32 %8, ptr %3, align 4
  call void @llvm.va_end.p0(ptr %4)
  %9 = load i32, ptr %3, align 4
  ret i32 %9
}

; Function Attrs: mustprogress nocallback nofree nosync nounwind willreturn
declare void @llvm.va_start.p0(ptr) #1

; Function Attrs: mustprogress nocallback nofree nosync nounwind willreturn
declare void @llvm.va_end.p0(ptr) #1

; Function Attrs: noinline nounwind optnone uwtable
define linkonce_odr dso_local ptr @__local_stdio_printf_options() local_unnamed_addr #0 comdat {
  ret ptr @__local_stdio_printf_options._OptionsStorage
}

; Function Attrs: noinline nounwind optnone uwtable
define linkonce_odr dso_local i32 @_vfprintf_l(ptr noundef %0, ptr noundef %1, ptr noundef %2, ptr noundef %3) local_unnamed_addr #0 comdat {
  %5 = alloca ptr, align 8
  %6 = alloca ptr, align 8
  %7 = alloca ptr, align 8
  %8 = alloca ptr, align 8
  store ptr %3, ptr %5, align 8
  store ptr %2, ptr %6, align 8
  store ptr %1, ptr %7, align 8
  store ptr %0, ptr %8, align 8
  %9 = load ptr, ptr %5, align 8
  %10 = load ptr, ptr %6, align 8
  %11 = load ptr, ptr %7, align 8
  %12 = load ptr, ptr %8, align 8
  %13 = call ptr @__local_stdio_printf_options()
  %14 = load i64, ptr %13, align 8
  %15 = call i32 @__stdio_common_vfprintf(i64 noundef %14, ptr noundef %12, ptr noundef %11, ptr noundef %10, ptr noundef %9)
  ret i32 %15
}

declare dso_local ptr @__acrt_iob_func(i32 noundef) local_unnamed_addr #2

declare dso_local i32 @__stdio_common_vfprintf(i64 noundef, ptr noundef, ptr noundef, ptr noundef, ptr noundef) local_unnamed_addr #2

attributes #0 = { noinline nounwind optnone uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #1 = { mustprogress nocallback nofree nosync nounwind willreturn }
attributes #2 = { "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }

!llvm.dbg.cu = !{!0}
!llvm.module.flags = !{!2, !3, !4, !5, !6}
!llvm.ident = !{!7}

!0 = distinct !DICompileUnit(language: DW_LANG_C11, file: !1, producer: "clang version 22.1.6 (https://github.com/llvm/llvm-project fc4aad7b5db3fff421df9a9637605b9ca5667881)", isOptimized: false, runtimeVersion: 0, emissionKind: NoDebug, splitDebugInlining: false, nameTableKind: None)
!1 = !DIFile(filename: "solve_sel_bridge.c", directory: "C:\\Users\\User\\Documents\\COMPILADORES_PROYECTO_FINAL")
!2 = !{i32 2, !"Debug Info Version", i32 3}
!3 = !{i32 1, !"wchar_size", i32 2}
!4 = !{i32 8, !"PIC Level", i32 2}
!5 = !{i32 7, !"uwtable", i32 2}
!6 = !{i32 1, !"MaxTLSAlign", i32 65536}
!7 = !{!"clang version 22.1.6 (https://github.com/llvm/llvm-project fc4aad7b5db3fff421df9a9637605b9ca5667881)"}
