---
title: "ExportToBmp Method (IDocumentExporter)"
project: ""
interface: "IDocumentExporter"
member: "ExportToBmp"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocumentExporter~ExportToBmp.html"
---

# ExportToBmp Method (IDocumentExporter)

Saves the current view of the drawing as a **.bmp** (Bitmap) file.

## Syntax

### Visual Basic

```vb
Sub ExportToBmp( _
   ByVal PathName As System.String, _
   ByRef Success As System.Boolean _
)
```

### C#

```csharp
void ExportToBmp(
   System.string PathName,
   out System.bool Success
)
```

### JScript

```
function ExportToBmp(
   PathName : System.String,
   Success : System.boolean
);
```

### Managed Extensions for C++

```
void ExportToBmp(
   System.string* PathName,
   [PARAMFLAG::Out] System.bool Success
)
```

### C++/CLI

```cpp
void ExportToBmp(
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
