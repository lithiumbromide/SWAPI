---
title: "GetExtensionDictionary Method (IDictionary)"
project: ""
interface: "IDictionary"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDictionary~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (IDictionary)

Gets the extension dictionary for the dictionary.

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

If the extension dictionary does not exist or it was erased by either [IDictionary::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.IDictionary~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[IDictionary Interface](Interop.dsAutomation~Interop.dsAutomation.IDictionary.html)
[IDictionary Members](Interop.dsAutomation~Interop.dsAutomation.IDictionary_members.html)
[IDictionary::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~CreateExtensionDictionary.html)
[IDictionary::CreateDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~CreateDictionary.html)

## Availability

DraftSight V1R4.0
