---
title: "UseTimeCurve2 Property (ICWTemperature)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTemperature"
member: "UseTimeCurve2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTemperature~UseTimeCurve2.html"
---

# UseTimeCurve2 Property (ICWTemperature)

Gets or sets whether to use time curve data with the temperature.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseTimeCurve2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTemperature
Dim value As System.Boolean

instance.UseTimeCurve2 = value

value = instance.UseTimeCurve2
```

### C#

```csharp
System.bool UseTimeCurve2 {get; set;}
```

### C++/CLI

```cpp
property System.bool UseTimeCurve2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

-1 or true to use time curve data, 0 or false to not

## Remarks

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

## See Also

[ICWTemperature Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTemperature.html)
[ICWTemperature Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTemperature_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
