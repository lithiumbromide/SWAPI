---
title: "IExportPdfData Interface"
project: "SOLIDWORKS API Help"
interface: "IExportPdfData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData.html"
---

# IExportPdfData Interface

Allows access to the PDF export data interface, which allows you to save:

- one or more drawing sheets to PDF.
- parts and assemblies to 3D PDF.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IExportPdfData
```

### Visual Basic (Usage)

```vb
Dim instance As IExportPdfData
```

### C#

```csharp
public interface IExportPdfData
```

### C++/CLI

```cpp
public interface class IExportPdfData
```

## VBA Syntax

See [ExportPdfData](ms-its:sldworksapivb6.chm::/sldworks~ExportPdfData.html).

## Examples

[Save File as PDF (VBA)](Save_File_as_PDF_Example_VB.htm)
[Save File as PDF (C#)](Save_File_as_PDF_Example_CSharp.htm)
[Save File as PDF (VB.NET)](Save_File_as_PDF_Example_VBNET.htm)

## Remarks

**To export one or more drawing sheets to PDF:**

1. Get the IExportPdfData object using [ISldWorks::GetExportFileData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetExportFileData.html).
2. Set the sheets to export to PDF using [IExportPdfData::SetSheets](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IExportPdfData~SetSheets.html).
3. Set whether to view the PDF after saving using [IExportPdfData::ViewPdfAfterSaving](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IExportPdfData~ViewPdfAfterSaving.html).
4. Save the sheets using [IModelDocExtension::SaveAs](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SaveAs.html).

**To export a part or assembly to 3D PDF:**

1. Get the IExportPdfData object using [ISldWorks::GetExportFileData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetExportFileData.html).
2. Set [IExportPdfData::ExportAs3D](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IExportPdfData~ExportAs3D.html) to true.
3. Set whether to view the PDF after saving using [IExportPdfData::ViewPdfAfterSaving](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IExportPdfData~ViewPdfAfterSaving.html).
4. Save the part or assembly using [IModelDocExtension::SaveAs](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SaveAs.html).

## Accessors

[ISldWorks::GetExportFileData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetExportFileData.html)

## Access Diagram

[ExportPdfData](SWObjectModel.pdf#ExportPdfData)

## See Also

[IExportPdfData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
