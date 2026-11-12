---
title: "RunAttachedMacro Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "RunAttachedMacro"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RunAttachedMacro.html"
---

# RunAttachedMacro Method (ISldWorks)

Runs the specified attached macro, module, and procedure.

## Syntax

### Visual Basic (Declaration)

```vb
Function RunAttachedMacro( _
   ByVal FileName As System.String, _
   ByVal ModuleName As System.String, _
   ByVal ProcedureName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim FileName As System.String
Dim ModuleName As System.String
Dim ProcedureName As System.String
Dim value As System.Boolean

value = instance.RunAttachedMacro(FileName, ModuleName, ProcedureName)
```

### C#

```csharp
System.bool RunAttachedMacro(
   System.string FileName,
   System.string ModuleName,
   System.string ProcedureName
)
```

### C++/CLI

```cpp
System.bool RunAttachedMacro(
   System.String^ FileName,
   System.String^ ModuleName,
   System.String^ ProcedureName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Filename of macro to run (do not include a path)
- `ModuleName`: Module of specified macro to run
- `ProcedureName`: Procedure of specified macro to run

### Return Value

True if macro runs, false if not

## VBA Syntax

See [SldWorks::RunAttachedMacro](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~RunAttachedMacro.html).

## Examples

**Visual Basic for Applications (VBA)**

Create two VBA macros using the following code samples. Attach **RunMacroSub.swp** to the active document's Design Binder. Then run **RunAttachedMacro.swp**.

'--------------------------------------
' RunAttachedMacro.swp
'-------------------------------------
Option Explicit
Dim swApp As SldWorks.SldWorks
Dim boolstatus As Boolean

Sub main()
Set swApp = Application.SldWorks
Dim RunMacroError As Long
boolstatus = swApp.**RunAttachedMacro**("RunMacroSub.swp", "RunMacroSub1", "main")
End Sub

'---------------------------------------
' RunMacroSub.swp'
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

## Remarks

An example of an attached macro is a macro that is attached to the active document's Design Binder.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::RunMacro2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RunMacro2.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
