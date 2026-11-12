---
title: "CreateExtensionDictionary Method (ICustomCoordinateSystem)"
project: ""
interface: "ICustomCoordinateSystem"
member: "CreateExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystem~CreateExtensionDictionary.html"
---

# CreateExtensionDictionary Method (ICustomCoordinateSystem)

Creates a dictionary for the custom coordinate system.

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
| Already exists for the custom coordinate system | Not overwritten; instead, the existing dictionary is returned. |
| Was erased by either ICustomCoordinateSystem::ReleaseExtensionDictionary or IDictionary::Erased | Restored. NOTE : If the drawing is closed with the dictionary erased, then the dictionary is deleted from the drawing and cannot be restored. |

## See Also

[ICustomCoordinateSystem Interface](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystem.html)
[ICustomCoordinateSystem Members](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystem_members.html)
[ICustomCoordinateSystem::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystem~GetExtensionDictionary.html)

## Availability

DraftSight V1R4.0
