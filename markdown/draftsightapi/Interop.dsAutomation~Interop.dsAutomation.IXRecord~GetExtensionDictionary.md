---
title: "GetExtensionDictionary Method (IXRecord)"
project: ""
interface: "IXRecord"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (IXRecord)

Gets the dictionary for the XRecord.

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

If the dictionary does not exist or it was erased by either [IXRecord::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.IXRecord~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[IXRecord Interface](Interop.dsAutomation~Interop.dsAutomation.IXRecord.html)
[IXRecord Members](Interop.dsAutomation~Interop.dsAutomation.IXRecord_members.html)
[IXRecord::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~CreateExtensionDictionary.html)

## Availability

DraftSight V1R4.0
