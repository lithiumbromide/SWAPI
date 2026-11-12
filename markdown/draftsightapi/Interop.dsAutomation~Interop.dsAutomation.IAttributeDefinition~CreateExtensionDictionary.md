---
title: "CreateExtensionDictionary Method (IAttributeDefinition)"
project: ""
interface: "IAttributeDefinition"
member: "CreateExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition~CreateExtensionDictionary.html"
---

# CreateExtensionDictionary Method (IAttributeDefinition)

Creates a dictionary for the BlockAttribute definition.

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
| Already exists for the BlockAttribute definition | Not overwritten; instead, the existing dictionary is returned. |
| Was erased by either IAttributeDefinition::ReleaseExtensionDictionary or IDictionary::Erased | Restored. NOTE : If the drawing is closed with the extension dictionary erased, then the extension dictionary is deleted from the drawing. |

## See Also

[IAttributeDefinition Interface](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition.html)
[IAttributeDefinition Members](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition_members.html)
[IAttributeDefinition::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition~GetExtensionDictionary.html)

## Availability

DraftSight V1R4.0
