---
title: "UseBulkTemperatureTimeCurve2 Property (ICWConvection)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWConvection"
member: "UseBulkTemperatureTimeCurve2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection~UseBulkTemperatureTimeCurve2.html"
---

# UseBulkTemperatureTimeCurve2 Property (ICWConvection)

Gets or sets whether to use a bulk temperature curve for convection.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseBulkTemperatureTimeCurve2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWConvection
Dim value As System.Boolean

instance.UseBulkTemperatureTimeCurve2 = value

value = instance.UseBulkTemperatureTimeCurve2
```

### C#

```csharp
System.bool UseBulkTemperatureTimeCurve2 {get; set;}
```

### C++/CLI

```cpp
property System.bool UseBulkTemperatureTimeCurve2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

-1 or true to use bulk temperature curve, 0 or false to not

## Remarks

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

## See Also

[ICWConvection Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection.html)
[ICWConvection Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWConvection_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
