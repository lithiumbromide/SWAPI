---
title: "GetExtensionDictionary Method (IAttributeInstance)"
project: ""
interface: "IAttributeInstance"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (IAttributeInstance)

Gets the dictionary for the BlockAttribute instance.

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

If the dictionary does not exist or it was erased by either [IAttributeInstance::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[IAttributeInstance Interface](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance.html)
[IAttributeInstance Members](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance_members.html)
[IAttributeInstance::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance~CreateExtensionDictionary.html)

## Availability

DraftSight V1R4.0
