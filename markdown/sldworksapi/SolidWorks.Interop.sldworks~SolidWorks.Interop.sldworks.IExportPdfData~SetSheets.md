---
title: "SetSheets Method (IExportPdfData)"
project: "SOLIDWORKS API Help"
interface: "IExportPdfData"
member: "SetSheets"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData~SetSheets.html"
---

# SetSheets Method (IExportPdfData)

Sets the drawing [sheets](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISheet.html) to export.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetSheets( _
   ByVal Which As System.Integer, _
   ByVal Sheets As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IExportPdfData
Dim Which As System.Integer
Dim Sheets As System.Object
Dim value As System.Boolean

value = instance.SetSheets(Which, Sheets)
```

### C#

```csharp
System.bool SetSheets(
   System.int Which,
   System.object Sheets
)
```

### C++/CLI

```cpp
System.bool SetSheets(
   System.int Which,
   System.Object^ Sheets
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Which`: Drawing sheets to export to PDF as defined in [swExportDataSheetsToExport_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swExportDataSheetsToExport_e.html)
- `Sheets`: Array of the names of the drawing sheets to export

### Return Value

True if the drawings sheets are set to export to PDF, false if not

## VBA Syntax

See [ExportPdfData::SetSheets](ms-its:sldworksapivb6.chm::/sldworks~ExportPdfData~SetSheets.html).

## Examples

[Save File as PDF (VBA)](Save_File_as_PDF_Example_VB.htm)
[Save File as PDF (C#)](Save_File_as_PDF_Example_CSharp.htm)
[Save File as PDF (VB.NET)](Save_File_as_PDF_Example_VBNET.htm)

## See Also

[IExportPdfData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData.html)
[IExportPdfData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData_members.html)
[IExportPdfData::GetSheets Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData~GetSheets.html)
[IExportPdfData::GetWhichSheets Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData~GetWhichSheets.html)

## Availability

SOLIDWORKS 2007 SP1, Revision Number 15
