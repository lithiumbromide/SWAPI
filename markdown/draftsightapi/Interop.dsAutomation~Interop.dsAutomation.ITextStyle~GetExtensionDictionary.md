---
title: "GetExtensionDictionary Method (ITextStyle)"
project: ""
interface: "ITextStyle"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITextStyle~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (ITextStyle)

Gets the dictionary for the TextStyle.

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

If the dictionary does not exist or it was erased by either [ITextStyle::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.ITextStyle~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[ITextStyle Interface](Interop.dsAutomation~Interop.dsAutomation.ITextStyle.html)
[ITextStyle Members](Interop.dsAutomation~Interop.dsAutomation.ITextStyle_members.html)
[ITextStyle::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.ITextStyle~CreateExtensionDictionary.html)

## Availability

DraftSight V1R4.0
