---
title: "EndAngle Property (IArcAlignedText)"
project: ""
interface: "IArcAlignedText"
member: "EndAngle"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IArcAlignedText~EndAngle.html"
---

# EndAngle Property (IArcAlignedText)

Gets or sets the end angle of the curved text.

## Syntax

### Visual Basic

```vb
Property EndAngle As System.Double
```

### C#

```csharp
System.double EndAngle {get; set;}
```

### JScript

```
function get,set EndAngle : System.double
```

### Managed Extensions for C++

```
__property System.double get_EndAngle();
__property void set_EndAngle(
   System.double value
);
```

### C++/CLI

```cpp
property System.double EndAngle {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

End angle

## Remarks

The end angle is the angle between two entities:

- the line segment connecting the end point of the arc to the center of the arc's circle

- and -

- the x-axis

## See Also

[IArcAlignedText Interface](Interop.dsAutomation~Interop.dsAutomation.IArcAlignedText.html)
[IArcAlignedText Members](Interop.dsAutomation~Interop.dsAutomation.IArcAlignedText_members.html)
[IArcAlignedText::StartAngle Property ()](Interop.dsAutomation~Interop.dsAutomation.IArcAlignedText~StartAngle.html)

## Availability

DraftSight 2018 SP2
