---
title: "CreateExtensionDictionary Method (IPolyLine)"
project: ""
interface: "IPolyLine"
member: "CreateExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyLine~CreateExtensionDictionary.html"
---

# CreateExtensionDictionary Method (IPolyLine)

Creates a dictionary for the 2D PolyLine.

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
| Already exists for the 2D PolyLine | Not overwritten; instead, the existing dictionary is returned. |
| Was erased by either IPolyLine::ReleaseExtensionDictionary or IDictionary::Erased | Restored. NOTE : If the drawing is closed with the dictionary erased, then the dictionary is deleted from the drawing and cannot be restored. |

## See Also

[IPolyLine Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine.html)
[IPolyLine Members](Interop.dsAutomation~Interop.dsAutomation.IPolyLine_members.html)
[IPolyLine::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetExtensionDictionary.html)

## Availability

DraftSight V1R4.0
