---
title: "GetExtensionDictionary Method (INote)"
project: ""
interface: "INote"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.INote~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (INote)

Gets the dictionary for the Note.

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

If the dictionary does not exist or it was erased by either [INote::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.INote~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[INote Interface](Interop.dsAutomation~Interop.dsAutomation.INote.html)
[INote Members](Interop.dsAutomation~Interop.dsAutomation.INote_members.html)
[INote::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.INote~CreateExtensionDictionary.html)

## Availability

DraftSight V1R4.0
