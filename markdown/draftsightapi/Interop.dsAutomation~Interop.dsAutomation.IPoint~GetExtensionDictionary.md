---
title: "GetExtensionDictionary Method (IPoint)"
project: ""
interface: "IPoint"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPoint~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (IPoint)

Gets the dictionary for the Point.

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

If the dictionary does not exist or it was erased by either [IPoint::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.IPoint~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[IPoint Interface](Interop.dsAutomation~Interop.dsAutomation.IPoint.html)
[IPoint Members](Interop.dsAutomation~Interop.dsAutomation.IPoint_members.html)
[IPoint::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IPoint~CreateExtensionDictionary.html)

## Availability

DraftSight V1R4.0
