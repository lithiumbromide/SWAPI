---
title: "ToleranceAttachment Property (IMLeader)"
project: ""
interface: "IMLeader"
member: "ToleranceAttachment"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMLeader~ToleranceAttachment.html"
---

# ToleranceAttachment Property (IMLeader)

Gets or sets the tolerance attachment type of this MLeader.

## Syntax

### Visual Basic

```vb
Property ToleranceAttachment As dsMLeaderTolAttachmentType_e
```

### C#

```csharp
dsMLeaderTolAttachmentType_e ToleranceAttachment {get; set;}
```

### JScript

```
function get,set ToleranceAttachment : dsMLeaderTolAttachmentType_e
```

### Managed Extensions for C++

```
__property dsMLeaderTolAttachmentType_e get_ToleranceAttachment();
__property void set_ToleranceAttachment(
   dsMLeaderTolAttachmentType_e value
);
```

### C++/CLI

```cpp
property dsMLeaderTolAttachmentType_e ToleranceAttachment {
   dsMLeaderTolAttachmentType_e get();
   void set (    dsMLeaderTolAttachmentType_e value);
}
```

### Property Value

Tolerance attachment type as defined by [dsMLeaderTolAttachmentType_e](Interop.dsAutomation~Interop.dsAutomation.dsMLeaderTolAttachmentType_e.html)

## Remarks

This property is valid only if this MLeader was created with Tolerance content, [ISketchManager::InsertMLeaderWithToleranceContentType](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertMLeaderWithToleranceContentType.html) ([dsMLeaderContentType_e](Interop.dsAutomation~Interop.dsAutomation.dsMLeaderContentType_e.html).dsMLeaderContentType_Tolerance).

## See Also

[IMLeader Interface](Interop.dsAutomation~Interop.dsAutomation.IMLeader.html)
[IMLeader Members](Interop.dsAutomation~Interop.dsAutomation.IMLeader_members.html)

## Availability

DraftSight 2024 SP4
