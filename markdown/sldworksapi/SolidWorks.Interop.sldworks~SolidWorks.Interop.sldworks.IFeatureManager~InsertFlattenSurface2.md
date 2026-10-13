---
title: "InsertFlattenSurface2 Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertFlattenSurface2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertFlattenSurface2.html"
---

# InsertFlattenSurface2 Method (IFeatureManager)

Inserts a surface-flatten feature in the model.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertFlattenSurface2( _
   ByVal AccuracyFactor As System.Integer, _
   ByVal ShouldUseTears As System.Boolean _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim AccuracyFactor As System.Integer
Dim ShouldUseTears As System.Boolean
Dim value As Feature

value = instance.InsertFlattenSurface2(AccuracyFactor, ShouldUseTears)
```

### C#

```csharp
Feature InsertFlattenSurface2(
   System.int AccuracyFactor,
   System.bool ShouldUseTears
)
```

### C++/CLI

```cpp
Feature^ InsertFlattenSurface2(
   System.int AccuracyFactor,
   System.bool ShouldUseTears
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AccuracyFactor`: 10 >= Accuracy of flattened triangle mesh >= 1; 1 is highest accuracy
- `ShouldUseTears`: True to use relief cuts, false to not

### Return Value

Surface-flatten [feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::InsertFlattenSurface2](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertFlattenSurface2.html).

## Examples

[Get Data for Surface-flatten Feature (C#)](Get_Data_for_Surface_Flatten_Feature_Example_CSharp.htm)
[Get Data for Surface-flatten Feature (VB.NET)](Get_Data_for_Surface_Flatten_Feature_Example_VBNET.htm)
[Get Data for Surface-flatten Feature (VBA)](Get_Data_for_Surface_Flatten_Feature_Example_VB.htm)

## Remarks

| Before calling this method, select... | By calling IModelDocExtension::SelectByID2 with Mark... |
| --- | --- |
| Faces or surfaces to flatten | 1 |
| Edges to guide the shape and length of the flattened surface | 2 |
| Map edges | 4 |
| Tear edges | 8 |
| Anchor point from which to flatten | 16 |

Map edges:

- are entities to map to the flattened surface. By default, any entity that lies on top of a face or surface to flatten is ignored unless the user selects the entity as a map edge.
- are useful when users want to see where a selected entity on the original body would lie on a flattened surface. For example, users might select edges as map lines to serve as bend lines in the flattened surface.
- can be any of these types of selected entities:

  - edges.
  - reference curves,
  - 2D/3D splines,
  - sketches, and
  - sketch text.

Tear edges:

- indicate where to make relief cuts before flattening the surface. During flattening, regions of the flattened surface are stretched while other regions are compressed. Adding tear edges through regions of high stress can reduce these deformations, which increases the accuracy of the flattened surface.
- allow users to flatten closed surfaces, such as spheres or entire solid bodies, that would otherwise not be flattened.
- can be any of these types of selected entities:

  - edges,
  - reference curves, and
  - 2D/3D splines.
- must each intersect the face or surface being flattened while touching one boundary edge, which is an edge adjacent to exactly one face or surface.
- are only applied when ShouldUseTears is true.

An anchor point can be a vertex or point on an edge.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[ISurfaceFlattenFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
