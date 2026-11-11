---
title: "CreateExtensionDictionary Method (IViewTile)"
project: ""
interface: "IViewTile"
member: "CreateExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IViewTile~CreateExtensionDictionary.html"
---

# CreateExtensionDictionary Method (IViewTile)

Creates a dictionary for this ViewTile.

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
| Already exists for the ViewTile | Not overwritten; instead, the existing dictionary is returned. |
| Was erased by either IViewTile::ReleaseExtensionDictionary or IDictionary::Erased | Restored. NOTE : If the drawing is closed with the dictionary erased, then the dictionary is deleted from the drawing and cannot be restored. |

## See Also

[IViewTile Interface](Interop.dsAutomation~Interop.dsAutomation.IViewTile.html)
[IViewTile Members](Interop.dsAutomation~Interop.dsAutomation.IViewTile_members.html)
[IViewTile::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IViewTile~GetExtensionDictionary.html)

## Availability

DraftSight V1R6.0
