---
title: "GetExtensionDictionary Method (IDimensionStyle)"
project: ""
interface: "IDimensionStyle"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (IDimensionStyle)

Gets the dictionary for the DimensionStyle.

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

If the dictionary does not exist or it was erased by either [IDimensionStyle::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[IDimensionStyle Interface](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle.html)
[IDimensionStyle Members](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle_members.html)
[IDimensionStyle::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle~CreateExtensionDictionary.html)

## Availability

DraftSight V1R4.0
