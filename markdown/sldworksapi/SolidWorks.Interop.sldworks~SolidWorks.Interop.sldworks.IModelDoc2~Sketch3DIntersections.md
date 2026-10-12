---
title: "Sketch3DIntersections Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "Sketch3DIntersections"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Sketch3DIntersections.html"
---

# Sketch3DIntersections Method (IModelDoc2)

Creates new sketch segments based on the selected surfaces.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Sketch3DIntersections()
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2

instance.Sketch3DIntersections()
```

### C#

```csharp
void Sketch3DIntersections()
```

### C++/CLI

```cpp
void Sketch3DIntersections();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDoc2::Sketch3DIntersections](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~Sketch3DIntersections.html).

## Remarks

The new sketch segments are added either to the active sketch or to an appropriate new sketch.

If the active sketch is a 2D sketch and the intersection curves are not in that plane, then the resulting sketch segments are projected onto the plane of the sketch.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[ISurface::GetIntersectCurveCount2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetIntersectCurveCount2.html)
[ISurface::IIntersectCurve2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IIntersectCurve2.html)
[ISurface::IntersectCurve2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IntersectCurve2.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
