---
title: "Sense Property (ICurveParamData)"
project: "SOLIDWORKS API Help"
interface: "ICurveParamData"
member: "Sense"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveParamData~Sense.html"
---

# Sense Property (ICurveParamData)

Gets whether the curve and edge are in the same direction.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Sense As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICurveParamData
Dim value As System.Boolean

value = instance.Sense
```

### C#

```csharp
System.bool Sense {get;}
```

### C++/CLI

```cpp
property System.bool Sense {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if curve and edge are in the same direction, false if not

## VBA Syntax

See [CurveParamData::Sense](ms-its:sldworksapivb6.chm::/sldworks~CurveParamData~Sense.html).

## Examples

[Get Edge Curve Parameterization (C#)](Get_Edge_Curve_Parameterization_Example_CSharp.htm)
[Get Edge Curve Parameterization (VB.NET)](Get_Edge_Curve_Parameterization_Example_VBNET.htm)
[Get Edge Curve Parameterization (VBA)](Get_Edge_Curve_Parameterization_Example_VB.htm)

## Remarks

If this method returns False, then the curve and edge are in opposite directions. In that case, [ICurveParamData::StartPoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurveParamData~StartPoint.html) corresponds to the end of the edge, [ICurveParamData::EndPoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurveParamData~EndPoint.html) corresponds to the start of the edge.

## See Also

[ICurveParamData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveParamData.html)
[ICurveParamData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveParamData_members.html)
[ICurveParamData::UMaxValue Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveParamData~UMaxValue.html)
[ICurveParamData::UMinValue Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveParamData~UMinValue.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
