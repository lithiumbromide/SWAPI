---
title: "CopySheet Method (IDocument)"
project: ""
interface: "IDocument"
member: "CopySheet"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~CopySheet.html"
---

# CopySheet Method (IDocument)

Creates a new Sheet by copying the specified existing Sheet.

## Syntax

### Visual Basic

```vb
Function CopySheet( _
   ByVal Name As System.String, _
   ByVal SheetToCopy As System.String _
) As Sheet
```

### C#

```csharp
Sheet CopySheet(
   System.string Name,
   System.string SheetToCopy
)
```

### JScript

```
function CopySheet(
   Name : System.String,
   SheetToCopy : System.String
) : Sheet;
```

### Managed Extensions for C++

```
Sheet* CopySheet(
   System.string* Name,
   System.string* SheetToCopy
)
```

### C++/CLI

```cpp
Sheet^ CopySheet(
   System.String^ Name,
   System.String^ SheetToCopy
)
```

### Parameters

- `Name`: Name of the new sheet to create
- `SheetToCopy`: Name of the existing sheet to copy to create the new sheet

### Return Value

New [Sheet](Interop.dsAutomation~Interop.dsAutomation.ISheet.html)

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)
[IDocument::CreateSheet Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~CreateSheet.html)
[IDocument::CreateSheetByTemplate Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~CreateSheetByTemplate.html)
[IDocument::GetSheet Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetSheet.html)
[IDocument::GetSheets Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetSheets.html)
[IDocument::HasSheet Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~HasSheet.html)
[IDocument::RemoveSheet Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~RemoveSheet.html)

## Availability

DraftSight V1R5.0
