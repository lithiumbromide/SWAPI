---
title: "IConvertArcToBcurveSize Method (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "IConvertArcToBcurveSize"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IConvertArcToBcurveSize.html"
---

# IConvertArcToBcurveSize Method (ICurve)

Gets the b-curve size for the arc's conversion given the coordinates of the two end points of a line.

## Syntax

### Visual Basic (Declaration)

```vb
Function IConvertArcToBcurveSize( _
   ByRef Center As System.Double, _
   ByRef Axis As System.Double, _
   ByRef Start As System.Double, _
   ByRef End As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim Center As System.Double
Dim Axis As System.Double
Dim Start As System.Double
Dim End As System.Double
Dim value As System.Integer

value = instance.IConvertArcToBcurveSize(Center, Axis, Start, End)
```

### C#

```csharp
System.int IConvertArcToBcurveSize(
   ref System.double Center,
   ref System.double Axis,
   ref System.double Start,
   ref System.double End
)
```

### C++/CLI

```cpp
System.int IConvertArcToBcurveSize(
   System.double% Center,
   System.double% Axis,
   System.double% Start,
   System.double% End
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Center`: Pointer to an array of doubles (x, y, z), the coordinates of the arc center
- `Axis`: Pointer to an array of doubles (x, y, z), the normal vector of the arc
- `Start`: Pointer to an array of doubles (x, y, z), the coordinates of the arc start point
- `End`: Pointer to an array of doubles (x, y, z), the coordinates of the arc end point

### Return Value

Size of the data necessary for the conversion to a b-curve

## VBA Syntax

See [Curve::IConvertArcToBcurveSize](ms-its:sldworksapivb6.chm::/sldworks~Curve~IConvertArcToBcurveSize.html).

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html)
[ICurve::ConvertArcToBcurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ConvertArcToBcurve.html)
[ICurve::ExtentCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ExtentCurve.html)
[ICurve::GetBCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetBCurveParams.html)
[ICurve::IGetBCurveParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetBCurveParams.html)
[ICurve::IGetBCurveParamsSize2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IGetBCurveParamsSize2.html)
[ICurve::IsBcurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsBcurve.html)
[ICurve::MakeBsplineCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~MakeBsplineCurve.html)
[ICurve::SimplifyBCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~SimplifyBCurve.html)
[ICurve::IConvertLineToBcurveSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IConvertLineToBcurveSize.html)
[ICurve::IConvertPcurveToBcurveSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IConvertPcurveToBcurveSize.html)
[ICurve::ConvertLineToBcurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ConvertLineToBcurve.html)
