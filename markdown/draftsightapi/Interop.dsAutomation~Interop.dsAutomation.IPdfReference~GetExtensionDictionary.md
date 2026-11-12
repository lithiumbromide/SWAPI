---
title: "GetExtensionDictionary Method (IPdfReference)"
project: ""
interface: "IPdfReference"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPdfReference~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (IPdfReference)

Gets the dictionary for the PDF reference.

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

If the dictionary does not exist or it was erased by either [IPdfReference::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.IPdfReference~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[IPdfReference Interface](Interop.dsAutomation~Interop.dsAutomation.IPdfReference.html)
[IPdfReference Members](Interop.dsAutomation~Interop.dsAutomation.IPdfReference_members.html)
[IPdfReference::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IPdfReference~CreateExtensionDictionary.html)

## Availability

DraftSight 2020 SP0
