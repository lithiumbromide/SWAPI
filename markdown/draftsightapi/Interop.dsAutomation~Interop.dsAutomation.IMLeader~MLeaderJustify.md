---
title: "MLeaderJustify Property (IMLeader)"
project: ""
interface: "IMLeader"
member: "MLeaderJustify"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMLeader~MLeaderJustify.html"
---

# MLeaderJustify Property (IMLeader)

Gets or sets the type of alignment of the Note for this MLeader.

## Syntax

### Visual Basic

```vb
Property MLeaderJustify As dsMLeaderNoteJustify_e
```

### C#

```csharp
dsMLeaderNoteJustify_e MLeaderJustify {get; set;}
```

### JScript

```
function get,set MLeaderJustify : dsMLeaderNoteJustify_e
```

### Managed Extensions for C++

```
__property dsMLeaderNoteJustify_e get_MLeaderJustify();
__property void set_MLeaderJustify(
   dsMLeaderNoteJustify_e value
);
```

### C++/CLI

```cpp
property dsMLeaderNoteJustify_e MLeaderJustify {
   dsMLeaderNoteJustify_e get();
   void set (    dsMLeaderNoteJustify_e value);
}
```

### Property Value

Note alignment as defined by [dsMLeaderNoteJustify_e](Interop.dsAutomation~Interop.dsAutomation.dsMLeaderNoteJustify_e.html)

## Remarks

This property is valid only if this MLeader was created with Note content, [ISketchManager::InsertMLeaderWithNoteContentType](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertMLeaderWithNoteContentType.html) ([dsMLeaderContentType_e](Interop.dsAutomation~Interop.dsAutomation.dsMLeaderContentType_e.html).dsMLeaderContentType_Note).

## See Also

[IMLeader Interface](Interop.dsAutomation~Interop.dsAutomation.IMLeader.html)
[IMLeader Members](Interop.dsAutomation~Interop.dsAutomation.IMLeader_members.html)

## Availability

DraftSight 2024 SP4
