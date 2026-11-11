---
title: "CreateExtensionDictionary Method (IDimensionStyle)"
project: ""
interface: "IDimensionStyle"
member: "CreateExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle~CreateExtensionDictionary.html"
---

# CreateExtensionDictionary Method (IDimensionStyle)

Creates a dictionary for the DimensionStyle.

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
| Already exists for the DimensionStyle | Not overwritten; instead, the existing dictionary is returned. |
| Was erased by either IDimensionStyle::ReleaseExtensionDictionary or IDictionary::Erased | Restored. NOTE : If the drawing is closed with the dictionary erased, then the dictionary is deleted from the drawing and cannot be restored. |

## See Also

[IDimensionStyle Interface](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle.html)
[IDimensionStyle Members](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle_members.html)
[IDimensionStyle::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle~GetExtensionDictionary.html)

## Availability

DraftSight V1R4.0
