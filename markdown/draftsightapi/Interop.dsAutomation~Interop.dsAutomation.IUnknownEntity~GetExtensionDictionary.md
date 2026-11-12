---
title: "GetExtensionDictionary Method (IUnknownEntity)"
project: ""
interface: "IUnknownEntity"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IUnknownEntity~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (IUnknownEntity)

Gets the dictionary for the unknown entity.

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

If the dictionary does not exist or it was erased by either [IUnknownEntity::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.IUnknownEntity~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[IUnknownEntity Interface](Interop.dsAutomation~Interop.dsAutomation.IUnknownEntity.html)
[IUnknownEntity Members](Interop.dsAutomation~Interop.dsAutomation.IUnknownEntity_members.html)
[IUnknownEntity::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IUnknownEntity~CreateExtensionDictionary.html)

## Availability

DraftSight 2018 SP2
