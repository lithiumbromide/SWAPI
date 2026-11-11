---
title: "GetExtensionDictionary Method (ISpline)"
project: ""
interface: "ISpline"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISpline~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (ISpline)

Gets the dictionary for the Spline.

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

If the dictionary does not exist or it was erased by either [ISpline::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.ISpline~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[ISpline Interface](Interop.dsAutomation~Interop.dsAutomation.ISpline.html)
[ISpline Members](Interop.dsAutomation~Interop.dsAutomation.ISpline_members.html)
[ISpline::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.ISpline~CreateExtensionDictionary.html)

## Availability

DraftSight V1R4.0
