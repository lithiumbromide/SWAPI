---
title: "Scale Property (IRichLine)"
project: ""
interface: "IRichLine"
member: "Scale"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRichLine~Scale.html"
---

# Scale Property (IRichLine)

Gets or sets the scale factor for the width of the RichLine.

## Syntax

### Visual Basic

```vb
Property Scale As System.Double
```

### C#

```csharp
System.double Scale {get; set;}
```

### JScript

```
function get,set Scale : System.double
```

### Managed Extensions for C++

```
__property System.double get_Scale();
__property void set_Scale(
   System.double value
);
```

### C++/CLI

```cpp
property System.double Scale {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Scale factor for the width of the RichLine

## Remarks

The scale factor is based on the width of the [LineStyle](Interop.dsAutomation~Interop.dsAutomation.IRichLine~LineStyle.html). Specifying a scale factor of 2 for IRichLine::Scale results in a RichLine twice as wide as that defined by [IRichLine::LineScale](Interop.dsAutomation~Interop.dsAutomation.IRichLine~LineScale.html). IRichLine::Scale does not change IRichLine::LineScale.

To collapse the RichLine to a single line, specify a scale factor of 0.

## See Also

[IRichLine Interface](Interop.dsAutomation~Interop.dsAutomation.IRichLine.html)
[IRichLine Members](Interop.dsAutomation~Interop.dsAutomation.IRichLine_members.html)

## Availability

DraftSight V1R1.1
