---
title: "CreateExtensionDictionary Method (IRichLine)"
project: ""
interface: "IRichLine"
member: "CreateExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRichLine~CreateExtensionDictionary.html"
---

# CreateExtensionDictionary Method (IRichLine)

Creates a dictionary for the RichLine.

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
| Already exists for the RichLine | Not overwritten; instead, the existing dictionary is returned. |
| Was erased by either IRichLine::ReleaseExtensionDictionary or IDictionary::Erased | Restored. NOTE : If the drawing is closed with the dictionary erased, then the dictionary is deleted from the drawing and cannot be restored. |

## See Also

[IRichLine Interface](Interop.dsAutomation~Interop.dsAutomation.IRichLine.html)
[IRichLine Members](Interop.dsAutomation~Interop.dsAutomation.IRichLine_members.html)
[IRichLine::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IRichLine~GetExtensionDictionary.html)

## Availability

DraftSight V1R4.0
