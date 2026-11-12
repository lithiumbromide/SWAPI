---
title: "GetExtensionDictionary Method (IRevolvedSurface)"
project: ""
interface: "IRevolvedSurface"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRevolvedSurface~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (IRevolvedSurface)

Gets the dictionary for this revolved surface.

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

[IRevolvedSurface Interface](Interop.dsAutomation~Interop.dsAutomation.IRevolvedSurface.html)
[IRevolvedSurface Members](Interop.dsAutomation~Interop.dsAutomation.IRevolvedSurface_members.html)
[IRevolvedSurface::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IRevolvedSurface~CreateExtensionDictionary.html)

## Availability

DraftSight 2020 SP0
