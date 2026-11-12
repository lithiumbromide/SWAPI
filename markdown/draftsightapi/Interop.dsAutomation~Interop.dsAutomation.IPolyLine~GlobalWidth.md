---
title: "GlobalWidth Property (IPolyLine)"
project: ""
interface: "IPolyLine"
member: "GlobalWidth"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GlobalWidth.html"
---

# GlobalWidth Property (IPolyLine)

Gets the width of the entire length of the 2D PolyLine.

## Syntax

### Visual Basic

```vb
Property GlobalWidth As System.Double
```

### C#

```csharp
System.double GlobalWidth {get; set;}
```

### JScript

```
function get,set GlobalWidth : System.double
```

### Managed Extensions for C++

```
__property System.double get_GlobalWidth();
__property void set_GlobalWidth(
   System.double value
);
```

### C++/CLI

```cpp
property System.double GlobalWidth {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Width of the entire length of the 2D PolyLine

## Remarks

To set different start and end widths, use [IPolyLine::SetSegmentEndWidth](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~SetSegmentEndWidth.html) and [IPolyLineSetSegmentStartWidth](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~SetSegmentStartWidth.html).

## See Also

[IPolyLine Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine.html)
[IPolyLine Members](Interop.dsAutomation~Interop.dsAutomation.IPolyLine_members.html)

## Availability

DraftSight V1R1.1
