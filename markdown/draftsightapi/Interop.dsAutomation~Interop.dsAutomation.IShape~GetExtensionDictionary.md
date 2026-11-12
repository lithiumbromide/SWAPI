---
title: "GetExtensionDictionary Method (IShape)"
project: ""
interface: "IShape"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IShape~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (IShape)

Gets the dictionary for the shape.

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

If the dictionary does not exist or it was erased by either [IShape::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.IShape~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[IShape Interface](Interop.dsAutomation~Interop.dsAutomation.IShape.html)
[IShape Members](Interop.dsAutomation~Interop.dsAutomation.IShape_members.html)
[IShape::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IShape~CreateExtensionDictionary.html)

## Availability

DraftSight V1R4.0
