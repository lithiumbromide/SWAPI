---
title: "CreateExtensionDictionary Method (IModelNamedView)"
project: ""
interface: "IModelNamedView"
member: "CreateExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IModelNamedView~CreateExtensionDictionary.html"
---

# CreateExtensionDictionary Method (IModelNamedView)

Creates a dictionary for the model named view.

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
| Already exists for the model named view | Not overwritten; instead, the existing dictionary is returned. |
| Was erased by either IModelNamedView::ReleaseExtensionDictionary or IDictionary::Erased | Restored. NOTE : If the drawing is closed with the dictionary erased, then the dictionary is deleted from the drawing and cannot be restored. |

## See Also

[IModelNamedView Interface](Interop.dsAutomation~Interop.dsAutomation.IModelNamedView.html)
[IModelNamedView Members](Interop.dsAutomation~Interop.dsAutomation.IModelNamedView_members.html)
[IModelNamedView::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IModelNamedView~GetExtensionDictionary.html)

## Availability

DraftSight V1R4.0
