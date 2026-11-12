---
title: "GetExtensionDictionary Method (IExternalReference)"
project: ""
interface: "IExternalReference"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IExternalReference~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (IExternalReference)

Gets the dictionary for the external reference.

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

If the dictionary does not exist or it was erased by either [IExternalReference::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.IExternalReference~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[IExternalReference Interface](Interop.dsAutomation~Interop.dsAutomation.IExternalReference.html)
[IExternalReference Members](Interop.dsAutomation~Interop.dsAutomation.IExternalReference_members.html)
[IExternalReference::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IExternalReference~CreateExtensionDictionary.html)

## Availability

DraftSight V1R4.0
