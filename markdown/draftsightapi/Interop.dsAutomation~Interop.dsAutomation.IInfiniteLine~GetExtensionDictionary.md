---
title: "GetExtensionDictionary Method (IInfiniteLine)"
project: ""
interface: "IInfiniteLine"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (IInfiniteLine)

Gets the dictionary for the InfiniteLine.

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

If the dictionary does not exist or it was erased by either [IInfiniteLine::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[IInfiniteLine Interface](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine.html)
[IInfiniteLine Members](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine_members.html)
[IInfiniteLine::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine~CreateExtensionDictionary.html)

## Availability

DraftSight V1R4.0
