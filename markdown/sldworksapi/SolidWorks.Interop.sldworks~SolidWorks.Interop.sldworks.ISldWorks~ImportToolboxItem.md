---
title: "ImportToolboxItem Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "ImportToolboxItem"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ImportToolboxItem.html"
---

# ImportToolboxItem Method (ISldWorks)

Imports data for the specified Toolbox standard.

## Syntax

### Visual Basic (Declaration)

```vb
Function ImportToolboxItem( _
   ByVal StdToImport As System.String, _
   ByVal DestinationFilePath As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim StdToImport As System.String
Dim DestinationFilePath As System.String
Dim value As System.Integer

value = instance.ImportToolboxItem(StdToImport, DestinationFilePath)
```

### C#

```csharp
System.int ImportToolboxItem(
   System.string StdToImport,
   System.string DestinationFilePath
)
```

### C++/CLI

```cpp
System.int ImportToolboxItem(
   System.String^ StdToImport,
   System.String^ DestinationFilePath
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `StdToImport`: Standard to import (see **Remarks**)
- `DestinationFilePath`: Path and name of file to import (see **Remarks**)

### Return Value

0 if the Toolbox standard imported successfully, 1 if not

## VBA Syntax

See [SldWorks::ImportToolboxItem](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~ImportToolboxItem.html).

## Examples

```
'VBA Preconditions'
```

```
'Open a part.
```

```
'Ensure the *.xlsx file exists.
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

    SourceHWItem = "ansi inch\bolts and screws\hex head\heavy hex bolt_ai.sldprt"

    DestinationFolderName = "C:\temp\AI_Heavy Hex Bolt.xlsx"

    longstatus = swApp.ImportToolboxItem(SourceHWItem, DestinationFolderName)

    Exit Sub
```

```
End Sub
```

## Remarks

Specify StdToImport with the path and file name beneath **C:\SOLIDWORKS Data\browser**, e.g., "**ansi inch\bolts and screws\hex head\heavy hex bolt_ai.sldprt**".

Specify DestinationFilePath with the path and file name of the Excel Workbook (***.xslx**) you want to import. The Excel file name is formatted as follows:

`standard`**_**`hole class`**_**`hole type`**.xslx**

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::ExportToolboxItem Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ExportToolboxItem.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
