---
title: "GetExtensionDictionary Method (IExtrusion)"
project: ""
interface: "IExtrusion"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IExtrusion~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (IExtrusion)

Gets the dictionary for this extrusion.

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

If the dictionary does not exist or it was erased by either [IExtrusion::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.IExtrusion~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[IExtrusion Interface](Interop.dsAutomation~Interop.dsAutomation.IExtrusion.html)
[IExtrusion Members](Interop.dsAutomation~Interop.dsAutomation.IExtrusion_members.html)
[IExtrusion::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IExtrusion~CreateExtensionDictionary.html)

## Availability

DraftSight 2020 SP0
