---
title: "GetNextSegment Method (IReferenceCurve)"
project: "SOLIDWORKS API Help"
interface: "IReferenceCurve"
member: "GetNextSegment"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve~GetNextSegment.html"
---

# GetNextSegment Method (IReferenceCurve)

Gets the next curve segment in the reference curve feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNextSegment() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IReferenceCurve
Dim value As System.Object

value = instance.GetNextSegment()
```

### C#

```csharp
System.object GetNextSegment()
```

### C++/CLI

```cpp
System.Object^ GetNextSegment();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Next [edge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) for the segment

## VBA Syntax

See [ReferenceCurve::GetNextSegment](ms-its:sldworksapivb6.chm::/sldworks~ReferenceCurve~GetNextSegment.html).

## Examples

[Get Curve Segments (VBA)](Get_Curve_Segments_Example_VB.htm)
[Get Reference Curve Information (VBA)](Get_Reference_Curve_Information_Example_VB.htm)

## Remarks

Because edges returned by this method are not selectable; you should not call any Select methods to get them. Select methods return NULL for any returned edges.

## See Also

[IReferenceCurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve.html)
[IReferenceCurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve_members.html)
[IReferenceCurve::IGetNextSegment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve~IGetNextSegment.html)
[IReferenceCurve::GetFirstSegment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve~GetFirstSegment.html)
[IReferenceCurve::IGetFirstSegment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve~IGetFirstSegment.html)
[IReferenceCurve::GetSegmentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve~GetSegmentCount.html)
[IReferenceCurve::GetSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve~GetSegments.html)
[IReferenceCurve::IGetSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve~IGetSegments.html)
