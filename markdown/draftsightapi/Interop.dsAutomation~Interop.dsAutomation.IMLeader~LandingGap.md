---
title: "LandingGap Property (IMLeader)"
project: ""
interface: "IMLeader"
member: "LandingGap"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMLeader~LandingGap.html"
---

# LandingGap Property (IMLeader)

Gets or sets the gap between the landing line and the Note text of this MLeader.

## Syntax

### Visual Basic

```vb
Property LandingGap As System.Double
```

### C#

```csharp
System.double LandingGap {get; set;}
```

### JScript

```
function get,set LandingGap : System.double
```

### Managed Extensions for C++

```
__property System.double get_LandingGap();
__property void set_LandingGap(
   System.double value
);
```

### C++/CLI

```cpp
property System.double LandingGap {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Gap between the landing line and the Note text

## Remarks

This property is valid only if this MLeader was created with Note content, [ISketchManager::InsertMLeaderWithNoteContentType](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertMLeaderWithNoteContentType.html) ([dsMLeaderContentType_e](Interop.dsAutomation~Interop.dsAutomation.dsMLeaderContentType_e.html).dsMLeaderContentType_Note).

## See Also

[IMLeader Interface](Interop.dsAutomation~Interop.dsAutomation.IMLeader.html)
[IMLeader Members](Interop.dsAutomation~Interop.dsAutomation.IMLeader_members.html)

## Availability

DraftSight 2024 SP4
