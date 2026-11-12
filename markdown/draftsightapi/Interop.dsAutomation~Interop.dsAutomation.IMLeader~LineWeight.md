---
title: "LineWeight Property (IMLeader)"
project: ""
interface: "IMLeader"
member: "LineWeight"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMLeader~LineWeight.html"
---

# LineWeight Property (IMLeader)

Gets or sets the general LineWeight of the text and leader for this MLeader.

## Syntax

### Visual Basic

```vb
Property LineWeight As dsLineWeight_e
```

### C#

```csharp
dsLineWeight_e LineWeight {get; set;}
```

### JScript

```
function get,set LineWeight : dsLineWeight_e
```

### Managed Extensions for C++

```
__property dsLineWeight_e get_LineWeight();
__property void set_LineWeight(
   dsLineWeight_e value
);
```

### C++/CLI

```cpp
property dsLineWeight_e LineWeight {
   dsLineWeight_e get();
   void set (    dsLineWeight_e value);
}
```

### Property Value

LineWeight as defined in [dsLineWeight_e](Interop.dsAutomation~Interop.dsAutomation.dsLineWeight_e.html)

## Remarks

This property may be overridden by [IMLeader::LeaderLineWeight](Interop.dsAutomation~Interop.dsAutomation.IMLeader~LeaderLineWeight.html).

## See Also

[IMLeader Interface](Interop.dsAutomation~Interop.dsAutomation.IMLeader.html)
[IMLeader Members](Interop.dsAutomation~Interop.dsAutomation.IMLeader_members.html)

## Availability

DraftSight 2024 SP4
