---
title: "GetNote Method (IMLeader)"
project: ""
interface: "IMLeader"
member: "GetNote"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMLeader~GetNote.html"
---

# GetNote Method (IMLeader)

Gets the Note for this MLeader.

## Syntax

### Visual Basic

```vb
Function GetNote() As Note
```

### C#

```csharp
Note GetNote()
```

### JScript

```
function GetNote() : Note;
```

### Managed Extensions for C++

```
Note* GetNote();
```

### C++/CLI

```cpp
Note^ GetNote();
```

### Return Value

[INote](Interop.dsAutomation~Interop.dsAutomation.INote.html)

## Remarks

This property is valid only if this MLeader was created with Note content, [ISketchManager::InsertMLeaderWithNoteContentType](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertMLeaderWithNoteContentType.html) ([dsMLeaderContentType_e](Interop.dsAutomation~Interop.dsAutomation.dsMLeaderContentType_e.html).dsMLeaderContentType_Note).

## See Also

[IMLeader Interface](Interop.dsAutomation~Interop.dsAutomation.IMLeader.html)
[IMLeader Members](Interop.dsAutomation~Interop.dsAutomation.IMLeader_members.html)

## Availability

DraftSight 2024 SP4
