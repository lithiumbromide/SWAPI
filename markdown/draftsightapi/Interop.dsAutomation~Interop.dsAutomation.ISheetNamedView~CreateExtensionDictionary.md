---
title: "CreateExtensionDictionary Method (ISheetNamedView)"
project: ""
interface: "ISheetNamedView"
member: "CreateExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISheetNamedView~CreateExtensionDictionary.html"
---

# CreateExtensionDictionary Method (ISheetNamedView)

Creates a dictionary for the sheet named view.

## Syntax

### Visual Basic

```vb
Function CreateExtensionDictionary() As Dictionary
```

### C#

```csharp
Dictionary CreateExtensionDictionary()
```

### JScript

```
function CreateExtensionDictionary() : Dictionary;
```

### Managed Extensions for C++

```
Dictionary* CreateExtensionDictionary();
```

### C++/CLI

```cpp
Dictionary^ CreateExtensionDictionary();
```

### Return Value

[Dictionary](Interop.dsAutomation~Interop.dsAutomation.IDictionary.html)

## Remarks

| If the dictionary... | Then the dictionary is... |
| --- | --- |
| Already exists for the sheet named view | Not overwritten; instead, the existing dictionary is returned. |
| Was erased by either ISheetNamedView::ReleaseExtensionDictionary or IDictionary::Erased | Restored. NOTE : If the drawing is closed with the dictionary erased, then the dictionary is deleted from the drawing and cannot be restored. |

## See Also

[ISheetNamedView Interface](Interop.dsAutomation~Interop.dsAutomation.ISheetNamedView.html)
[ISheetNamedView Members](Interop.dsAutomation~Interop.dsAutomation.ISheetNamedView_members.html)
[ISheetNamedView::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.ISheetNamedView~GetExtensionDictionary.html)

## Availability

DraftSight V1R4.0
