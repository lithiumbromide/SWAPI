---
title: "RunMacro2 Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "RunMacro2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RunMacro2.html"
---

# RunMacro2 Method (ISldWorks)

Runs a macro from a project file.

## Syntax

### Visual Basic (Declaration)

```vb
Function RunMacro2( _
   ByVal FilePathName As System.String, _
   ByVal ModuleName As System.String, _
   ByVal ProcedureName As System.String, _
   ByVal Options As System.Integer, _
   ByRef Error As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim FilePathName As System.String
Dim ModuleName As System.String
Dim ProcedureName As System.String
Dim Options As System.Integer
Dim Error As System.Integer
Dim value As System.Boolean

value = instance.RunMacro2(FilePathName, ModuleName, ProcedureName, Options, Error)
```

### C#

```csharp
System.bool RunMacro2(
   System.string FilePathName,
   System.string ModuleName,
   System.string ProcedureName,
   System.int Options,
   out System.int Error
)
```

### C++/CLI

```cpp
System.bool RunMacro2(
   System.String^ FilePathName,
   System.String^ ModuleName,
   System.String^ ProcedureName,
   System.int Options,
   [Out] System.int Error
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FilePathName`: Path and filename of the project file containing the macro
- `ModuleName`: Name of the module in the macro
- `ProcedureName`: Name of the procedure in the module
- `Options`: Option as defined [swRunMacroOption_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRunMacroOption_e.html) (supports VBA macros only)
- `Error`: Error as defined by [swRunMacroError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRunMacroError_e.html) (supports VBA macros only)

### Return Value

True if macro runs, false if not

## VBA Syntax

See [SldWorks::RunMacro2](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~RunMacro2.html).

## Examples

**Visual Basic for Applications (VBA)**

1. Create two VBA macros using the following code samples.
2. Store **RunMacroSub.swp** in **c:\test**.
3. Run **RunMacro.swp**.

'----------------------------
' RunMacro.swp
'---------------------------

Option Explicit
Dim swApp As SldWorks.SldWorks
Dim boolstatus As Boolean
Sub main()
Set swApp = Application.SldWorks
Dim runMacroError As Long
boolstatus = swApp.**RunMacro2**("c:\test\RunMacroSub.swp", "RunMacroSub1", "main", swRunMacroUnloadAfterRun, runMacroError)
End Sub

'---------------------------------------
' RunMacroSub.swp
'---------------------------------------
Option Explicit
Dim swApp As SldWorks.SldWorks
Sub alternate()
Set swApp = Application.SldWorks
swApp.SendMsgToUser "RunMacroSub1:alternate() called."
End Sub
Sub main()
Set swApp = Application.SldWorks
swApp.SendMsgToUser "RunMacroSub1:main() called."
End Sub

**Running a C# DLL from VBA**

boolstatus = Me.swApp.**RunMacro2**('C:\Test\CSharpMacro\SwMacro\bin\Release\CSharpMacro.dll',

'', 'Main', swRunMacroOption_e.swRunMacroDefault, runMacroError)

## Remarks

If you specify swRunMacroUnloadAfterRun for Options, then the macro is unloaded from the VBA IDE after running.

Use the path and filename of the compiled DLL for the FilePathName argument for a .NET macro. By default, the procedure is called **Main** in a C# macro. Because C# is case sensitive, you must specify **Main** for ProcedureName in this method.. See **Running a C# DLL from VBA** in the **Example** section.

Running a macro from an add-in application, standalone .exe, or VBA macro is supported. Running a .NET macro from a .NET macro is also supported, but only if both .NET macros were created using the same VSTA version.

See [SOLIDWORKS Macros](sldworksAPIProgGuide.chm::/GettingStarted/SOLIDWORKS_Macros.htm) for details.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::GetCurrentMacroPathFolder Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentMacroPathFolder.html)
[ISldWorks::GetCurrentMacroPathName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentMacroPathName.html)
[ISldWorks::GetMacroMethods Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetMacroMethods.html)
[ISldWorks::RunAttachedMacro Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RunAttachedMacro.html)
[ISldWorks::RecordLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RecordLine.html)
[ISldWorks::RecordLineCSharp Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RecordLineCSharp.html)
[ISldWorks::RecordLineVBnet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RecordLineVBnet.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
