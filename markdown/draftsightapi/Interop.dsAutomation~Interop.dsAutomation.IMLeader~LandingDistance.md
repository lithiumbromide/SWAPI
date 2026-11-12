---
title: "LandingDistance Property (IMLeader)"
project: ""
interface: "IMLeader"
member: "LandingDistance"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMLeader~LandingDistance.html"
---

# LandingDistance Property (IMLeader)

Gets or sets the length of the horizontal landing line for this MLeader.

## Syntax

### Visual Basic

```vb
Property LandingDistance As System.Double
```

### C#

```csharp
System.double LandingDistance {get; set;}
```

### JScript

```
function get,set LandingDistance : System.double
```

### Managed Extensions for C++

```
__property System.double get_LandingDistance();
__property void set_LandingDistance(
   System.double value
);
```

### C++/CLI

```cpp
property System.double LandingDistance {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Horizontal landing line distance

## Remarks

This property is valid only if [IMLeader::HorzLanding](Interop.dsAutomation~Interop.dsAutomation.IMLeader~HorzLanding.html) is true.

## See Also

[IMLeader Interface](Interop.dsAutomation~Interop.dsAutomation.IMLeader.html)
[IMLeader Members](Interop.dsAutomation~Interop.dsAutomation.IMLeader_members.html)

## Availability

DraftSight 2024 SP4
