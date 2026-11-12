---
title: "GetExtensionDictionary Method (IPolyLine3D)"
project: ""
interface: "IPolyLine3D"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (IPolyLine3D)

Gets the dictionary for the 3D PolyLine.

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

If the dictionary does not exist or it was erased by either [IPolyLine3D::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[IPolyLine3D Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D.html)
[IPolyLine3D Members](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D_members.html)
[IPolyLine3D::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~CreateExtensionDictionary.html)

## Availability

DraftSight V1R4.0
