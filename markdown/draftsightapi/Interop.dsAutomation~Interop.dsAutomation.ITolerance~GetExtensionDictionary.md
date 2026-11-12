---
title: "GetExtensionDictionary Method (ITolerance)"
project: ""
interface: "ITolerance"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITolerance~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (ITolerance)

Gets the dictionary for the geometric Tolerance.

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

If the dictionary does not exist or it was erased by either [ITolerance::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.ITolerance~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[ITolerance Interface](Interop.dsAutomation~Interop.dsAutomation.ITolerance.html)
[ITolerance Members](Interop.dsAutomation~Interop.dsAutomation.ITolerance_members.html)
[ITolerance::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.ITolerance~CreateExtensionDictionary.html)

## Availability

DaftSight V1R4.0
