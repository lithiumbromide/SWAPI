---
title: "StartAngle Property (IArcAlignedText)"
project: ""
interface: "IArcAlignedText"
member: "StartAngle"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IArcAlignedText~StartAngle.html"
---

# StartAngle Property (IArcAlignedText)

Gets or sets the start angle of the curved text.

## Syntax

### Visual Basic

```vb
Property StartAngle As System.Double
```

### C#

```csharp
System.double StartAngle {get; set;}
```

### JScript

```
function get,set StartAngle : System.double
```

### Managed Extensions for C++

```
__property System.double get_StartAngle();
__property void set_StartAngle(
   System.double value
);
```

### C++/CLI

```cpp
property System.double StartAngle {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Value of start angle

## Remarks

The start angle is the angle between two entities:

- the line segment connecting the start point of the arc to the center of the arc's circle

- and -

- the x-axis

## See Also

[IArcAlignedText Interface](Interop.dsAutomation~Interop.dsAutomation.IArcAlignedText.html)
[IArcAlignedText Members](Interop.dsAutomation~Interop.dsAutomation.IArcAlignedText_members.html)
[IArcAlignedText::EndAngle Property ()](Interop.dsAutomation~Interop.dsAutomation.IArcAlignedText~EndAngle.html)

## Availability

DraftSight 2018 SP2
