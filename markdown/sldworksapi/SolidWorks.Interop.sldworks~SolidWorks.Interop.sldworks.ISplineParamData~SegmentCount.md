---
title: "SegmentCount Property (ISplineParamData)"
project: "SOLIDWORKS API Help"
interface: "ISplineParamData"
member: "SegmentCount"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~SegmentCount.html"
---

# SegmentCount Property (ISplineParamData)

Gets the number of segments in the spline.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property SegmentCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISplineParamData
Dim value As System.Integer

value = instance.SegmentCount
```

### C#

```csharp
System.int SegmentCount {get;}
```

### C++/CLI

```cpp
property System.int SegmentCount {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of segments if a P-spline, -1 if not

## VBA Syntax

See [SplineParamData::SegmentCount](ms-its:sldworksapivb6.chm::/sldworks~SplineParamData~SegmentCount.html).

## Examples

[Get P-Spline Parameterization Data (C#)](Get_P-Spline_Parameterization_Data_Example_CSharp.htm)
[Get P-Spline Parameterization Data (VB.NET)](Get_P-Spline_Parameterization_Data_Example_VBNET.htm)
[Get P-Spline Parameterization Data (VBA)](Get_P-Spline_Parameterization_Data_Example_VB.htm)

## Remarks

This method works only with P-spline parameter data. Before calling this method, call [ICurve::GetPCurveParams2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~GetPCurveParams2.html) to generate P-spline parameterization data object for the curve.

## See Also

[ISplineParamData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData.html)
[ISplineParamData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData_members.html)
[ISplineParamData::GetSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~GetSegments.html)
[ISplineParamData::IGetSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData~IGetSegments.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
