---
title: "GetExtensionDictionary Method (IDgnReference)"
project: ""
interface: "IDgnReference"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDgnReference~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (IDgnReference)

Gets the dictionary for the DGN reference.

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

If the dictionary does not exist or it was erased by either [IDgnReference::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.IDgnReference~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[IDgnReference Interface](Interop.dsAutomation~Interop.dsAutomation.IDgnReference.html)
[IDgnReference Members](Interop.dsAutomation~Interop.dsAutomation.IDgnReference_members.html)
[IDgnReference::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IDgnReference~CreateExtensionDictionary.html)

## Availability

DraftSight 2020 SP0
