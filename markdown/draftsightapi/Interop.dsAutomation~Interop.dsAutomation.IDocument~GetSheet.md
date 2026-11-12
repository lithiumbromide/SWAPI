---
title: "GetSheet Method (IDocument)"
project: ""
interface: "IDocument"
member: "GetSheet"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~GetSheet.html"
---

# GetSheet Method (IDocument)

Gets the specified Sheet.

## Syntax

### Visual Basic

```vb
Function GetSheet( _
   ByVal Name As System.String _
) As Sheet
```

### C#

```csharp
Sheet GetSheet(
   System.string Name
)
```

### JScript

```
function GetSheet(
   Name : System.String
) : Sheet;
```

### Managed Extensions for C++

```
Sheet* GetSheet(
   System.string* Name
)
```

### C++/CLI

```cpp
Sheet^ GetSheet(
   System.String^ Name
)
```

### Parameters

- `Name`: Name of the Sheet

### Return Value

[Sheet](Interop.dsAutomation~Interop.dsAutomation.ISheet.html)

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)
[IDocument::CopySheet Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~CopySheet.html)
[IDocument::CreateSheet Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~CreateSheet.html)
[IDocument::CreateSheetByTemplate Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~CreateSheetByTemplate.html)
[IDocument::GetSheets Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetSheets.html)
[IDocument::HasSheet Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~HasSheet.html)
[IDocument::RemoveSheet Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~RemoveSheet.html)

## Availability

DraftSight V1R5.0
