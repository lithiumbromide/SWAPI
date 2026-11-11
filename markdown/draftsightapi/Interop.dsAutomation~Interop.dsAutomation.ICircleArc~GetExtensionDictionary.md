---
title: "GetExtensionDictionary Method (ICircleArc)"
project: ""
interface: "ICircleArc"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICircleArc~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (ICircleArc)

Gets the dictionary for the Arc.

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

If the dictionary does not exist or it was erased by either [ICircleArc::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.ICircleArc~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[ICircleArc Interface](Interop.dsAutomation~Interop.dsAutomation.ICircleArc.html)
[ICircleArc Members](Interop.dsAutomation~Interop.dsAutomation.ICircleArc_members.html)
[IDictionary::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.ICircleArc~CreateExtensionDictionary.html)

## Availability

DraftSight V1R4.0
