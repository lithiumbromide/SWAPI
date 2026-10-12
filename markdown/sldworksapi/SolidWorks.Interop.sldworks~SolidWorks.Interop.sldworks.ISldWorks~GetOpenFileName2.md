---
title: "GetOpenFileName2 Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetOpenFileName2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenFileName2.html"
---

# GetOpenFileName2 Method (ISldWorks)

Prompts the user for the name of the file to open.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetOpenFileName2( _
   ByVal DialogTitle As System.String, _
   ByVal InitialFileName As System.String, _
   ByVal FileFilter As System.String, _
   ByRef OpenOptions As System.Integer, _
   ByRef ConfigName As System.String, _
   ByRef DisplayName As System.String, _
   ByRef DisplayStateName As System.String _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim DialogTitle As System.String
Dim InitialFileName As System.String
Dim FileFilter As System.String
Dim OpenOptions As System.Integer
Dim ConfigName As System.String
Dim DisplayName As System.String
Dim DisplayStateName As System.String
Dim value As System.String

value = instance.GetOpenFileName2(DialogTitle, InitialFileName, FileFilter, OpenOptions, ConfigName, DisplayName, DisplayStateName)
```

### C#

```csharp
System.string GetOpenFileName2(
   System.string DialogTitle,
   System.string InitialFileName,
   System.string FileFilter,
   out System.int OpenOptions,
   out System.string ConfigName,
   out System.string DisplayName,
   out System.string DisplayStateName
)
```

### C++/CLI

```cpp
System.String^ GetOpenFileName2(
   System.String^ DialogTitle,
   System.String^ InitialFileName,
   System.String^ FileFilter,
   [Out] System.int OpenOptions,
   [Out] System.String^ ConfigName,
   [Out] System.String^ DisplayName,
   [Out] System.String^ DisplayStateName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DialogTitle`: Title of the dialog
- `InitialFileName`: Path and file name of the file to open
- `FileFilter`: File name extension of the file to open
- `OpenOptions`: Open options as defined by [swGetOpenFileNameOptions_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swGetOpenFileNameOptions_e.html)
- `ConfigName`: Name of configuration of InitialFileName; comma-separated list of sheet names beginning with active sheet if OpenOptions is swGetOpenFileNameOptions_e.swGetOpenFileNameOptions_SelectedSheets
- `DisplayName`: Recommended name to use for opened file
- `DisplayStateName`: Selected display state name

### Return Value

Path and file name of the file to open

## VBA Syntax

See [SldWorks::GetOpenFileName2](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetOpenFileName2.html).

## Examples

[Open File (VBA)](Open_File_Example_VB.htm)

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
