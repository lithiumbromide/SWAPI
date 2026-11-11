---
title: "CreateExtensionDictionary Method (IBlockDefinition)"
project: ""
interface: "IBlockDefinition"
member: "CreateExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition~CreateExtensionDictionary.html"
---

# CreateExtensionDictionary Method (IBlockDefinition)

Creates a dictionary for the Block definition.

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
| Already exists for the Block definition | Not overwritten; instead, the existing dictionary is returned. |
| Was erased by either IBlockDefinition::ReleaseExtensionDictionary or IDictionary::Erased | Restored. NOTE : If the drawing is closed with the dictionary erased, then the dictionary is deleted from the drawing and cannot be restored. |

## See Also

[IBlockDefinition Interface](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition.html)
[IBlockDefinition Members](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition_members.html)
[IBlockDefinition::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition~GetExtensionDictionary.html)

## Availability

DraftSight V1R4.0
