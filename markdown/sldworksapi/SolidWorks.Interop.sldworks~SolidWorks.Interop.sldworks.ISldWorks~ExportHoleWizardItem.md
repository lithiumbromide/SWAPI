---
title: "ExportHoleWizardItem Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "ExportHoleWizardItem"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ExportHoleWizardItem.html"
---

# ExportHoleWizardItem Method (ISldWorks)

Exports data for the specified Hole Wizard standard.

## Syntax

### Visual Basic (Declaration)

```vb
Function ExportHoleWizardItem( _
   ByVal StdToExport As System.String, _
   ByVal DestinationFolderPath As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim StdToExport As System.String
Dim DestinationFolderPath As System.String
Dim value As System.Integer

value = instance.ExportHoleWizardItem(StdToExport, DestinationFolderPath)
```

### C#

```csharp
System.int ExportHoleWizardItem(
   System.string StdToExport,
   System.string DestinationFolderPath
)
```

### C++/CLI

```cpp
System.int ExportHoleWizardItem(
   System.String^ StdToExport,
   System.String^ DestinationFolderPath
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `StdToExport`: Standard to export (see **Remarks**)
- `DestinationFolderPath`: Path where to export the data (see **Remarks**)

### Return Value

0 if successful, 1 if errors

## VBA Syntax

See [SldWorks::ExportHoleWizardItem](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~ExportHoleWizardItem.html).

## Examples

```
'VBA Preconditions'
```

```
'Open a part.
```

```
'Ensure that c:\temp exists.
```

```
Dim swApp As SldWorks.SldWorks
Dim SourceHWItem As String
Dim DestinationFoldeName As String
Dim longstatus As Long
Option Explicit
```

```
Sub Main()
```

```
    Set swApp = Application.SldWorks

    SourceHWItem = "ansi inch\Counterbore Holes\Hex Bolt"

    DestinationFolderName = "C:\temp"

    longstatus = swApp.ExportHoleWizardItem(SourceHWItem, DestinationFolderName)

    Exit Sub
```

```
End Sub
```

## Remarks

Specify StdToImport with the path and file name as shown on the Hole Wizard tab of the Toolbox, e.g., "**ansi inch\Counterbore Holes\Hex Bolt**".

Specify DestinationFolderPath with the path where to create the Excel Workbook (***.xslx**). The data is exported to a file whose name is formatted as follows:

`standard`**_**`hole class`**_**`hole type`**.xslx**

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::ImportHoleWizardItem Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ImportHoleWizardItem.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
