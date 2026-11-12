---
title: "NoteAttachmentDirectionType Property (IMLeader)"
project: ""
interface: "IMLeader"
member: "NoteAttachmentDirectionType"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMLeader~NoteAttachmentDirectionType.html"
---

# NoteAttachmentDirectionType Property (IMLeader)

Gets or sets the Note attachment direction type of this MLeader.

## Syntax

### Visual Basic

```vb
Property NoteAttachmentDirectionType As dsNoteDirection_e
```

### C#

```csharp
dsNoteDirection_e NoteAttachmentDirectionType {get; set;}
```

### JScript

```
function get,set NoteAttachmentDirectionType : dsNoteDirection_e
```

### Managed Extensions for C++

```
__property dsNoteDirection_e get_NoteAttachmentDirectionType();
__property void set_NoteAttachmentDirectionType(
   dsNoteDirection_e value
);
```

### C++/CLI

```cpp
property dsNoteDirection_e NoteAttachmentDirectionType {
   dsNoteDirection_e get();
   void set (    dsNoteDirection_e value);
}
```

### Property Value

Note attachment direction type as defined by [dsNoteDirection_e](Interop.dsAutomation~Interop.dsAutomation.dsNoteDirection_e.html)

## Remarks

This property is valid only if this MLeader was created with Note content, [ISketchManager::InsertMLeaderWithNoteContentType](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertMLeaderWithNoteContentType.html) ([dsMLeaderContentType_e](Interop.dsAutomation~Interop.dsAutomation.dsMLeaderContentType_e.html).dsMLeaderContentType_Note).

## See Also

[IMLeader Interface](Interop.dsAutomation~Interop.dsAutomation.IMLeader.html)
[IMLeader Members](Interop.dsAutomation~Interop.dsAutomation.IMLeader_members.html)

## Availability

DraftSight 2024 SP4
