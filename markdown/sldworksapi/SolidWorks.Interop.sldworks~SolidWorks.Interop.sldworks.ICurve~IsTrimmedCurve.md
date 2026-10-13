---
title: "IsTrimmedCurve Method (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "IsTrimmedCurve"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsTrimmedCurve.html"
---

# IsTrimmedCurve Method (ICurve)

Gets whether the curve is trimmed.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsTrimmedCurve() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim value As System.Boolean

value = instance.IsTrimmedCurve()
```

### C#

```csharp
System.bool IsTrimmedCurve()
```

### C++/CLI

```cpp
System.bool IsTrimmedCurve();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if this curve is a trimmed curve, false if other curve type

## VBA Syntax

See [Curve::IsTrimmedCurve](ms-its:sldworksapivb6.chm::/sldworks~Curve~IsTrimmedCurve.html).

## Examples

[Create Space Parameter Curve on Surface (VBA)](Create_Space_Parameter_Curve_on_Surface_Example_VB.htm)
[Get Intersecting Faces (VBA)](Get_Intersecting_Faces_Example_VB.htm)
[Get Sketch Segment and Curve Data (VBA)](Get_Sketch_Segment_and_Curve_Data_Example_VB.htm)
[Get Whether Sketch Segment is Trimmed (VBA)](Get_Whether_Sketch_Segment_is_Trimmed_or_Not_Example_VB.htm)

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html)
[ICurve::IsBcurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~IsBcurve.html)
[ICurve::CreateTrimmedCurve2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~CreateTrimmedCurve2.html)
[ICurve::Identity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~Identity.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
