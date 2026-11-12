---
title: "HasSheet Method (IDocument)"
project: ""
interface: "IDocument"
member: "HasSheet"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~HasSheet.html"
---

# HasSheet Method (IDocument)

Gets whether the document contains the specified [Sheet](Interop.dsAutomation~Interop.dsAutomation.ISheet.html).

## Syntax

### Visual Basic

```vb
Function HasSheet( _
   ByVal Name As System.String _
) As System.Boolean
```

### C#

```csharp
System.bool HasSheet(
   System.string Name
)
```

### JScript

```
function HasSheet(
   Name : System.String
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool HasSheet(
   System.string* Name
)
```

### C++/CLI

```cpp
System.bool HasSheet(
   System.String^ Name
)
```

### Parameters

- `Name`: Name of the Sheet

### Return Value

True if the document contains the specified Sheet, false if not

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)
[IDocument::CopySheet Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~CopySheet.html)
[IDocument::CreateSheet Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~CreateSheet.html)
[IDocument::CreateSheetByTemplate Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~CreateSheetByTemplate.html)
[IDocument::GetSheet Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetSheet.html)
[IDocument::GetSheets Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetSheets.html)
[IDocument::RemoveSheet Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~RemoveSheet.html)

## Availability

DraftSight V1R5.0
