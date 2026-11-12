---
title: "GetExtensionDictionary Method (ISheet)"
project: ""
interface: "ISheet"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISheet~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (ISheet)

Gets the dictionary for the Sheet.

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

If the dictionary does not exist or it was erased by either [ISheet::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.ISheet~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[ISheet Interface](Interop.dsAutomation~Interop.dsAutomation.ISheet.html)
[ISheet Members](Interop.dsAutomation~Interop.dsAutomation.ISheet_members.html)
[ISheet::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.ISheet~CreateExtensionDictionary.html)

## Availability

DraftSight V1R4.0
