---
title: "GetExtensionDictionary Method (IBlockInstance)"
project: ""
interface: "IBlockInstance"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IBlockInstance~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (IBlockInstance)

Gets the dictionary for the Block instance.

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

If the dictionary does not exist or it was erased by either [IBlockInstance::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[IBlockInstance Interface](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance.html)
[IBlockInstance Members](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance_members.html)
[IBlockInstance::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance~CreateExtensionDictionary.html)

## Availability

DraftSight V1R4.0
