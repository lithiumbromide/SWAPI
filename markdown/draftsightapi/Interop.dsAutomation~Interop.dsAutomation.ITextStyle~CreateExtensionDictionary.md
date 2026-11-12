---
title: "CreateExtensionDictionary Method (ITextStyle)"
project: ""
interface: "ITextStyle"
member: "CreateExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITextStyle~CreateExtensionDictionary.html"
---

# CreateExtensionDictionary Method (ITextStyle)

Creates a dictionary for the TextStyle.

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
| Already exists for the TextStyle | Not overwritten; instead, the existing dictionary is returned. |
| Was erased by either ITextStyle::ReleaseExtensionDictionary or IDictionary::Erased | Restored. NOTE : If the drawing is closed with the dictionary erased, then the dictionary is deleted from the drawing and cannot be restored. |

## See Also

[ITextStyle Interface](Interop.dsAutomation~Interop.dsAutomation.ITextStyle.html)
[ITextStyle Members](Interop.dsAutomation~Interop.dsAutomation.ITextStyle_members.html)
[ITextStyle::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.ITextStyle~GetExtensionDictionary.html)

## Availability

DraftSight V1R4.0
