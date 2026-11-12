---
title: "IGetSegments Method (IReferenceCurve)"
project: "SOLIDWORKS API Help"
interface: "IReferenceCurve"
member: "IGetSegments"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve~IGetSegments.html"
---

# IGetSegments Method (IReferenceCurve)

Gets the segments in this reference curve.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSegments( _
   ByVal NumSegments As System.Integer _
) As Edge
```

### Visual Basic (Usage)

```vb
Dim instance As IReferenceCurve
Dim NumSegments As System.Integer
Dim value As Edge

value = instance.IGetSegments(NumSegments)
```

### C#

```csharp
Edge IGetSegments(
   System.int NumSegments
)
```

### C++/CLI

```cpp
Edge^ IGetSegments(
   System.int NumSegments
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumSegments`: Number of segments in the reference curve

### Return Value

- in-process, unmanaged C++: Pointer to an array of [segments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) in the reference curve

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [IReferenceCurve::GetSegmentCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IReferenceCurve~GetSegmentCount.html) to get NumSegments.

## See Also

[IReferenceCurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve.html)
[IReferenceCurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve_members.html)
[IReferenceCurve::GetSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve~GetSegments.html)
[IReferenceCurve::IGetFirstSegment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve~IGetFirstSegment.html)
[IReferenceCurve::IGetNextSegment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve~IGetNextSegment.html)
[IReferenceCurve::GetFirstSegment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve~GetFirstSegment.html)
[IReferenceCurve::GetNextSegment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve~GetNextSegment.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
