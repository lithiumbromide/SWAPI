---
title: "SelectByRay Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SelectByRay"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SelectByRay.html"
---

# SelectByRay Method (IModelDoc2)

Obsolete. Superseded by [IModelDocExtension::SelectByRay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByRay.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SelectByRay( _
   ByVal DoubleInfoIn As System.Object, _
   ByVal TypeWanted As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim DoubleInfoIn As System.Object
Dim TypeWanted As System.Integer
Dim value As System.Boolean

value = instance.SelectByRay(DoubleInfoIn, TypeWanted)
```

### C#

```csharp
System.bool SelectByRay(
   System.object DoubleInfoIn,
   System.int TypeWanted
)
```

### C++/CLI

```cpp
System.bool SelectByRay(
   System.Object^ DoubleInfoIn,
   System.int TypeWanted
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DoubleInfoIn`: Array of 7 doubles: 3 for the start point of the ray, 3 for the direction of the ray, and 1 for the radius
- `TypeWanted`: Type of objects to select as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

### Return Value

True if a selection is made, false if not

## VBA Syntax

See [ModelDoc2::SelectByRay](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SelectByRay.html).

## Remarks

This method:

- Defines a cylindrical region of infinite length that begins at pointIn, runs parallel to VectorIn, and has a radius of RadiusIn. If you specified edge or vertex entities, then the first edge or vertex found within the selection cylinder is selected.
- Only selects entity objects, which include faces, edges, vertices, and so on. You cannot select sketch objects using this method.
- Does not support the selection of silhouette edges.

Only a single entity is selected within the distance radius regardless of multiple entities existing within that radius. For selecting face entities, RadiusIn is ignored and a cylinder of infinitely small radius is used.

Use model space view to determine the selection vector in a drawing.

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
[IModelDoc2::MultiSelectByRay Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~MultiSelectByRay.html)
[IModelDoc2::RayIntersections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~RayIntersections.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
