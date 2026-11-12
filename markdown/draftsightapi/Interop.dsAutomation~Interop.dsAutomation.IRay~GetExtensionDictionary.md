---
title: "GetExtensionDictionary Method (IRay)"
project: ""
interface: "IRay"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRay~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (IRay)

Gets the dictionary for the Ray.

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

If the dictionary does not exist or it was erased by either [IRay::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.IRay~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[IRay Interface](Interop.dsAutomation~Interop.dsAutomation.IRay.html)
[IRay Members](Interop.dsAutomation~Interop.dsAutomation.IRay_members.html)
[IRay::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IRay~CreateExtensionDictionary.html)

## Availability

DraftSight V1R4.0
