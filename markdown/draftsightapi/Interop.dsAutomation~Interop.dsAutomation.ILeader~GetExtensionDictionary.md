---
title: "GetExtensionDictionary Method (ILeader)"
project: ""
interface: "ILeader"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILeader~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (ILeader)

Gets the dictionary for the Leader.

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

If the dictionary does not exist or it was erased by either [ILeader::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.ILeader~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[ILeader Interface](Interop.dsAutomation~Interop.dsAutomation.ILeader.html)
[ILeader Members](Interop.dsAutomation~Interop.dsAutomation.ILeader_members.html)
[ILeader::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.ILeader~CreateExtensionDictionary.html)

## Availability

DraftSight V1R4.0
