---
title: "GetExtensionDictionary Method (ILoft)"
project: ""
interface: "ILoft"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILoft~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (ILoft)

Gets the dictionary for this Loft.

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

If the dictionary does not exist or it was erased by either [IEllipseArc::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[ILoft Interface](Interop.dsAutomation~Interop.dsAutomation.ILoft.html)
[ILoft Members](Interop.dsAutomation~Interop.dsAutomation.ILoft_members.html)
[ILoft::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.ILoft~CreateExtensionDictionary.html)

## Availability

DraftSight 2020 SP0
