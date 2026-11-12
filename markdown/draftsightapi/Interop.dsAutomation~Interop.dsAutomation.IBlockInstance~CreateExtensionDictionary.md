---
title: "CreateExtensionDictionary Method (IBlockInstance)"
project: ""
interface: "IBlockInstance"
member: "CreateExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IBlockInstance~CreateExtensionDictionary.html"
---

# CreateExtensionDictionary Method (IBlockInstance)

Creates a dictionary for the Block instance.

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
| Already exists for the Block instance | Not overwritten; instead, the existing dictionary is returned. |
| Was erased by either IBlockInstance::ReleaseExtensionDictionary or IDictionary::Erased | Is restored. NOTE : If the drawing is closed with the dictionary erased, then the dictionary is deleted from the drawing and cannot be restored. |

## See Also

[IBlockInstance Interface](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance.html)
[IBlockInstance Members](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance_members.html)
[IBlockInstance::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance~GetExtensionDictionary.html)

## Availability

DraftSight V1R4.0
