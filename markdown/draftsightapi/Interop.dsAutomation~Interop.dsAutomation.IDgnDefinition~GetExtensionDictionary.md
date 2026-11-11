---
title: "GetExtensionDictionary Method (IDgnDefinition)"
project: ""
interface: "IDgnDefinition"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDgnDefinition~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (IDgnDefinition)

Gets the dictionary for the DGN definition.

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

If the dictionary does not exist or it was erased by either [IDgnDefinition::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.IDgnDefinition~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[IDgnDefinition Interface](Interop.dsAutomation~Interop.dsAutomation.IDgnDefinition.html)
[IDgnDefinition Members](Interop.dsAutomation~Interop.dsAutomation.IDgnDefinition_members.html)
[IDgnDefinition::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IDgnDefinition~CreateExtensionDictionary.html)

## Availability

DraftSight 2020 SP0
