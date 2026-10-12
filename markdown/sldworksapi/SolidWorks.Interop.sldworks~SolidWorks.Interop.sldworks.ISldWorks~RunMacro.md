---
title: "RunMacro Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "RunMacro"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RunMacro.html"
---

# RunMacro Method (ISldWorks)

Obsolete. Superseded by [ISldWorks::RunMacro2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~RunMacro2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function RunMacro( _
   ByVal FilePathName As System.String, _
   ByVal ModuleName As System.String, _
   ByVal ProcedureName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim FilePathName As System.String
Dim ModuleName As System.String
Dim ProcedureName As System.String
Dim value As System.Boolean

value = instance.RunMacro(FilePathName, ModuleName, ProcedureName)
```

### C#

```csharp
System.bool RunMacro(
   System.string FilePathName,
   System.string ModuleName,
   System.string ProcedureName
)
```

### C++/CLI

```cpp
System.bool RunMacro(
   System.String^ FilePathName,
   System.String^ ModuleName,
   System.String^ ProcedureName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FilePathName`: Path and file name of the project file containing the macro
- `ModuleName`: Name of the module in the macro
- `ProcedureName`: Name of the procedure in the module

### Return Value

True if macro runs successfully, false if not

## VBA Syntax

See [SldWorks::RunMacro](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~RunMacro.html).

## Examples

[Run Macro (VBA)](Run_Macro_VB.htm)

## Remarks

See [SOLIDWORKS Macros](sldworksAPIProgGuide.chm::/GettingStarted/SOLIDWORKS_Macros.htm) for details.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::GetCurrentMacroPathFolder Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentMacroPathFolder.html)
[ISldWorks::GetCurrentMacroPathName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentMacroPathName.html)
[ISldWorks::RecordLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RecordLine.html)
[ISldWorks::GetMacroMethods Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetMacroMethods.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
