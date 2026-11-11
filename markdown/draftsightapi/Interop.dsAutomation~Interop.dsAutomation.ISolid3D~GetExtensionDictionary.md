---
title: "GetExtensionDictionary Method (ISolid3D)"
project: ""
interface: "ISolid3D"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISolid3D~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (ISolid3D)

Gets the dictionary for this 3D solid.

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

If the dictionary does not exist or it was erased by either [ISolid3D::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.ISolid3D~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[ISolid3D Interface](Interop.dsAutomation~Interop.dsAutomation.ISolid3D.html)
[ISolid3D Members](Interop.dsAutomation~Interop.dsAutomation.ISolid3D_members.html)
[ISolid3D::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.ISolid3D~CreateExtensionDictionary.html)

## Availability

DraftSight 2020 SP0
