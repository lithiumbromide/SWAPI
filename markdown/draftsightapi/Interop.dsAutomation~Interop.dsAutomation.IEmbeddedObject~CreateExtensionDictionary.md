---
title: "CreateExtensionDictionary Method (IEmbeddedObject)"
project: ""
interface: "IEmbeddedObject"
member: "CreateExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IEmbeddedObject~CreateExtensionDictionary.html"
---

# CreateExtensionDictionary Method (IEmbeddedObject)

Creates a dictionary for the embedded object.

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
| Already exists for the embedded object | Not overwritten; instead, the existing dictionary is returned. |
| Was erased by either IEmbeddedObject::ReleaseExtensionDictionary or IDictionary::Erased | Restored. NOTE : If the drawing is closed with the dictionary erased, then the dictionary is deleted from the drawing and cannot be restored. |

## See Also

[IEmbeddedObject Interface](Interop.dsAutomation~Interop.dsAutomation.IEmbeddedObject.html)
[IEmbeddedObject Members](Interop.dsAutomation~Interop.dsAutomation.IEmbeddedObject_members.html)
[IEmbeddedObject::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IEmbeddedObject~GetExtensionDictionary.html)

## Availability

DraftSight V1R4.0
