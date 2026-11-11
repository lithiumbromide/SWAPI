---
title: "GetExtensionDictionary Method (IExtrudedSurface)"
project: ""
interface: "IExtrudedSurface"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IExtrudedSurface~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (IExtrudedSurface)

Gets the dictionary for this extruded surface.

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

If the dictionary does not exist or it was erased by either [IExtrudedSurface::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.IExtrudedSurface~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[IExtrudedSurface Interface](Interop.dsAutomation~Interop.dsAutomation.IExtrudedSurface.html)
[IExtrudedSurface Members](Interop.dsAutomation~Interop.dsAutomation.IExtrudedSurface_members.html)
[IExtrudedSurface::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IExtrudedSurface~CreateExtensionDictionary.html)

## Availability

DraftSight 2020 SP0
