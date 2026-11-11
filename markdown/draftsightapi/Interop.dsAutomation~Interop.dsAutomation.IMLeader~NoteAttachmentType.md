---
title: "NoteAttachmentType Property (IMLeader)"
project: ""
interface: "IMLeader"
member: "NoteAttachmentType"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMLeader~NoteAttachmentType.html"
---

# NoteAttachmentType Property (IMLeader)

Gets or sets the Note attachment type of this MLeader.

## Syntax

### Visual Basic

```vb
Property NoteAttachmentType As dsMLeaderAttachmentType_e
```

### C#

```csharp
dsMLeaderAttachmentType_e NoteAttachmentType {get; set;}
```

### JScript

```
function get,set NoteAttachmentType : dsMLeaderAttachmentType_e
```

### Managed Extensions for C++

```
__property dsMLeaderAttachmentType_e get_NoteAttachmentType();
__property void set_NoteAttachmentType(
   dsMLeaderAttachmentType_e value
);
```

### C++/CLI

```cpp
property dsMLeaderAttachmentType_e NoteAttachmentType {
   dsMLeaderAttachmentType_e get();
   void set (    dsMLeaderAttachmentType_e value);
}
```

### Property Value

Note attachment type as defined by [dsMLeaderAttachmentType_e](Interop.dsAutomation~Interop.dsAutomation.dsMLeaderAttachmentType_e.html)

## Remarks

This property is valid only if this MLeader was created with Note content, [ISketchManager::InsertMLeaderWithNoteContentType](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertMLeaderWithNoteContentType.html) ([dsMLeaderContentType_e](Interop.dsAutomation~Interop.dsAutomation.dsMLeaderContentType_e.html).dsMLeaderContentType_Note).

## See Also

[IMLeader Interface](Interop.dsAutomation~Interop.dsAutomation.IMLeader.html)
[IMLeader Members](Interop.dsAutomation~Interop.dsAutomation.IMLeader_members.html)

## Availability

DraftSight 2024 SP4
