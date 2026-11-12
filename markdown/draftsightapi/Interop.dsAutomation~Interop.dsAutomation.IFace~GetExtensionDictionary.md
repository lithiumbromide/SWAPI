---
title: "GetExtensionDictionary Method (IFace)"
project: ""
interface: "IFace"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IFace~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (IFace)

Gets the dictionary for the Face.

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

If the dictionary does not exist or it was erased by either [IFace::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.IFace~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[IFace Interface](Interop.dsAutomation~Interop.dsAutomation.IFace.html)
[IFace Members](Interop.dsAutomation~Interop.dsAutomation.IFace_members.html)
[IFace::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IFace~CreateExtensionDictionary.html)

## Availability

DraftSight V1R4.0
