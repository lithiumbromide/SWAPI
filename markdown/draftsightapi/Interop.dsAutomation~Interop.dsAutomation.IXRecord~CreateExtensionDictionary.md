---
title: "CreateExtensionDictionary Method (IXRecord)"
project: ""
interface: "IXRecord"
member: "CreateExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IXRecord~CreateExtensionDictionary.html"
---

# CreateExtensionDictionary Method (IXRecord)

Creates a dictionary for the XRecord.

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
| Already exists for the XRecord | Not overwritten; instead, the existing dictionary is returned. |
| Was erased by either IXRecord::ReleaseExtensionDictionary or IDictionary::Erased | Restored. NOTE : If the drawing is closed with the extension dictionary erased, then the extension dictionary is deleted from the drawing and cannot be restored. |

## See Also

[IXRecord Interface](Interop.dsAutomation~Interop.dsAutomation.IXRecord.html)
[IXRecord Members](Interop.dsAutomation~Interop.dsAutomation.IXRecord_members.html)
[IXRecord::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetExtensionDictionary.html)

## Availability

DraftSight V1R4.0
