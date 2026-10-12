---
title: "SelectByRay Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "SelectByRay"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByRay.html"
---

# SelectByRay Method (IModelDocExtension)

Selects the first entity of the specified type that is intersected by a ray that starts at the specified point and runs parallel to the specified direction vector within the specified radius.

## Syntax

### Visual Basic (Declaration)

```vb
Function SelectByRay( _
   ByVal WorldX As System.Double, _
   ByVal WorldY As System.Double, _
   ByVal WorldZ As System.Double, _
   ByVal RayVecX As System.Double, _
   ByVal RayVecY As System.Double, _
   ByVal RayVecZ As System.Double, _
   ByVal RayRadius As System.Double, _
   ByVal TypeWanted As System.Integer, _
   ByVal Append As System.Boolean, _
   ByVal Mark As System.Integer, _
   ByVal Option As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim WorldX As System.Double
Dim WorldY As System.Double
Dim WorldZ As System.Double
Dim RayVecX As System.Double
Dim RayVecY As System.Double
Dim RayVecZ As System.Double
Dim RayRadius As System.Double
Dim TypeWanted As System.Integer
Dim Append As System.Boolean
Dim Mark As System.Integer
Dim Option As System.Integer
Dim value As System.Boolean

value = instance.SelectByRay(WorldX, WorldY, WorldZ, RayVecX, RayVecY, RayVecZ, RayRadius, TypeWanted, Append, Mark, Option)
```

### C#

```csharp
System.bool SelectByRay(
   System.double WorldX,
   System.double WorldY,
   System.double WorldZ,
   System.double RayVecX,
   System.double RayVecY,
   System.double RayVecZ,
   System.double RayRadius,
   System.int TypeWanted,
   System.bool Append,
   System.int Mark,
   System.int Option
)
```

### C++/CLI

```cpp
System.bool SelectByRay(
   System.double WorldX,
   System.double WorldY,
   System.double WorldZ,
   System.double RayVecX,
   System.double RayVecY,
   System.double RayVecZ,
   System.double RayRadius,
   System.int TypeWanted,
   System.bool Append,
   System.int Mark,
   System.int Option
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WorldX`: x coordinate of ray start point
- `WorldY`: y coordinate of ray start point
- `WorldZ`: z coordinate of ray start point
- `RayVecX`: x coordinate of ray direction vector
- `RayVecY`: y coordinate of ray direction vector
- `RayVecZ`: z coordinate of ray direction vector
- `RayRadius`: Radius <= 2.9 m
- `TypeWanted`: Type of entities to select as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)
- `Append`:

  | If... | And if entity is... | Then... |
  | --- | --- | --- |
  | True | Not already selected | Entity is appended to the current selection list |
  |  | Already selected | Entity is removed from the current selection list |
  | False | Not already selected | Current selection is cleared and then the entity is put on the list |
  |  | Already selected | Current selection list remains the same |
- `Mark`: Value to use as a mark; this value is used by other functions that require ordered selection
- `Option`: Selection option as defined in [swSelectOption_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectOption_e.html) (see **Remarks**)

### Return Value

True if the entity is selected, false if not

## VBA Syntax

See [ModelDocExtension::SelectByRay](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~SelectByRay.html).

## Examples

[Select Face Using Intersecting Ray (C#)](Select_Face_Using_Intersecting_Ray_Example_CSharp.htm)
[Select Face Using Intersecting Ray (VB.NET)](Select_Face_Using_Intersecting_Ray_Example_VBNET.htm)
[Select Face Using Intersecting Ray (VBA)](Select_Face_Using_Intersecting_Ray_Example_VB.htm)

## Remarks

This method:

- Defines a cylindrical region of infinite length that starts at the specified point and runs parallel to the specified direction vector within the specified radius.
- Only selects these entities: faces, edges, and vertices.
- Does not support the selection of sketch entities, axes, center marks, center lines, section lines, etc.

Only a single entity is selected within the radius regardless if multiple entities existing within that radius. If selecting faces, then the RayRadius parameter is ignored and a cylinder of an infinitely small radius is used.

Use model space view to determine the selection vector in a drawing.

For the Option parameter, specify swSelectOption_e.swSelectOptionDefault to indicate that the Shift key is not used during selection or swSelectOption_e.swSelectOptionExtensive to indicate that the Shift key is used during selection.

**NOTES:**

- This method is recorded when [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html) relies on the selection coordinates and prone to failure if the model view is altered.
- The difference between this method and the now obsolete [IModelDoc2::SelectByRay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SelectByRay.html) method is that if you call IModelDocExtension::SelectByRay in a macro or application to select an entity by an intersecting ray and then rerun that macro or application, the original entity is successfully selected regardless of the viewing transform.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDoc2::GetRayIntersectionsPoints Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetRayIntersectionsPoints.html)
[IModelDoc2::GetRayIntersectionsTopology Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetRayIntersectionsTopology.html)
[IModelDoc2::MultiSelectByRay Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~MultiSelectByRay.html)
[IModelDoc2::RayIntersections Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~RayIntersections.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
