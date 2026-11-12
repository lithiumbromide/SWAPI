---
title: "GetWhichSheets Method (IExportPdfData)"
project: "SOLIDWORKS API Help"
interface: "IExportPdfData"
member: "GetWhichSheets"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData~GetWhichSheets.html"
---

# GetWhichSheets Method (IExportPdfData)

Gets the drawing [sheets](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISheet.html) to export to PDF.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetWhichSheets() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IExportPdfData
Dim value As System.Integer

value = instance.GetWhichSheets()
```

### C#

```csharp
System.int GetWhichSheets()
```

### C++/CLI

```cpp
System.int GetWhichSheets();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Drawing sheets to export to PDF as defined in [swExportDataSheetsToExport_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swExportDataSheetsToExport_e.html)

## VBA Syntax

See [ExportPdfData::GetWhichSheets](ms-its:sldworksapivb6.chm::/sldworks~ExportPdfData~GetWhichSheets.html).

## See Also

[IExportPdfData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData.html)
[IExportPdfData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData_members.html)
[IExportPdfData::GetSheets Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData~GetSheets.html)
[IExportPdfData::SetSheets Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData~SetSheets.html)

## Availability

SOLIDWORKS 2007 SP1, Revision Number 15
