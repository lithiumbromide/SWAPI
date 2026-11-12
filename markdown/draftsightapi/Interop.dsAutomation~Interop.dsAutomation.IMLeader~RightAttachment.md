---
title: "RightAttachment Property (IMLeader)"
project: ""
interface: "IMLeader"
member: "RightAttachment"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMLeader~RightAttachment.html"
---

# RightAttachment Property (IMLeader)

Gets or sets the right attachment of the Note for this MLeader.

## Syntax

### Visual Basic

```vb
Property RightAttachment As dsMLeaderNoteAttachmentType_e
```

### C#

```csharp
dsMLeaderNoteAttachmentType_e RightAttachment {get; set;}
```

### JScript

```
function get,set RightAttachment : dsMLeaderNoteAttachmentType_e
```

### Managed Extensions for C++

```
__property dsMLeaderNoteAttachmentType_e get_RightAttachment();
__property void set_RightAttachment(
   dsMLeaderNoteAttachmentType_e value
);
```

### C++/CLI

```cpp
property dsMLeaderNoteAttachmentType_e RightAttachment {
   dsMLeaderNoteAttachmentType_e get();
   void set (    dsMLeaderNoteAttachmentType_e value);
}
```

### Property Value

Note right attachment type as defined by [dsMLeaderNoteAttachmentType_e](Interop.dsAutomation~Interop.dsAutomation.dsMLeaderNoteAttachmentType_e.html)

## Remarks

This property is valid only if this MLeader was created with Note content, [ISketchManager::InsertMLeaderWithNoteContentType](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertMLeaderWithNoteContentType.html) ([dsMLeaderContentType_e](Interop.dsAutomation~Interop.dsAutomation.dsMLeaderContentType_e.html).dsMLeaderContentType_Note).

## See Also

[IMLeader Interface](Interop.dsAutomation~Interop.dsAutomation.IMLeader.html)
[IMLeader Members](Interop.dsAutomation~Interop.dsAutomation.IMLeader_members.html)

## Availability

DraftSight 2024 SP4
