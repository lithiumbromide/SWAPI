---
title: "CreateExtensionDictionary Method (ILineStyle)"
project: ""
interface: "ILineStyle"
member: "CreateExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILineStyle~CreateExtensionDictionary.html"
---

# CreateExtensionDictionary Method (ILineStyle)

Creates a dictionary for the LineStyle.

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
| Already exists for the LineStyle | Not overwritten; instead, the existing dictionary is returned. |
| Was erased by either ILineStyle::ReleaseExtensionDictionary or IDictionary::Erased | Restored. NOTE : If the drawing is closed with the dictionary erased, then the dictionary is deleted from the drawing and cannot be restored. |

## See Also

[ILineStyle Interface](Interop.dsAutomation~Interop.dsAutomation.ILineStyle.html)
[ILineStyle Members](Interop.dsAutomation~Interop.dsAutomation.ILineStyle_members.html)
[ILineStyle::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.ILineStyle~GetExtensionDictionary.html)

## Availability

DraftSight V1R4.0
