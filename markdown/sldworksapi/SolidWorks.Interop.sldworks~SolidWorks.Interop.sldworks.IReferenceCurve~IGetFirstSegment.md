---
title: "IGetFirstSegment Method (IReferenceCurve)"
project: "SOLIDWORKS API Help"
interface: "IReferenceCurve"
member: "IGetFirstSegment"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve~IGetFirstSegment.html"
---

# IGetFirstSegment Method (IReferenceCurve)

Gets the first curve segment in a reference curve feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFirstSegment() As Edge
```

### Visual Basic (Usage)

```vb
Dim instance As IReferenceCurve
Dim value As Edge

value = instance.IGetFirstSegment()
```

### C#

```csharp
Edge IGetFirstSegment()
```

### C++/CLI

```cpp
Edge^ IGetFirstSegment();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

First [edge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) for the segment

## VBA Syntax

See [ReferenceCurve::IGetFirstSegment](ms-its:sldworksapivb6.chm::/sldworks~ReferenceCurve~IGetFirstSegment.html).

## Remarks

Because edges returned by this method are not selectable; you should not call any Select methods to get them. Select methods return NULL for any returned edges.

## See Also

[IReferenceCurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve.html)
[IReferenceCurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve_members.html)
[IReferenceCurve::GetFirstSegment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve~GetFirstSegment.html)
[IReferenceCurve::GetSegmentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve~GetSegmentCount.html)
[IReferenceCurve::GetNextSegment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve~GetNextSegment.html)
[IReferenceCurve::IGetNextSegment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve~IGetNextSegment.html)
[IReferenceCurve::GetSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve~GetSegments.html)
[IReferenceCurve::IGetSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve~IGetSegments.html)
