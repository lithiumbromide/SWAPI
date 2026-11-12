---
title: "GetExtensionDictionary Method (ILine)"
project: ""
interface: "ILine"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILine~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (ILine)

Gets the dictionary for the Line.

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

If the dictionary does not exist or it was erased by either [ILine::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.ILine~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[ILine Interface](Interop.dsAutomation~Interop.dsAutomation.ILine.html)
[ILine Members](Interop.dsAutomation~Interop.dsAutomation.ILine_members.html)
[ILine::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.ILine~CreateExtensionDictionary.html)

## Availability

DraftSight V1R4.0
