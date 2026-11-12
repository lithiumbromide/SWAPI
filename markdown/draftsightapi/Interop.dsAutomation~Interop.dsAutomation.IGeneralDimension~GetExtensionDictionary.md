---
title: "GetExtensionDictionary Method (IGeneralDimension)"
project: ""
interface: "IGeneralDimension"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (IGeneralDimension)

Gets the dictionary for the Dimension.

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

If the dictionary does not exist or it was erased by either [IGeneralDimension::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[IGeneralDimension Interface](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension.html)
[IGeneralDimension Members](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension_members.html)
[IGeneralDimension::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension~CreateExtensionDictionary.html)

## Availability

DraftSight V1R4.0
