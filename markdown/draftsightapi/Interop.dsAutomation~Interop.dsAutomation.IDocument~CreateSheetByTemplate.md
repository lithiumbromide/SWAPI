---
title: "CreateSheetByTemplate Method (IDocument)"
project: ""
interface: "IDocument"
member: "CreateSheetByTemplate"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~CreateSheetByTemplate.html"
---

# CreateSheetByTemplate Method (IDocument)

Creates a Sheet based on a Sheet in another file.

## Syntax

### Visual Basic

```vb
Function CreateSheetByTemplate( _
   ByVal Name As System.String, _
   ByVal TemplateFileName As System.String, _
   ByVal TemplateSheetName As System.String _
) As Sheet
```

### C#

```csharp
Sheet CreateSheetByTemplate(
   System.string Name,
   System.string TemplateFileName,
   System.string TemplateSheetName
)
```

### JScript

```
function CreateSheetByTemplate(
   Name : System.String,
   TemplateFileName : System.String,
   TemplateSheetName : System.String
) : Sheet;
```

### Managed Extensions for C++

```
Sheet* CreateSheetByTemplate(
   System.string* Name,
   System.string* TemplateFileName,
   System.string* TemplateSheetName
)
```

### C++/CLI

```cpp
Sheet^ CreateSheetByTemplate(
   System.String^ Name,
   System.String^ TemplateFileName,
   System.String^ TemplateSheetName
)
```

### Parameters

- `Name`: Name of the Sheet to create
- `TemplateFileName`: Path and file name that contains a Sheet on which to base this Sheet; the filename extension of the file must be **.dwt, .dwg**, or **.dxf**
- `TemplateSheetName`: Name of a Sheet in TemplateFileName to use as the template for this Sheet

### Return Value

[Sheet](Interop.dsAutomation~Interop.dsAutomation.ISheet.html)

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)
[IDocument::CopySheet Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~CopySheet.html)
[IDocument::CreateSheet Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~CreateSheet.html)
[IDocument::GetSheet Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetSheet.html)
[IDocument::GetSheets Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetSheets.html)
[IDocument::HasSheet Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~HasSheet.html)
[IDocument::RemoveSheet Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~RemoveSheet.html)

## Availability

DraftSight V1R5.0
