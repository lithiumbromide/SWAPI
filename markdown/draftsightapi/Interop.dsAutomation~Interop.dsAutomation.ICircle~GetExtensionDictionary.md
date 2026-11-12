---
title: "GetExtensionDictionary Method (ICircle)"
project: ""
interface: "ICircle"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICircle~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (ICircle)

Gets the dictionary for the Circle.

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

If the dictionary does not exist or it was erased by either [ICircle::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.ICircle~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[ICircle Interface](Interop.dsAutomation~Interop.dsAutomation.ICircle.html)
[ICircle Members](Interop.dsAutomation~Interop.dsAutomation.ICircle_members.html)
[ICircle::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.ICircle~CreateExtensionDictionary.html)

## Availability

DraftSight V1R4.0
