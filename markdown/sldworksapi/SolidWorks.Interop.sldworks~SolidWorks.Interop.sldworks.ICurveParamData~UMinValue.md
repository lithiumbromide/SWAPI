---
title: "UMinValue Property (ICurveParamData)"
project: "SOLIDWORKS API Help"
interface: "ICurveParamData"
member: "UMinValue"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveParamData~UMinValue.html"
---

# UMinValue Property (ICurveParamData)

Gets the minimum U parameter value.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property UMinValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICurveParamData
Dim value As System.Double

value = instance.UMinValue
```

### C#

```csharp
System.double UMinValue {get;}
```

### C++/CLI

```cpp
property System.double UMinValue {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Minimum U parameter value

## VBA Syntax

See [CurveParamData::UMinValue](ms-its:sldworksapivb6.chm::/sldworks~CurveParamData~UMinValue.html).

## Examples

[Get Edge Curve Parameterization (C#)](Get_Edge_Curve_Parameterization_Example_CSharp.htm)
[Get Edge Curve Parameterization (VB.NET)](Get_Edge_Curve_Parameterization_Example_VBNET.htm)
[Get Edge Curve Parameterization (VBA)](Get_Edge_Curve_Parameterization_Example_VB.htm)

## Remarks

The minimum U parameter must always be smaller than the maximum U parameter.

If the curve and edge are in opposite directions ([ICurveParamData::Sense](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurveParamData~Sense.html) returns false) and the minimum U parameter is larger than the maximum U parameter, then the parameters are in negative parameter space. For example, if ICurveParamData::Sense is false, minimum U parameter is 10, and maximum U parameter is 5, then ICurveParamData::UMinValue = -10 and [ICurveParamData::UMaxValue](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurveParamData~UMaxValue.html) = -5. To normalize the values in positive parameter space, swap the two U parameter values and then negate them, so that the values of the minimum U parameter is 5 and the maximum U parameter is 10.

If the curve is closed and the curve starts and ends at the same point, then ICurveParamData::UMinValue and ICurveParamData::UMaxValue are a period apart.

## See Also

[ICurveParamData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveParamData.html)
[ICurveParamData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveParamData_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
