---
title: "GetExtensionDictionary Method (ISweptSurface)"
project: ""
interface: "ISweptSurface"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISweptSurface~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (ISweptSurface)

Gets the dictionary for this swept surface.

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

If the dictionary does not exist or it was erased by either [ISweptSurface::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.ISweptSurface~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[ISweptSurface Interface](Interop.dsAutomation~Interop.dsAutomation.ISweptSurface.html)
[ISweptSurface Members](Interop.dsAutomation~Interop.dsAutomation.ISweptSurface_members.html)
[ISweptSurface::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.ISweptSurface~CreateExtensionDictionary.html)

## Availability

DraftSight 2020 SP0
