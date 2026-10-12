---
title: "GetSheets Method (IExportPdfData)"
project: "SOLIDWORKS API Help"
interface: "IExportPdfData"
member: "GetSheets"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData~GetSheets.html"
---

# GetSheets Method (IExportPdfData)

Gets the drawing [sheets](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISheet.html) to export.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSheets() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IExportPdfData
Dim value As System.Object

value = instance.GetSheets()
```

### C#

```csharp
System.object GetSheets()
```

### C++/CLI

```cpp
System.Object^ GetSheets();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of the names of the sheets to export

## VBA Syntax

See [ExportPdfData::GetSheets](ms-its:sldworksapivb6.chm::/sldworks~ExportPdfData~GetSheets.html).

## Remarks

Call [IModelDocExtension::SaveAs](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SaveAs.html) after calling this method.

## See Also

[IExportPdfData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData.html)
[IExportPdfData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData_members.html)
[IExportPdfData::GetWhichSheets Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData~GetWhichSheets.html)
[IExportPdfData::SetSheets Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData~SetSheets.html)

## Availability

SOLIDWORKS 2007 SP1, Revision Number 15
