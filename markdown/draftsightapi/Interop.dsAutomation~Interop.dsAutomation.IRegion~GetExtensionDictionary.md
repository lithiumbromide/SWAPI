---
title: "GetExtensionDictionary Method (IRegion)"
project: ""
interface: "IRegion"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRegion~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (IRegion)

Gets the dictionary for the Region.

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

If the dictionary does not exist or it was erased by either [IRegion::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.IRegion~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[IRegion Interface](Interop.dsAutomation~Interop.dsAutomation.IRegion.html)
[IRegion Members](Interop.dsAutomation~Interop.dsAutomation.IRegion_members.html)
[IRegion::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IRegion~CreateExtensionDictionary.html)

## Availability

DraftSight V1R4.0
