---
title: "CreateTangentArc2 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "CreateTangentArc2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateTangentArc2.html"
---

# CreateTangentArc2 Method (IModelDoc2)

Obsolete. Superseded by [ISketchManager::CreateTangentArc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~CreateTangentArc.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateTangentArc2( _
   ByVal P1x As System.Double, _
   ByVal P1y As System.Double, _
   ByVal P1z As System.Double, _
   ByVal P2x As System.Double, _
   ByVal P2y As System.Double, _
   ByVal P2z As System.Double, _
   ByVal ArcTypeIn As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim P1x As System.Double
Dim P1y As System.Double
Dim P1z As System.Double
Dim P2x As System.Double
Dim P2y As System.Double
Dim P2z As System.Double
Dim ArcTypeIn As System.Integer
Dim value As System.Boolean

value = instance.CreateTangentArc2(P1x, P1y, P1z, P2x, P2y, P2z, ArcTypeIn)
```

### C#

```csharp
System.bool CreateTangentArc2(
   System.double P1x,
   System.double P1y,
   System.double P1z,
   System.double P2x,
   System.double P2y,
   System.double P2z,
   System.int ArcTypeIn
)
```

### C++/CLI

```cpp
System.bool CreateTangentArc2(
   System.double P1x,
   System.double P1y,
   System.double P1z,
   System.double P2x,
   System.double P2y,
   System.double P2z,
   System.int ArcTypeIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `P1x`: x coordinate of start point in meters
- `P1y`: y coordinate of start point in meters
- `P1z`: Always 0
- `P2x`: x coordinate of end point in meters
- `P2y`: y coordinate of end point in meters
- `P2z`: Always 0
- `ArcTypeIn`: Type of tangent arc as defined in [swTangentArcTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTangentArcTypes_e.html)

### Return Value

1 = success, 0 = failure

## VBA Syntax

See [ModelDoc2::CreateTangentArc2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~CreateTangentArc2.html).

## Remarks

This method can only create 2D tangent arcs. Use [ISketchManager::CreateTangentArc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~CreateTangentArc.html) to create 3D tangent arcs.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::Create3PointArc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Create3PointArc.html)
[IModelDoc2::CreateArc2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateArc2.html)
[IModelDoc2::CreateArcByCenter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateArcByCenter.html)
[IModelDoc2::ICreateArc2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateArc2.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
