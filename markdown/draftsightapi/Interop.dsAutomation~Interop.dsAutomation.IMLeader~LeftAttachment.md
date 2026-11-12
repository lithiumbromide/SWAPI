---
title: "LeftAttachment Property (IMLeader)"
project: ""
interface: "IMLeader"
member: "LeftAttachment"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMLeader~LeftAttachment.html"
---

# LeftAttachment Property (IMLeader)

Gets or sets the left attachment of the Note for this MLeader.

## Syntax

### Visual Basic

```vb
Property LeftAttachment As dsMLeaderNoteAttachmentType_e
```

### C#

```csharp
dsMLeaderNoteAttachmentType_e LeftAttachment {get; set;}
```

### JScript

```
function get,set LeftAttachment : dsMLeaderNoteAttachmentType_e
```

### Managed Extensions for C++

```
__property dsMLeaderNoteAttachmentType_e get_LeftAttachment();
__property void set_LeftAttachment(
   dsMLeaderNoteAttachmentType_e value
);
```

### C++/CLI

```cpp
property dsMLeaderNoteAttachmentType_e LeftAttachment {
   dsMLeaderNoteAttachmentType_e get();
   void set (    dsMLeaderNoteAttachmentType_e value);
}
```

### Property Value

Note left attachment type as defined by [dsMLeaderNoteAttachmentType_e](Interop.dsAutomation~Interop.dsAutomation.dsMLeaderNoteAttachmentType_e.html)

## Remarks

This property is valid only if this MLeader was created with Note content, [ISketchManager::InsertMLeaderWithNoteContentType](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertMLeaderWithNoteContentType.html) ([dsMLeaderContentType_e](Interop.dsAutomation~Interop.dsAutomation.dsMLeaderContentType_e.html).dsMLeaderContentType_Note).

## See Also

[IMLeader Interface](Interop.dsAutomation~Interop.dsAutomation.IMLeader.html)
[IMLeader Members](Interop.dsAutomation~Interop.dsAutomation.IMLeader_members.html)

## Availability

DraftSight 2024 SP4
