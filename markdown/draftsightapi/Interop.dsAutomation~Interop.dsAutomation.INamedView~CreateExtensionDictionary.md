---
title: "CreateExtensionDictionary Method (INamedView)"
project: ""
interface: "INamedView"
member: "CreateExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.INamedView~CreateExtensionDictionary.html"
---

# CreateExtensionDictionary Method (INamedView)

Creates a dictionary for the named view.

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
| Already exists for the named view | Not overwritten; instead, the existing dictionary is returned. |
| Was erased by either INamedView::ReleaseExtensionDictionary or IDictionary::Erased | Restored. NOTE : If the drawing is closed with the dictionary erased, then the dictionary is deleted from the drawing and cannot be restored. |

## See Also

[INamedView Interface](Interop.dsAutomation~Interop.dsAutomation.INamedView.html)
[INamedView Members](Interop.dsAutomation~Interop.dsAutomation.INamedView_members.html)
[INamedView::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.INamedView~GetExtensionDictionary.html)

## Availability

DraftSight V1R4.0
