---
title: "BlockColor Property (IMLeader)"
project: ""
interface: "IMLeader"
member: "BlockColor"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMLeader~BlockColor.html"
---

# BlockColor Property (IMLeader)

Gets or sets the color of the Block content for this MLeader.

## Syntax

### Visual Basic

```vb
Property BlockColor As Color
```

### C#

```csharp
Color BlockColor {get; set;}
```

### JScript

```
function get,set BlockColor : Color
```

### Managed Extensions for C++

```
__property Color* get_BlockColor();
__property void set_BlockColor(
   Color* value
);
```

### C++/CLI

```cpp
property Color^ BlockColor {
   Color^ get();
   void set (    Color^ value);
}
```

### Property Value

[BlockColor](Interop.dsAutomation~Interop.dsAutomation.IColor.html)

## Remarks

This property is valid only if this MLeader was created with Block content, [ISketchManager::InsertMLeaderWithBlockContentType](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertMLeaderWithBlockContentType.html) ([dsMLeaderContentType_e](Interop.dsAutomation~Interop.dsAutomation.dsMLeaderContentType_e.html).dsMLeaderContentType_Block).

## See Also

[IMLeader Interface](Interop.dsAutomation~Interop.dsAutomation.IMLeader.html)
[IMLeader Members](Interop.dsAutomation~Interop.dsAutomation.IMLeader_members.html)

## Availability

DraftSight 2024 SP4
