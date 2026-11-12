---
title: "ReverseDirection2 Property (ICWPressure)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPressure"
member: "ReverseDirection2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~ReverseDirection2.html"
---

# ReverseDirection2 Property (ICWPressure)

Gets or sets whether to reverse the direction of this pressure.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReverseDirection2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPressure
Dim value As System.Boolean

instance.ReverseDirection2 = value

value = instance.ReverseDirection2
```

### C#

```csharp
System.bool ReverseDirection2 {get; set;}
```

### C++/CLI

```cpp
property System.bool ReverseDirection2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

-1 or true to reverse direction, 0 or false to not

## Examples

See the [ICWPressure](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure.html) examples.

## Remarks

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

## See Also

[ICWPressure Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure.html)
[ICWPressure Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
