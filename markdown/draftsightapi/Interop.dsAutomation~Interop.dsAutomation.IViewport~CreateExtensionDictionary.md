---
title: "CreateExtensionDictionary Method (IViewport)"
project: ""
interface: "IViewport"
member: "CreateExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IViewport~CreateExtensionDictionary.html"
---

# CreateExtensionDictionary Method (IViewport)

Creates a dictionary for the Viewport.

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
| Already exists for the Viewport | Not overwritten; instead, the existing dictionary is returned. |
| Was erased by either IViewport::ReleaseExtensionDictionary or IDictionary::Erased | Restored. NOTE : If the drawing is closed with the dictionary erased, then the dictionary is deleted from the drawing and cannot be restored. |

## See Also

[IViewport Interface](Interop.dsAutomation~Interop.dsAutomation.IViewport.html)
[IViewport Members](Interop.dsAutomation~Interop.dsAutomation.IViewport_members.html)
[IViewport::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IViewport~GetExtensionDictionary.html)

## Availability

DraftSight V1R4.0
