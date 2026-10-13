---
title: "RayIntersections Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "RayIntersections"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RayIntersections.html"
---

# RayIntersections Method (IModelDocExtension)

Finds the intersections between the specified set of rays and the specified set of bodies.

## Syntax

### Visual Basic (Declaration)

```vb
Function RayIntersections( _
   ByVal BodiesIn As System.Object, _
   ByVal BasePointsIn As System.Object, _
   ByVal VectorsIn As System.Object, _
   ByVal Options As System.Integer, _
   ByVal HitRadius As System.Double, _
   ByVal Offset As System.Double, _
   ByVal HighPrecision As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim BodiesIn As System.Object
Dim BasePointsIn As System.Object
Dim VectorsIn As System.Object
Dim Options As System.Integer
Dim HitRadius As System.Double
Dim Offset As System.Double
Dim HighPrecision As System.Boolean
Dim value As System.Integer

value = instance.RayIntersections(BodiesIn, BasePointsIn, VectorsIn, Options, HitRadius, Offset, HighPrecision)
```

### C#

```csharp
System.int RayIntersections(
   System.object BodiesIn,
   System.object BasePointsIn,
   System.object VectorsIn,
   System.int Options,
   System.double HitRadius,
   System.double Offset,
   System.bool HighPrecision
)
```

### C++/CLI

```cpp
System.int RayIntersections(
   System.Object^ BodiesIn,
   System.Object^ BasePointsIn,
   System.Object^ VectorsIn,
   System.int Options,
   System.double HitRadius,
   System.double Offset,
   System.bool HighPrecision
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BodiesIn`: Array of [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) that are hit by the rays (see **Remarks**)
- `BasePointsIn`: Array of doubles containing the x,y,z base points of each ray
- `VectorsIn`: Array of doubles containing the direction vectors of each ray
- `Options`: Options as defined in [swRayPtsOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRayPtsOpts_e.html) (see **Remarks**)
- `HitRadius`: Radius of hit cylinder; this is used mainly in grazing cases to establish a hit (see **Remarks**)
- `Offset`: Length tolerance to use to establish whether a hit on a face represents the entry or exit of the ray from the body (see Remarks)
- `HighPrecision`: True to use maximum precision when evaluating intersections close to the ray boundary, false to use dynamic precision based on the ray radius (see **Remarks**)

### Return Value

Number of intersections

## VBA Syntax

See [ModelDocExtension::RayIntersections](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~RayIntersections.html).

## Remarks

The method performs intersection operations between the specified bodies and the specified ray vectors. To get the results (a set of intersection points, intersection normals, and the bodies from your BodiesIn array that were hit), you must call [IModelDoc2::GetRayIntersectionsPoints](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetRayIntersectionsPoints.html) and [IModelDoc2::GetRayIntersectionTopology](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetRayIntersectionsTopology.html).

Information returned by IModelDoc2::GetRayIntersectionsPoints and IModelDoc2::GetRayIntersectionTopology depends partially on the value of the Options parameter. Valid Option values can be combined using bitwise operations. See IModelDoc2::GetRayIntersectionsPoints to determine which data is always output regardless of the values specified by Options.

For each ray that hits an edge or a vertex, the Offset value is added in both the positive and negative directions along the ray, and the points computed are tested for spatial inclusion in the hit body. This determines whether the ray was entering, leaving, or just grazing the body at the hit point. Entry and exit for faces can be computed and does not require an offset.

The difference between this method and the now obsolete IModelDoc2::RayIntersections and IModelDoc2::IRayIntersections is the HighPrecision parameter. Setting HighPrecision to true forces use of the highest possible precision when evaluating intersections close to ray profile boundaries. Setting HighPrecision to false forces use of a dynamic tolerance that is based on the HitRadius, which is the behavior of the obsolete methods.

The actual ray profile is polygonal, approximating an ideal circular ray profile of HitRadius. Evaluating intersections very close to the ray profile boundary may produce unexpected results due to this polygonal approximation. Experimentation with HighPrecision is recommended.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDoc2::MultiSelectByRay Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~MultiSelectByRay.html)
[IModelDoc2::SelectByRay Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SelectByRay.html)

## Availability

SOLIDWORKS 2018 SP02, Revision Number 26.2
