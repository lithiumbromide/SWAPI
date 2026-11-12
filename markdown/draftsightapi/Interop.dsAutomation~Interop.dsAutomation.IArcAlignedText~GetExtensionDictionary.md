---
title: "GetExtensionDictionary Method (IArcAlignedText)"
project: ""
interface: "IArcAlignedText"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IArcAlignedText~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (IArcAlignedText)

Gets the dictionary for this curved text.

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

If the dictionary does not exist or it was erased by either [IArcAlignedText::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.IArcAlignedText~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[IArcAlignedText Interface](Interop.dsAutomation~Interop.dsAutomation.IArcAlignedText.html)
[IArcAlignedText Members](Interop.dsAutomation~Interop.dsAutomation.IArcAlignedText_members.html)
[IArcAlignedText::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IArcAlignedText~CreateExtensionDictionary.html)

## Availability

DraftSight 2018 SP2
