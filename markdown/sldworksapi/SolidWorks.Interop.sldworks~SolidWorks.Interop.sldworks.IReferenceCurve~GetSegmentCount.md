---
title: "GetSegmentCount Method (IReferenceCurve)"
project: "SOLIDWORKS API Help"
interface: "IReferenceCurve"
member: "GetSegmentCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve~GetSegmentCount.html"
---

# GetSegmentCount Method (IReferenceCurve)

Gets the number of curve segments in a reference curve feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSegmentCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IReferenceCurve
Dim value As System.Integer

value = instance.GetSegmentCount()
```

### C#

```csharp
System.int GetSegmentCount()
```

### C++/CLI

```cpp
System.int GetSegmentCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of segments in the curve

## VBA Syntax

See [ReferenceCurve::GetSegmentCount](ms-its:sldworksapivb6.chm::/sldworks~ReferenceCurve~GetSegmentCount.html).

## Examples

[Get Curve Segments (VBA)](Get_Curve_Segments_Example_VB.htm)

## See Also

[IReferenceCurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve.html)
[IReferenceCurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve_members.html)
[IReferenceCurve::GetFirstSegment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve~GetFirstSegment.html)
[IReferenceCurve::IGetFirstSegment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve~IGetFirstSegment.html)
[IReferenceCurve::GetNextSegment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve~GetNextSegment.html)
[IReferenceCurve::IGetNextSegment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve~IGetNextSegment.html)
[IReferenceCurve::GetSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve~GetSegments.html)
[IReferenceCurve::IGetSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve~IGetSegments.html)
