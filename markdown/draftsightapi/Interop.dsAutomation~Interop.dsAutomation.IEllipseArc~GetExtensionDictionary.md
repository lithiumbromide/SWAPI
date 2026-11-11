---
title: "GetExtensionDictionary Method (IEllipseArc)"
project: ""
interface: "IEllipseArc"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IEllipseArc~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (IEllipseArc)

Gets the dictionary for the Ellipse or elliptical Arc.

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

[IEllipseArc Interface](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc.html)
[IEllipseArc Members](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc_members.html)
[IEllipseArc::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc~CreateExtensionDictionary.html)

## Availability

DraftSight V1R4.0
