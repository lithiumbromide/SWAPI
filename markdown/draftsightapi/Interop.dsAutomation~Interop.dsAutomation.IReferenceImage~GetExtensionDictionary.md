---
title: "GetExtensionDictionary Method (IReferenceImage)"
project: ""
interface: "IReferenceImage"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IReferenceImage~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (IReferenceImage)

Gets the dictionary for the Referenced image.

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

If the dictionary does not exist or it was erased by either [IReferenceImage::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.IReferenceImage~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[IReferenceImage Interface](Interop.dsAutomation~Interop.dsAutomation.IReferenceImage.html)
[IReferenceImage Members](Interop.dsAutomation~Interop.dsAutomation.IReferenceImage_members.html)
[IReferenceImage::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IReferenceImage~CreateExtensionDictionary.html)

## Availability

DraftSight V1R4.0
