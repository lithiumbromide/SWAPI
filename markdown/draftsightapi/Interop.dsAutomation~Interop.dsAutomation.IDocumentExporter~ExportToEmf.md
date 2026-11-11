---
title: "ExportToEmf Method (IDocumentExporter)"
project: ""
interface: "IDocumentExporter"
member: "ExportToEmf"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocumentExporter~ExportToEmf.html"
---

# ExportToEmf Method (IDocumentExporter)

Saves the current view of the drawing as a **.emf** (Microsoft Windows Enhanced Metafile) file.

## Syntax

### Visual Basic

```vb
Sub ExportToEmf( _
   ByVal PathName As System.String, _
   ByRef Success As System.Boolean _
)
```

### C#

```csharp
void ExportToEmf(
   System.string PathName,
   out System.bool Success
)
```

### JScript

```
function ExportToEmf(
   PathName : System.String,
   Success : System.boolean
);
```

### Managed Extensions for C++

```
void ExportToEmf(
   System.string* PathName,
   [PARAMFLAG::Out] System.bool Success
)
```

### C++/CLI

```cpp
void ExportToEmf(
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
