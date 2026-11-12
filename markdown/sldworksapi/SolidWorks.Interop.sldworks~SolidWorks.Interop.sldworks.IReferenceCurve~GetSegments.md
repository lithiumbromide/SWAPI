---
title: "GetSegments Method (IReferenceCurve)"
project: "SOLIDWORKS API Help"
interface: "IReferenceCurve"
member: "GetSegments"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve~GetSegments.html"
---

# GetSegments Method (IReferenceCurve)

Gets the segments in this reference curve.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSegments() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IReferenceCurve
Dim value As System.Object

value = instance.GetSegments()
```

### C#

```csharp
System.object GetSegments()
```

### C++/CLI

```cpp
System.Object^ GetSegments();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [segments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)

## VBA Syntax

See [ReferenceCurve::GetSegments](ms-its:sldworksapivb6.chm::/sldworks~ReferenceCurve~GetSegments.html).

## See Also

[IReferenceCurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve.html)
[IReferenceCurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve_members.html)
[IReferenceCurve::IGetSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve~IGetSegments.html)
[IReferenceCurve::GetFirstSegment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve~GetFirstSegment.html)
[IReferenceCurve::GetNextSegment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve~GetNextSegment.html)
[IReferenceCurve::GetSegmentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve~GetSegmentCount.html)
[IReferenceCurve::IGetFirstSegment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve~IGetFirstSegment.html)
[IReferenceCurve::IGetNextSegment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve~IGetNextSegment.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
