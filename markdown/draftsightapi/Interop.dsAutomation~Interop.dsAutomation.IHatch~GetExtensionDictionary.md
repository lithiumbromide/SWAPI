---
title: "GetExtensionDictionary Method (IHatch)"
project: ""
interface: "IHatch"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IHatch~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (IHatch)

Gets the dictionary for the Hatch.

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

If the dictionary does not exist or it was erased by either [IHatch::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.IHatch~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[IHatch Interface](Interop.dsAutomation~Interop.dsAutomation.IHatch.html)
[IHatch Members](Interop.dsAutomation~Interop.dsAutomation.IHatch_members.html)
[IHatch::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IHatch~CreateExtensionDictionary.html)

## Availability

DraftSight V1R4.0
