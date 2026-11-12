---
title: "GetExtensionDictionary Method (IPolyLine)"
project: ""
interface: "IPolyLine"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (IPolyLine)

Gets the dictionary for the 2D PolyLine.

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

If the dictionary does not exist or it was erased by either [IPolyLine::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[IPolyLine Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine.html)
[IPolyLine Members](Interop.dsAutomation~Interop.dsAutomation.IPolyLine_members.html)
[IPolyLine::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~CreateExtensionDictionary.html)

## Availability

DraftSight V1R4.0
