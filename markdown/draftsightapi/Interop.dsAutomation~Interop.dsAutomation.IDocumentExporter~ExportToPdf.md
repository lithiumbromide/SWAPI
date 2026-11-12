---
title: "ExportToPdf Method (IDocumentExporter)"
project: ""
interface: "IDocumentExporter"
member: "ExportToPdf"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocumentExporter~ExportToPdf.html"
---

# ExportToPdf Method (IDocumentExporter)

Obsolete. Superseded by [IDocumentExporter::ExportToPdf2](Interop.dsAutomation~Interop.dsAutomation.IDocumentExporter~ExportToPdf2.html).

## Syntax

### Visual Basic

```vb
Sub ExportToPdf( _
   ByVal PathName As System.String, _
   ByVal SheetsForExportStrArray As System.Object, _
   ByVal PageLength As System.Double, _
   ByVal PageWidth As System.Double, _
   ByRef Success As System.Boolean _
)
```

### C#

```csharp
void ExportToPdf(
   System.string PathName,
   System.object SheetsForExportStrArray,
   System.double PageLength,
   System.double PageWidth,
   out System.bool Success
)
```

### JScript

```
function ExportToPdf(
   PathName : System.String,
   SheetsForExportStrArray : System.Object,
   PageLength : System.double,
   PageWidth : System.double,
   Success : System.boolean
);
```

### Managed Extensions for C++

```
void ExportToPdf(
   System.string* PathName,
   System.Object* SheetsForExportStrArray,
   System.double PageLength,
   System.double PageWidth,
   [PARAMFLAG::Out] System.bool Success
)
```

### C++/CLI

```cpp
void ExportToPdf(
   System.String^ PathName,
   System.Object^ SheetsForExportStrArray,
   System.double PageLength,
   System.double PageWidth,
   [Out] System.bool Success
)
```

### Parameters

- `PathName`: Path and filename to which to save the current view of the drawing
- `SheetsForExportStrArray`: Array of the names of the sheets in the drawing to export
- `PageLength`: Length of the page
- `PageWidth`: Width of the page
- `Success`: True if the current view of the drawing is saved, false if not

## See Also

[IDocumentExporter Interface](Interop.dsAutomation~Interop.dsAutomation.IDocumentExporter.html)
[IDocumentExporter Members](Interop.dsAutomation~Interop.dsAutomation.IDocumentExporter_members.html)

## Availability

DraftSight V1R1
