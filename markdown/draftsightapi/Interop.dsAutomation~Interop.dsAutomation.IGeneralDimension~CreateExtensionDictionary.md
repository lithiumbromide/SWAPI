---
title: "CreateExtensionDictionary Method (IGeneralDimension)"
project: ""
interface: "IGeneralDimension"
member: "CreateExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension~CreateExtensionDictionary.html"
---

# CreateExtensionDictionary Method (IGeneralDimension)

Creates a dictionary for the Dimension.

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
| Already exists for the Dimension | Not overwritten; instead, the existing dictionary is returned. |
| Was erased by either IGeneralDimension::ReleaseExtensionDictionary or IDictionary::Erased | Restored. NOTE : If the drawing is closed with the dictionary erased, then the dictionary is deleted from the drawing and cannot be restored. |

## See Also

[IGeneralDimension Interface](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension.html)
[IGeneralDimension Members](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension_members.html)
[IGeneralDimension::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension~GetExtensionDictionary.html)

## Availability

DraftSight V1R4.0
