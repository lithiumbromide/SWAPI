---
title: "GetExtensionDictionary Method (ISimpleNote)"
project: ""
interface: "ISimpleNote"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISimpleNote~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (ISimpleNote)

Gets the dictionary for the SimpleNote.

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

If the dictionary does not exist or it was erased by either [ISimpleNote::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[ISimpleNote Interface](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote.html)
[ISimpleNote Members](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote_members.html)
[ISimpleNote::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote~CreateExtensionDictionary.html)

## Availability

DraftSight V1R4.0
