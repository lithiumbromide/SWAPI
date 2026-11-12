---
title: "CreateSheet Method (IDocument)"
project: ""
interface: "IDocument"
member: "CreateSheet"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~CreateSheet.html"
---

# CreateSheet Method (IDocument)

Creates a Sheet using the specified name.

## Syntax

### Visual Basic

```vb
Function CreateSheet( _
   ByVal Name As System.String _
) As Sheet
```

### C#

```csharp
Sheet CreateSheet(
   System.string Name
)
```

### JScript

```
function CreateSheet(
   Name : System.String
) : Sheet;
```

### Managed Extensions for C++

```
Sheet* CreateSheet(
   System.string* Name
)
```

### C++/CLI

```cpp
Sheet^ CreateSheet(
   System.String^ Name
)
```

### Parameters

- `Name`: Name of the Sheet to create

### Return Value

[Sheet](Interop.dsAutomation~Interop.dsAutomation.ISheet.html)

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)
[IDocument::CopySheet Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~CopySheet.html)
[IDocument::CreateSheetByTemplate Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~CreateSheetByTemplate.html)
[IDocument::GetSheet Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetSheet.html)
[IDocument::GetSheets Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetSheets.html)
[IDocument::HasSheet Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~HasSheet.html)
[IDocument::RemoveSheet Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~RemoveSheet.html)

## Availability

DraftSight V1R5.0
