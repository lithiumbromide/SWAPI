---
title: "CreateExtensionDictionary Method (IReferenceImage)"
project: ""
interface: "IReferenceImage"
member: "CreateExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IReferenceImage~CreateExtensionDictionary.html"
---

# CreateExtensionDictionary Method (IReferenceImage)

Creates a dictionary for the Referenced image.

## Syntax

### Visual Basic

```vb
Function CreateExtensionDictionary() As Dictionary
```

### C#

```csharp
Dictionary CreateExtensionDictionary()
```

### JScript

```
function CreateExtensionDictionary() : Dictionary;
```

### Managed Extensions for C++

```
Dictionary* CreateExtensionDictionary();
```

### C++/CLI

```cpp
Dictionary^ CreateExtensionDictionary();
```

### Return Value

[Dictionary](Interop.dsAutomation~Interop.dsAutomation.IDictionary.html)

## Remarks

| If the dictionary... | Then the dictionary is... |
| --- | --- |
| Already exists for the Referenced image | Not overwritten; instead, the existing dictionary is returned. |
| Was erased by either IReferenceImage::ReleaseExtensionDictionary or IDictionary::Erased | Restored. NOTE : If the drawing is closed with the dictionary erased, then the dictionary is deleted from the drawing and cannot be restored. |

## See Also

[IReferenceImage Interface](Interop.dsAutomation~Interop.dsAutomation.IReferenceImage.html)
[IReferenceImage Members](Interop.dsAutomation~Interop.dsAutomation.IReferenceImage_members.html)
[IReferenceImage::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IReferenceImage~GetExtensionDictionary.html)

## Availability

DraftSight V1R4.0
