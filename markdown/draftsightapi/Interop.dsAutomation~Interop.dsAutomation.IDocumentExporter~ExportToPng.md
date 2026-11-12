---
title: "ExportToPng Method (IDocumentExporter)"
project: ""
interface: "IDocumentExporter"
member: "ExportToPng"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocumentExporter~ExportToPng.html"
---

# ExportToPng Method (IDocumentExporter)

Saves the current view of the drawing as a **.png** (Portable Network Graphics bitmap image) file.

## Syntax

### Visual Basic

```vb
Sub ExportToPng( _
   ByVal PathName As System.String, _
   ByRef Success As System.Boolean _
)
```

### C#

```csharp
void ExportToPng(
   System.string PathName,
   out System.bool Success
)
```

### JScript

```
function ExportToPng(
   PathName : System.String,
   Success : System.boolean
);
```

### Managed Extensions for C++

```
void ExportToPng(
   System.string* PathName,
   [PARAMFLAG::Out] System.bool Success
)
```

### C++/CLI

```cpp
void ExportToPng(
   System.String^ PathName,
   [Out] System.bool Success
)
```

### Parameters

- `PathName`: Path and file name to which to save the current view of the drawing
- `Success`: True if the current view of the drawing is saved, false if not

## Examples

See [Export File as Specified File Type (COM native C++)](Export_File_as_Specified_File_Type_CPPCOM.htm).

## Examples

[Get DimensionStyle Names and Options (C#)](Get_DimensionStyle_Names_and_Options_Example_CSharp.htm)
[Get DimensionStyle Names and Options (VB.NET)](Get_DimensionStyle_Names_and_Options_Example_VBNET.htm)
[Get DimensionStyle Names and Options (VBA)](Get_DimensionStyle_Names_and_Options_Example_VBA.htm)
[Get DimensionStyle Names and Options (JavaScript)](Get_DimensionStyle_Names_and_Options_Example_JS.htm)

## See Also

[IDocumentExporter Interface](Interop.dsAutomation~Interop.dsAutomation.IDocumentExporter.html)
[IDocumentExporter Members](Interop.dsAutomation~Interop.dsAutomation.IDocumentExporter_members.html)

## Availability

DraftSight V1R1
