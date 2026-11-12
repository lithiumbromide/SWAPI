---
title: "CreateExtensionDictionary Method (IAttributeInstance)"
project: ""
interface: "IAttributeInstance"
member: "CreateExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance~CreateExtensionDictionary.html"
---

# CreateExtensionDictionary Method (IAttributeInstance)

Creates a dictionary for the BlockAttribute instance.

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
| Already exists for the BlockAttribute instance | Not overwritten; instead, the existing dictionary is returned. |
| Was erased by either IAttributeInstance::ReleaseExtensionDictionary or IDictionary::Erased | Restored. NOTE : If the drawing is closed with the dictionary erased, then the dictionary is deleted from the drawing and cannot be restored. |

## See Also

[IAttributeInstance Interface](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance.html)
[IAttributeInstance Members](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance_members.html)
[IAttributeInstance::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance~GetExtensionDictionary.html)

## Availability

DraftSight V1R4.0
