---
title: "SetNote Method (IMLeader)"
project: ""
interface: "IMLeader"
member: "SetNote"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMLeader~SetNote.html"
---

# SetNote Method (IMLeader)

Sets the Note for this MLeader.

## Syntax

### Visual Basic

```vb
Sub SetNote( _
   ByVal Text As Note _
)
```

### C#

```csharp
void SetNote(
   Note Text
)
```

### JScript

```
function SetNote(
   Text : Note
);
```

### Managed Extensions for C++

```
void SetNote(
   Note* Text
)
```

### C++/CLI

```cpp
void SetNote(
   Note^ Text
)
```

### Parameters

- `Text`: [INote](Interop.dsAutomation~Interop.dsAutomation.INote.html)

## Remarks

This property is valid only if this MLeader was created with Note content, [ISketchManager::InsertMLeaderWithNoteContentType](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertMLeaderWithNoteContentType.html) ([dsMLeaderContentType_e](Interop.dsAutomation~Interop.dsAutomation.dsMLeaderContentType_e.html).dsMLeaderContentType_Note).

## See Also

[IMLeader Interface](Interop.dsAutomation~Interop.dsAutomation.IMLeader.html)
[IMLeader Members](Interop.dsAutomation~Interop.dsAutomation.IMLeader_members.html)

## Availability

DraftSight 2024 SP4
