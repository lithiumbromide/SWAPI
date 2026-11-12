---
title: "BlockScale Property (IMLeader)"
project: ""
interface: "IMLeader"
member: "BlockScale"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMLeader~BlockScale.html"
---

# BlockScale Property (IMLeader)

Gets or sets the scale factor for Block insertions to this MLeader.

## Syntax

### Visual Basic

```vb
Property BlockScale As System.Double
```

### C#

```csharp
System.double BlockScale {get; set;}
```

### JScript

```
function get,set BlockScale : System.double
```

### Managed Extensions for C++

```
__property System.double get_BlockScale();
__property void set_BlockScale(
   System.double value
);
```

### C++/CLI

```cpp
property System.double BlockScale {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Block scale factor

## Remarks

This property is valid only if this MLeader was created with Block content, [ISketchManager::InsertMLeaderWithBlockContentType](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertMLeaderWithBlockContentType.html) ([dsMLeaderContentType_e](Interop.dsAutomation~Interop.dsAutomation.dsMLeaderContentType_e.html).dsMLeaderContentType_Block).

## See Also

[IMLeader Interface](Interop.dsAutomation~Interop.dsAutomation.IMLeader.html)
[IMLeader Members](Interop.dsAutomation~Interop.dsAutomation.IMLeader_members.html)

## Availability

DraftSight 2024 SP4
