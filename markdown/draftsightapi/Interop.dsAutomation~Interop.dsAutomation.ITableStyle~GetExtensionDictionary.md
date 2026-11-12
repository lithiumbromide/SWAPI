---
title: "GetExtensionDictionary Method (ITableStyle)"
project: ""
interface: "ITableStyle"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITableStyle~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (ITableStyle)

Gets the dictionary for the TableStyle.

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

If the dictionary does not exist or it was erased by either [ITableStyle::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[ITableStyle Interface](Interop.dsAutomation~Interop.dsAutomation.ITableStyle.html)
[ITableStyle Members](Interop.dsAutomation~Interop.dsAutomation.ITableStyle_members.html)
[ITableStyle::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~CreateExtensionDictionary.html)

## Availability

DraftSight V1R4.0
