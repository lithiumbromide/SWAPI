---
title: "dsMLeaderNoteAttachmentType_e Enumeration"
project: ""
interface: "dsMLeaderNoteAttachmentType_e"
member: ""
kind: "enum"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.dsMLeaderNoteAttachmentType_e.html"
---

# dsMLeaderNoteAttachmentType_e Enumeration

IMLeader Note attachment options.

## Syntax

### Visual Basic

```vb
Public Enum dsMLeaderNoteAttachmentType_e
   Inherits System.Enum
```

### C#

```csharp
public enum dsMLeaderNoteAttachmentType_e : System.Enum
```

### JScript

```
public enum dsMLeaderNoteAttachmentType_e extends System.Enum
```

### Managed Extensions for C++

```
__value public enum dsMLeaderNoteAttachmentType_e : public System.Enum
```

### C++/CLI

```cpp
public enum class dsMLeaderNoteAttachmentType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| dsMLeaderNoteAttachmentType_AllLine | 8 = For left/right horizontal leader attachments of Notes, underline all content and attach to bottom of the top line of a multi-line Note |
| dsMLeaderNoteAttachmentType_BottomLine | 5 = For left/right horizontal leader attachments of Notes, attach to and underline bottom line of multi-line Note |
| dsMLeaderNoteAttachmentType_BottomOfBottom | 4 = For left/right horizontal leader attachments of Notes; attachment at bottom of bottom line of multi-line Note |
| dsMLeaderNoteAttachmentType_BottomOfTop | 7 = For left/right horizontal leader attachments of Notes; attachment at bottom of top line of multi-line Note |
| dsMLeaderNoteAttachmentType_BottomOfTopLine | 6 = For left/right horizontal leader attachments of Notes; attachment at bottom of top line of multi-line Note |
| dsMLeaderNoteAttachmentType_Center | 9 = For vertical leader attachments of Notes, center attachment at the top or bottom of Note |
| dsMLeaderNoteAttachmentType_LinedCenter | 10 = For vertical leader attachments of Notes; underline bottom of Note and center leader attachment beneath Note; overline top of Note and center leader attachment above Note |
| dsMLeaderNoteAttachmentType_Middle | 2 = For left/right horizontal leader attachments of Notes; attachment at middle of Note text |
| dsMLeaderNoteAttachmentType_MiddleOfBottom | 3 = For left/right horizontal leader attachments of Notes; attachment at middle of bottom line of multi-line Note |
| dsMLeaderNoteAttachmentType_MiddleOfTop | 1 = For left/right horizontal leader attachments of Notes; attachment at middle of top line of multi-line Note |
| dsMLeaderNoteAttachmentType_TopOfTop | 0 = For left/right horizontal leader attachments of Notes; attachment at top of top line of multi-line Note |

## Remarks

See [dsMLeaderNoteJustify_e](Interop.dsAutomation~Interop.dsAutomation.dsMLeaderNoteJustify_e.html) for justify options.

For more information, see **DraftSight user-interface help > Creating and Modifying Dimensions > Working with Leaders and Geometric Tolerances > Working with MultiLeaderStyles**.

## See Also

[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
