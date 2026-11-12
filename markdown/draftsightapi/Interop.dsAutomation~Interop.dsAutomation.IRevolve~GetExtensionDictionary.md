---
title: "GetExtensionDictionary Method (IRevolve)"
project: ""
interface: "IRevolve"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRevolve~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (IRevolve)

Gets the dictionary for this Revolve.

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

If the dictionary does not exist or it was erased by either [IRevolve::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.IRevolve~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[IRevolve Interface](Interop.dsAutomation~Interop.dsAutomation.IRevolve.html)
[IRevolve Members](Interop.dsAutomation~Interop.dsAutomation.IRevolve_members.html)
[IRevolve::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IRevolve~CreateExtensionDictionary.html)

## Availability

DraftSight 2020 SP0
