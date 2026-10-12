---
title: "ExportToolboxItem Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "ExportToolboxItem"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ExportToolboxItem.html"
---

# ExportToolboxItem Method (ISldWorks)

Exports data for the specified Toolbox standard.

## Syntax

### Visual Basic (Declaration)

```vb
Function ExportToolboxItem( _
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

value = instance.ExportToolboxItem(StdToExport, DestinationFolderPath)
```

### C#

```csharp
System.int ExportToolboxItem(
   System.string StdToExport,
   System.string DestinationFolderPath
)
```

### C++/CLI

```cpp
System.int ExportToolboxItem(
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

See [SldWorks::ExportToolboxItem](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~ExportToolboxItem.html).

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
```

```
Option Explicit
```

```
Sub Main()
```

```
    Set swApp = Application.SldWorks

    SourceHWItem = "ansi inch\bolts and screws\hex head\heavy hex bolt_ai.sldprt"

    DestinationFolderName = "C:\temp"

    longstatus = swApp.ExportToolboxItem(SourceHWItem, DestinationFolderName)

    Exit Sub
```

```
End Sub
```

## Remarks

Specify StdToImport with the path and file name beneath **C:\SOLIDWORKS Data\browser**, e.g., "**ansi inch\bolts and screws\hex head\heavy hex bolt_ai.sldprt**".

Specify DestinationFolderPath with the path where to export the Excel Workbook (***.xslx**). The data is exported to a file whose name is formatted as follows:

`standard`**_**`hole class`**_**`hole type`**.xslx**

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::ImportToolboxItem Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ImportToolboxItem.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
