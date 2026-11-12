---
title: "GetCurrentMacroPathName Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetCurrentMacroPathName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentMacroPathName.html"
---

# GetCurrentMacroPathName Method (ISldWorks)

Gets the path name for the macro currently running.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCurrentMacroPathName() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim value As System.String

value = instance.GetCurrentMacroPathName()
```

### C#

```csharp
System.string GetCurrentMacroPathName()
```

### C++/CLI

```cpp
System.String^ GetCurrentMacroPathName();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Path name for the macro currently running

## VBA Syntax

See [SldWorks::GetCurrentMacroPathName](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetCurrentMacroPathName.html).

## Examples

[Create Macro Feature Subfeature (VBA)](Create_Macro_Feature_Subfeature_Example_VB.htm)
[Import Models As Solids (VBA)](Import_Models_as_Solids_Example_VB.htm)
[Copy Document and Its Dependencies (VBA)](Copy_Document_and_Its_Dependencies_Example_VB.htm)
[Copy Document and Its Dependencies (VB.NET)](Copy_Document_and_Its_Dependencies_Example_VBNET.htm)
[Copy Document and Its Dependencies (C#)](Copy_Document_and_Its_Dependencies_Example_CSharp.htm)

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::GetCurrentMacroPathFolder Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentMacroPathFolder.html)
[ISldWorks::GetCurrentWorkingDirectory Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentWorkingDirectory.html)
[ISldWorks::RunMacro Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RunMacro.html)
[ISldWorks::GetMacroMethods Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetMacroMethods.html)

## Availability

SOLIDWORKS 2006 SP1, Revision Number 14.1
