---
title: "GetExtensionDictionary Method (IAttributeDefinition)"
project: ""
interface: "IAttributeDefinition"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (IAttributeDefinition)

Gets the dictionary for the BlockAttribute definition.

## Syntax

### Visual Basic

```vb
Function GetExtensionDictionary() As Dictionary
```

### C#

```csharp
Dictionary GetExtensionDictionary()
```

### JScript

```
function GetExtensionDictionary() : Dictionary;
```

### Managed Extensions for C++

```
Dictionary* GetExtensionDictionary();
```

### C++/CLI

```cpp
Dictionary^ GetExtensionDictionary();
```

### Return Value

[Dictionary](Interop.dsAutomation~Interop.dsAutomation.IDictionary.html)

## Remarks

If the dictionary does not exist or it was erased by either [IAttributeDefinition::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[IAttributeDefinition Interface](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition.html)
[IAttributeDefinition Members](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition_members.html)
[IAttributeDefinition::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition~CreateExtensionDictionary.html)

## Availability

DraftSight V1R4.0
