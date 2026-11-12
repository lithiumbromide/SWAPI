---
title: "RemoveSheet Method (IDocument)"
project: ""
interface: "IDocument"
member: "RemoveSheet"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~RemoveSheet.html"
---

# RemoveSheet Method (IDocument)

Deletes the specified [Sheet](Interop.dsAutomation~Interop.dsAutomation.ISheet.html) from the document.

## Syntax

### Visual Basic

```vb
Sub RemoveSheet( _
   ByVal Name As System.String _
)
```

### C#

```csharp
void RemoveSheet(
   System.string Name
)
```

### JScript

```
function RemoveSheet(
   Name : System.String
);
```

### Managed Extensions for C++

```
void RemoveSheet(
   System.string* Name
)
```

### C++/CLI

```cpp
void RemoveSheet(
   System.String^ Name
)
```

### Parameters

- `Name`: Name of the Sheet to delete from the document

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)
[IDocument::CopySheet Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~CopySheet.html)
[IDocument::CreateSheet Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~CreateSheet.html)
[IDocument::CreateSheetByTemplate Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~CreateSheetByTemplate.html)
[IDocument::GetSheet Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetSheet.html)
[IDocument::GetSheets Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetSheets.html)
[IDocument::HasSheet Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~HasSheet.html)

## Availability

DraftSight V1R5.0
