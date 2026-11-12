---
title: "ExportToTiff Method (IDocumentExporter)"
project: ""
interface: "IDocumentExporter"
member: "ExportToTiff"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocumentExporter~ExportToTiff.html"
---

# ExportToTiff Method (IDocumentExporter)

Saves the current view of the drawing as a **.tiff** (Tagged Image File Format) file.

## Syntax

### Visual Basic

```vb
Sub ExportToTiff( _
   ByVal PathName As System.String, _
   ByRef Success As System.Boolean _
)
```

### C#

```csharp
void ExportToTiff(
   System.string PathName,
   out System.bool Success
)
```

### JScript

```
function ExportToTiff(
   PathName : System.String,
   Success : System.boolean
);
```

### Managed Extensions for C++

```
void ExportToTiff(
   System.string* PathName,
   [PARAMFLAG::Out] System.bool Success
)
```

### C++/CLI

```cpp
void ExportToTiff(
   System.String^ PathName,
   [Out] System.bool Success
)
```

### Parameters

- `PathName`: Path and file name to which to save the current view of the drawing
- `Success`: True if the current view of the drawing is saved, false if not

## Examples

See [Export File as Specified File Type (COM native C++)](Export_File_as_Specified_File_Type_CPPCOM.htm).

## See Also

[IDocumentExporter Interface](Interop.dsAutomation~Interop.dsAutomation.IDocumentExporter.html)
[IDocumentExporter Members](Interop.dsAutomation~Interop.dsAutomation.IDocumentExporter_members.html)

## Availability

DraftSight V1R1
