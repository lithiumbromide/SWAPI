---
title: "IsPartial Property (IArcLengthDimension)"
project: ""
interface: "IArcLengthDimension"
member: "IsPartial"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IArcLengthDimension~IsPartial.html"
---

# IsPartial Property (IArcLengthDimension)

Gets or sets whether the arc length Dimension measures the length of part of an Arc.

## Syntax

### Visual Basic

```vb
Property IsPartial As System.Boolean
```

### C#

```csharp
System.bool IsPartial {get; set;}
```

### JScript

```
function get,set IsPartial : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_IsPartial();
__property void set_IsPartial(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool IsPartial {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True if the arc length Dimension measures the length of part of an Arc, false if it measures the entire length of the Arc

## Examples

[Create and Apply DimensionStyle (C#)](Create_and_Apply_DimensionStyle_Example_CSharp.htm)
[Create and Apply DimensionStyle (VB.NET)](Create_and_Apply_DimensionStyle_Example_VBNET.htm)
[Create and Apply DimensionStyle (VBA)](Create_and_Apply_DimensionStyle_Example_VBA.htm)

## See Also

[IArcLengthDimension Interface](Interop.dsAutomation~Interop.dsAutomation.IArcLengthDimension.html)
[IArcLengthDimension Members](Interop.dsAutomation~Interop.dsAutomation.IArcLengthDimension_members.html)

## Availability

DraftSight V1R1.2
