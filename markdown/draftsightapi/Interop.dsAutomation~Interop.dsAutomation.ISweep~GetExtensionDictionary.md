---
title: "GetExtensionDictionary Method (ISweep)"
project: ""
interface: "ISweep"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISweep~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (ISweep)

Gets the dictionary for this Sweep.

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

If the dictionary does not exist or it was erased by either [ISweep::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.ISweep~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[ISweep Interface](Interop.dsAutomation~Interop.dsAutomation.ISweep.html)
[ISweep Members](Interop.dsAutomation~Interop.dsAutomation.ISweep_members.html)
[ISweep::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.ISweep~CreateExtensionDictionary.html)

## Availability

DraftSight 2020 SP0
