---
title: "SplitClosedSegment Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SplitClosedSegment"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SplitClosedSegment.html"
---

# SplitClosedSegment Method (IModelDoc2)

Obsolete. Superseded by [ISketchManager::SplitClosedSegment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~SplitClosedSegment.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SplitClosedSegment( _
   ByVal X0 As System.Double, _
   ByVal Y0 As System.Double, _
   ByVal Z0 As System.Double, _
   ByVal X1 As System.Double, _
   ByVal Y1 As System.Double, _
   ByVal Z1 As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim X0 As System.Double
Dim Y0 As System.Double
Dim Z0 As System.Double
Dim X1 As System.Double
Dim Y1 As System.Double
Dim Z1 As System.Double

instance.SplitClosedSegment(X0, Y0, Z0, X1, Y1, Z1)
```

### C#

```csharp
void SplitClosedSegment(
   System.double X0,
   System.double Y0,
   System.double Z0,
   System.double X1,
   System.double Y1,
   System.double Z1
)
```

### C++/CLI

```cpp
void SplitClosedSegment(
   System.double X0,
   System.double Y0,
   System.double Z0,
   System.double X1,
   System.double Y1,
   System.double Z1
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X0`: X value of first point
- `Y0`: Y value of first point
- `Z0`: Z value of first point
- `X1`: X value of second point
- `Y1`: Y value of second point
- `Z1`: Z value of second point

## VBA Syntax

See [ModelDoc2::SplitClosedSegment](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SplitClosedSegment.html).

## Remarks

The selected sketch segment must be a closed entity (for example, the start and end points must be the same). To split a closed sketch segment (for example, a complete circle) into two pieces, you must specify two points (x1, y1, z1) and (x2, y2, z2).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::SplitOpenSegment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SplitOpenSegment.html)
[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
