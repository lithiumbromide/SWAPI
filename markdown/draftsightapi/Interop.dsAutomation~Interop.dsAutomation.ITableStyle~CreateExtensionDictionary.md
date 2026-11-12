---
title: "CreateExtensionDictionary Method (ITableStyle)"
project: ""
interface: "ITableStyle"
member: "CreateExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITableStyle~CreateExtensionDictionary.html"
---

# CreateExtensionDictionary Method (ITableStyle)

Creates a dictionary for the TableStyle.

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
| Already exists for the TableStyle | Not overwritten; instead, the existing dictionary is returned. |
| Was erased by either ITableStyle::ReleaseExtensionDictionary or IDictionary::Erased | Restored. NOTE : If the drawing is closed with the dictionary erased, then the dictionary is deleted from the drawing and cannot be restored. |

## See Also

[ITableStyle Interface](Interop.dsAutomation~Interop.dsAutomation.ITableStyle.html)
[ITableStyle Members](Interop.dsAutomation~Interop.dsAutomation.ITableStyle_members.html)
[ITableStyle::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~GetExtensionDictionary.html)

## Availability

DraftSight V1R4.0
