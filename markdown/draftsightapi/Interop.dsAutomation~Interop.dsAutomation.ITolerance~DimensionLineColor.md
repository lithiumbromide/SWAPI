---
title: "DimensionLineColor Property (ITolerance)"
project: ""
interface: "ITolerance"
member: "DimensionLineColor"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITolerance~DimensionLineColor.html"
---

# DimensionLineColor Property (ITolerance)

Gets or sets the LineColor for the Dimension lines of the geometric Tolerance.

## Syntax

### Visual Basic

```vb
Property DimensionLineColor As Color
```

### C#

```csharp
Color DimensionLineColor {get; set;}
```

### JScript

```
function get,set DimensionLineColor : Color
```

### Managed Extensions for C++

```
__property Color* get_DimensionLineColor();
__property void set_DimensionLineColor(
   Color* value
);
```

### C++/CLI

```cpp
property Color^ DimensionLineColor {
   Color^ get();
   void set (    Color^ value);
}
```

### Property Value

[LineColor](Interop.dsAutomation~Interop.dsAutomation.IColor.html)

## See Also

[ITolerance Interface](Interop.dsAutomation~Interop.dsAutomation.ITolerance.html)
[ITolerance Members](Interop.dsAutomation~Interop.dsAutomation.ITolerance_members.html)

## Availability

DraftSight V1R1.2
