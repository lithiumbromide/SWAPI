---
title: "GetExtensionDictionary Method (ILoftedSurface)"
project: ""
interface: "ILoftedSurface"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILoftedSurface~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (ILoftedSurface)

Gets the dictionary for this lofted surface.

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

If the dictionary does not exist or it was erased by either [ILoft::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.ILoft~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[ILoftedSurface Interface](Interop.dsAutomation~Interop.dsAutomation.ILoftedSurface.html)
[ILoftedSurface Members](Interop.dsAutomation~Interop.dsAutomation.ILoftedSurface_members.html)
[ILoftedSurface::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.ILoftedSurface~CreateExtensionDictionary.html)

## Availability

DraftSight 2020 SP0
