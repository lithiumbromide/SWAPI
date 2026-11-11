---
title: "GetExtensionDictionary Method (ICustomCoordinateSystem)"
project: ""
interface: "ICustomCoordinateSystem"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystem~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (ICustomCoordinateSystem)

Gets the dictionary for the custom coordinate system.

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

If the dictionary does not exist or it was erased by either [ICustomCoordinateSystem::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystem~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[ICustomCoordinateSystem Interface](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystem.html)
[ICustomCoordinateSystem Members](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystem_members.html)
[ICustomCoordinateSystem::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystem~CreateExtensionDictionary.html)

## Availability

DraftSight V1R4.0
