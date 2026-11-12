---
title: "HorzLanding Property (IMLeader)"
project: ""
interface: "IMLeader"
member: "HorzLanding"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMLeader~HorzLanding.html"
---

# HorzLanding Property (IMLeader)

Gets or sets whether to draw a horizontal landing line at the end of this MLeader.

## Syntax

### Visual Basic

```vb
Property HorzLanding As System.Boolean
```

### C#

```csharp
System.bool HorzLanding {get; set;}
```

### JScript

```
function get,set HorzLanding : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_HorzLanding();
__property void set_HorzLanding(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool HorzLanding {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to draw a horizontal landing line, false to not

## Remarks

If this property is set to true, use [IMLeader::LandingDistance](Interop.dsAutomation~Interop.dsAutomation.IMLeader~LandingDistance.html) to specify the length of the landing line.

## See Also

[IMLeader Interface](Interop.dsAutomation~Interop.dsAutomation.IMLeader.html)
[IMLeader Members](Interop.dsAutomation~Interop.dsAutomation.IMLeader_members.html)

## Availability

DraftSight 2024 SP4
