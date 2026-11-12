---
title: "GetMacroMethods Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetMacroMethods"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetMacroMethods.html"
---

# GetMacroMethods Method (ISldWorks)

Gets the names of the modules in the specified macro.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMacroMethods( _
   ByVal FilePathName As System.String, _
   ByVal Filter As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim FilePathName As System.String
Dim Filter As System.Integer
Dim value As System.Object

value = instance.GetMacroMethods(FilePathName, Filter)
```

### C#

```csharp
System.object GetMacroMethods(
   System.string FilePathName,
   System.int Filter
)
```

### C++/CLI

```cpp
System.Object^ GetMacroMethods(
   System.String^ FilePathName,
   System.int Filter
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FilePathName`: Path and macro filename whose module names you want
- `Filter`: Filter as defined in [swMacroMethods_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMacroMethods_e.html)

### Return Value

Array of names of the modules in FilePathName

## VBA Syntax

See [SldWorks::GetMacroMethods](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetMacroMethods.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::GetCurrentMacroPathFolder Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentMacroPathFolder.html)
[ISldWorks::GetCurrentMacroPathName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentMacroPathName.html)
[ISldWorks::GetCurrentWorkingDirectory Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentWorkingDirectory.html)
[ISldWorks::RunMacro Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RunMacro.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
