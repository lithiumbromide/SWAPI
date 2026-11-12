---
title: "UseTemperatureCurve2 Property (ICWRadiation)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRadiation"
member: "UseTemperatureCurve2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation~UseTemperatureCurve2.html"
---

# UseTemperatureCurve2 Property (ICWRadiation)

Gets or sets whether to use a temperature curve for this radiation.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseTemperatureCurve2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRadiation
Dim value As System.Boolean

instance.UseTemperatureCurve2 = value

value = instance.UseTemperatureCurve2
```

### C#

```csharp
System.bool UseTemperatureCurve2 {get; set;}
```

### C++/CLI

```cpp
property System.bool UseTemperatureCurve2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

-1 or true to use temperature curve, 0 or false to not

## Examples

See the [ICWRadiation](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation.html) examples.

## Remarks

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

## See Also

[ICWRadiation Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation.html)
[ICWRadiation Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
