---
title: "ExportToPdf2 Method (IDocumentExporter)"
project: ""
interface: "IDocumentExporter"
member: "ExportToPdf2"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocumentExporter~ExportToPdf2.html"
---

# ExportToPdf2 Method (IDocumentExporter)

Saves the current view of the drawing to the specified Portable Document Format (PDF) file.

## Syntax

### Visual Basic

```vb
Function ExportToPdf2( _
   ByVal PathName As System.String, _
   ByVal ExportSettings As ExportSettings _
) As System.Boolean
```

### C#

```csharp
System.bool ExportToPdf2(
   System.string PathName,
   ExportSettings ExportSettings
)
```

### JScript

```
function ExportToPdf2(
   PathName : System.String,
   ExportSettings : ExportSettings
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool ExportToPdf2(
   System.string* PathName,
   ExportSettings* ExportSettings
)
```

### C++/CLI

```cpp
System.bool ExportToPdf2(
   System.String^ PathName,
   ExportSettings^ ExportSettings
)
```

### Parameters

- `PathName`: Path and filename to which to save the current view of the drawing (***.pdf**)
- `ExportSettings`: [IExportSettings](Interop.dsAutomation~Interop.dsAutomation.IExportSettings.html)

### Return Value

True if successful, false if not

## Examples

See the [IExportSettings](Interop.dsAutomation~Interop.dsAutomation.IExportSettings.html) examples.

## See Also

[IDocumentExporter Interface](Interop.dsAutomation~Interop.dsAutomation.IDocumentExporter.html)
[IDocumentExporter Members](Interop.dsAutomation~Interop.dsAutomation.IDocumentExporter_members.html)
[IDocumentExporter::CreateExportSettings Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocumentExporter~CreateExportSettings.html)

## Availability

DraftSight 2018 SP0
