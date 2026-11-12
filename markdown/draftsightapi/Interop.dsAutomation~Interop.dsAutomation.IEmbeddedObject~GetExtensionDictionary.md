---
title: "GetExtensionDictionary Method (IEmbeddedObject)"
project: ""
interface: "IEmbeddedObject"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IEmbeddedObject~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (IEmbeddedObject)

Gets the dictionary for the embedded object.

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

If the dictionary does not exist or it was erased by either [IEmbeddedObject::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.IEmbeddedObject~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[IEmbeddedObject Interface](Interop.dsAutomation~Interop.dsAutomation.IEmbeddedObject.html)
[IEmbeddedObject Members](Interop.dsAutomation~Interop.dsAutomation.IEmbeddedObject_members.html)
[IEmbeddedObject::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IEmbeddedObject~CreateExtensionDictionary.html)

## Availability

DraftSight V1R4.0
