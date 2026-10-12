---
title: "GetCurrentMacroPathFolder Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetCurrentMacroPathFolder"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentMacroPathFolder.html"
---

# GetCurrentMacroPathFolder Method (ISldWorks)

Gets the name of the folder where the macro resides.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCurrentMacroPathFolder() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim value As System.String

value = instance.GetCurrentMacroPathFolder()
```

### C#

```csharp
System.string GetCurrentMacroPathFolder()
```

### C++/CLI

```cpp
System.String^ GetCurrentMacroPathFolder();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Name of the folder where the macro resides

## VBA Syntax

See [SldWorks::GetCurrentMacroPathFolder](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetCurrentMacroPathFolder.html).

## Examples

[Save Solid Body to File (C#)](Save_Solid_Body_to_File_Example_CSharp.htm)
[Save Solid Body to File (VB.NET)](Save_Solid_Body_to_File_Example_VBNET.htm)
[Save Solid Body to File (VBA)](Save_Solid_Body_to_File_Example_VB.htm)

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::GetCurrentMacroPathName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentMacroPathName.html)
[ISldWorks::GetCurrentWorkingDirectory Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentWorkingDirectory.html)
[ISldWorks::GetMacroMethods Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetMacroMethods.html)
[ISldWorks::RunMacro Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RunMacro.html)

## Availability

SOLIDWORKS 2006 SP1, Revision Number 14.1
