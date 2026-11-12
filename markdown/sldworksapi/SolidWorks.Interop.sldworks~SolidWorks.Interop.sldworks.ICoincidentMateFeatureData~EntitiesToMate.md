---
title: "EntitiesToMate Property (ICoincidentMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICoincidentMateFeatureData"
member: "EntitiesToMate"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoincidentMateFeatureData~EntitiesToMate.html"
---

# EntitiesToMate Property (ICoincidentMateFeatureData)

Gets or sets the entities to mate in this coincident mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property EntitiesToMate As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICoincidentMateFeatureData
Dim value As System.Object

instance.EntitiesToMate = value

value = instance.EntitiesToMate
```

### C#

```csharp
System.object EntitiesToMate {get; set;}
```

### C++/CLI

```cpp
property System.Object^ EntitiesToMate {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of entities to mate (see **Remarks**)

## VBA Syntax

See [CoincidentMateFeatureData::EntitiesToMate](ms-its:sldworksapivb6.chm::/sldworks~CoincidentMateFeatureData~EntitiesToMate.html).

## Examples

See the [ICoincidentMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoincidentMateFeatureData.html) example.

## Remarks

Instead of specifying this property, you can use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html) to pre-select the entities to mate using Mark = 1. You can pre-select mate entities during mate creation, but not during mate editing.

Populate the array of this property by using either IModelDocExtension::SelectByID2 or [IModelDocExtension::SelectByRay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByRay.html) and [ISelectionMgr::GetSelectedObject6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject6.html).

Create coincident mates with the following mate entity combinations:

| Mate entity/Mate entity | IEdge (arc, circular edge) | ISurface , IFace2 (cone) | IFeature (coordinate system) | ICurve (arc, spline, helix) | ISurface, IFace2 (cylinder) | IFace2 (extrusion face, draft is not allowed) | IEdge, IRefAxis , ICenterLine , ISketchLine (line) | IEntity (coordinate system origin) | IRefPlane | IRefPoint , IVertex , ISketchPoint | ISurface, IFace2 (sphere) | ISurface |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IEdge (arc, circular edge) | ● | ● |  |  | ● |  |  |  | ● | ● |  |  |
| ISurface, IFace2 (cone) | ● | ● Both cones must be of the same half angle |  |  |  |  |  |  |  | ● |  |  |
| IFeature (coordinate system) |  |  | ● |  |  |  |  | ● |  |  |  |  |
| ICurve (arc, spline, helix) |  |  |  |  |  |  |  |  |  | ● |  |  |
| ISurface, IFace2 (cylinder) | ● |  |  |  |  |  | ● |  |  |  |  |  |
| IFace2 (extrusion face, draft is not allowed) |  |  |  |  |  |  |  |  |  | ● |  |  |
| IEdge, IRefAxis, ICenterLine, ISketchLine (line) |  |  |  |  | ● |  | ● |  | ● | ● |  |  |
| IEntity (coordinate system origin) |  |  | ● |  |  |  |  | ● |  |  |  |  |
| IRefPlane | ● |  |  |  |  |  | ● |  | ● | ● |  |  |
| IRefPoint, IVertex, ISketchPoint | ● | ● |  | ● | ● | ● | ● |  | ● | ● | ● | ● |
| ISurface, IFace2 (sphere) |  |  |  |  |  |  |  |  |  | ● |  |  |
| ISurface |  |  |  |  |  |  |  |  |  | ● |  |  |

After specifying the entities to mate, specify their [ICoincidentMateFeatureData::PickPoints](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoincidentMateFeatureData~PickPoints.html) to fully define the position of the mate.

## See Also

[ICoincidentMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoincidentMateFeatureData.html)
[ICoincidentMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoincidentMateFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
