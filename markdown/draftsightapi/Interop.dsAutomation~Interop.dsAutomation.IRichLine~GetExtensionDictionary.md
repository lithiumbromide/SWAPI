---
title: "GetExtensionDictionary Method (IRichLine)"
project: ""
interface: "IRichLine"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRichLine~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (IRichLine)

Gets the dictionary for the RichLine.

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

If the dictionary does not exist or it was erased by either [IRichLine::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.IRichLine~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[IRichLine Interface](Interop.dsAutomation~Interop.dsAutomation.IRichLine.html)
[IRichLine Members](Interop.dsAutomation~Interop.dsAutomation.IRichLine_members.html)
[IRichLine::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IRichLine~CreateExtensionDictionary.html)

## Availability

DraftSight V1R4.0
