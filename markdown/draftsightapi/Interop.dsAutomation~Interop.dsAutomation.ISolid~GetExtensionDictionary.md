---
title: "GetExtensionDictionary Method (ISolid)"
project: ""
interface: "ISolid"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISolid~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (ISolid)

Gets the dictionary for the 2D Solid.

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

If the dictionary does not exist or it was erased by either [ISolid::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.ISolid~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[ISolid Interface](Interop.dsAutomation~Interop.dsAutomation.ISolid.html)
[ISolid Members](Interop.dsAutomation~Interop.dsAutomation.ISolid_members.html)
[ISolid::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.ISolid~CreateExtensionDictionary.html)

## Availability

DraftSight V1R4.0
