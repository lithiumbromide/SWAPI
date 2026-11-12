---
title: "Angle Property (ITextStyle)"
project: ""
interface: "ITextStyle"
member: "Angle"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITextStyle~Angle.html"
---

# Angle Property (ITextStyle)

Gets or sets the angle of the TextStyle.

## Syntax

### Visual Basic

```vb
Property Angle As System.Double
```

### C#

```csharp
System.double Angle {get; set;}
```

### JScript

```
function get,set Angle : System.double
```

### Managed Extensions for C++

```
__property System.double get_Angle();
__property void set_Angle(
   System.double value
);
```

### C++/CLI

```cpp
property System.double Angle {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Angle (see **Remarks**)

## Remarks

The angle defines the inclination of the characters in relation to the horizontal (x-axis) line.

| Values between... | Result in an inclination to the... |
| --- | --- |
| 0 and 84.90 | right (forward) |
| 0 and -84.90 | left (backwards) |

## See Also

[ITextStyle Interface](Interop.dsAutomation~Interop.dsAutomation.ITextStyle.html)
[ITextStyle Members](Interop.dsAutomation~Interop.dsAutomation.ITextStyle_members.html)

## Availability

DraftSight V1R1.1
