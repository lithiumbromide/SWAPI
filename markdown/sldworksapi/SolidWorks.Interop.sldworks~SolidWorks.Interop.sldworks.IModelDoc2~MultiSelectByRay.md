---
title: "MultiSelectByRay Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "MultiSelectByRay"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~MultiSelectByRay.html"
---

# MultiSelectByRay Method (IModelDoc2)

Selects multiple objects of the specified type that are intersected by a ray from point (x,y,z in meters) in direction vector (x,y,z) within a distance radius.

## Syntax

### Visual Basic (Declaration)

```vb
Function MultiSelectByRay( _
   ByVal DoubleInfoIn As System.Object, _
   ByVal TypeWanted As System.Integer, _
   ByVal Append As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim DoubleInfoIn As System.Object
Dim TypeWanted As System.Integer
Dim Append As System.Boolean
Dim value As System.Boolean

value = instance.MultiSelectByRay(DoubleInfoIn, TypeWanted, Append)
```

### C#

```csharp
System.bool MultiSelectByRay(
   System.object DoubleInfoIn,
   System.int TypeWanted,
   System.bool Append
)
```

### C++/CLI

```cpp
System.bool MultiSelectByRay(
   System.Object^ DoubleInfoIn,
   System.int TypeWanted,
   System.bool Append
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DoubleInfoIn`: Array of 7 doubles:3 for the start point of the ray, 3 for the direction of the ray, and 1 for the radius
- `TypeWanted`: Type of objects to select as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)
- `Append`: True to append the selections to the current selection list, false to not

### Return Value

True if an object is selected, false if not

## VBA Syntax

See [ModelDoc2::MultiSelectByRay](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~MultiSelectByRay.html).

## Remarks

This method:

- Defines a cylindrical region of infinite length that begins at pointIn, runs parallel to VectorIn, and has a radius of RadiusIn. If you specified edges or vertices, then any edge or vertex found within the selection cylinder is selected.
- Selects only entity objects, which include faces, edges, and vertices. You cannot use this function to select [ISketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch.html) objects.

  When selecting face entities, RadiusIn is ignored and a cylinder of infinitely small radius is used.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::GetRayIntersectionsPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetRayIntersectionsPoints.html)
[IModelDoc2::GetRayIntersectionsTopology Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetRayIntersectionsTopology.html)
[IModelDoc2::IGetRayIntersectionsPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetRayIntersectionsPoints.html)
[IModelDoc2::IGetRayIntersectionsTopology Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetRayIntersectionsTopology.html)
[IModelDoc2::IMultiSelectByRay Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IMultiSelectByRay.html)
[IModelDoc2::IRayIntersections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IRayIntersections.html)
[IModelDoc2::ISelectByRay Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ISelectByRay.html)
[IModelDoc2::RayIntersections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~RayIntersections.html)
[IModelDoc2::SelectByRay Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SelectByRay.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
