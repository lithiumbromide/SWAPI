---
title: "GetExtensionDictionary Method (IGroup)"
project: ""
interface: "IGroup"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IGroup~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (IGroup)

Gets the dictionary for the EntityGroup.

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

If the dictionary does not exist or it was erased by either [IGroup::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.IGroup~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[IGroup Interface](Interop.dsAutomation~Interop.dsAutomation.IGroup.html)
[IGroup Members](Interop.dsAutomation~Interop.dsAutomation.IGroup_members.html)
[IGroup::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IGroup~CreateExtensionDictionary.html)

## Availability

DraftSight V1R4.0
