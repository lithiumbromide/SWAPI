---
title: "GetExtensionDictionary Method (IBlockDefinition)"
project: ""
interface: "IBlockDefinition"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (IBlockDefinition)

Gets the dictionary for the Block definition.

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

If the dictionary does not exist or it was erased by either [IBlockDefinition::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[IBlockDefinition Interface](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition.html)
[IBlockDefinition Members](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition_members.html)
[IBlockDefinition::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition~CreateExtensionDictionary.html)

## Availability

DraftSight V1R4.0
