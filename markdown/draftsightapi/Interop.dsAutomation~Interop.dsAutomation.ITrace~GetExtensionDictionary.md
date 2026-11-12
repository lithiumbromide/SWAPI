---
title: "GetExtensionDictionary Method (ITrace)"
project: ""
interface: "ITrace"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITrace~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (ITrace)

Gets the dictionary for the Trace.

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

If the dictionary does not exist or it was erased by either [ITrace::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.ITrace~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[ITrace Interface](Interop.dsAutomation~Interop.dsAutomation.ITrace.html)
[ITrace Members](Interop.dsAutomation~Interop.dsAutomation.ITrace_members.html)
[ITrace::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.ITrace~CreateExtensionDictionary.html)

## Availability

DraftSight V1R5.0
