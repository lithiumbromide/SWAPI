---
title: "CreateExtensionDictionary Method (IEllipseArc)"
project: ""
interface: "IEllipseArc"
member: "CreateExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IEllipseArc~CreateExtensionDictionary.html"
---

# CreateExtensionDictionary Method (IEllipseArc)

Creates a dictionary for the Ellipse or elliptical Arc.

## Syntax

### Visual Basic

```vb
Function CreateExtensionDictionary() As Dictionary
```

### C#

```csharp
Dictionary CreateExtensionDictionary()
```

### JScript

```
function CreateExtensionDictionary() : Dictionary;
```

### Managed Extensions for C++

```
Dictionary* CreateExtensionDictionary();
```

### C++/CLI

```cpp
Dictionary^ CreateExtensionDictionary();
```

### Return Value

[Dictionary](Interop.dsAutomation~Interop.dsAutomation.IDictionary.html)

## Remarks

| If the dictionary... | Then the dictionary is... |
| --- | --- |
| Already exists for the Ellipse or elliptical Arc | Not overwritten; instead, the existing dictionary is returned. |
| Was erased by either IEllipseArc::ReleaseExtensionDictionary or IDictionary::Erased | Restored. NOTE : If the drawing is closed with the dictionary erased, then the dictionary is deleted from the drawing and cannot be restored. |

## See Also

[IEllipseArc Interface](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc.html)
[IEllipseArc Members](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc_members.html)
[IEllipseArc::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc~GetExtensionDictionary.html)

## Availability

DraftSight V1R4.0
