---
title: "TearEdges Property (ISurfaceFlattenFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceFlattenFeatureData"
member: "TearEdges"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData~TearEdges.html"
---

# TearEdges Property (ISurfaceFlattenFeatureData)

Gets or sets the tear edges for the relief cuts for this surface-flatten feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property TearEdges As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceFlattenFeatureData
Dim value As System.Object

instance.TearEdges = value

value = instance.TearEdges
```

### C#

```csharp
System.object TearEdges {get; set;}
```

### C++/CLI

```cpp
property System.Object^ TearEdges {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of entities that lie on the selected faces or surfaces to flatten (see **Remarks**)

## VBA Syntax

See [SurfaceFlattenFeatureData::TearEdges](ms-its:sldworksapivb6.chm::/sldworks~SurfaceFlattenFeatureData~TearEdges.html).

## Examples

[Get Data for Surface-flatten Feature (C#)](Get_Data_for_Surface_Flatten_Feature_Example_CSharp.htm)
[Get Data for Surface-flatten Feature (VB.NET)](Get_Data_for_Surface_Flatten_Feature_Example_VBNET.htm)
[Get Data for Surface-flatten Feature (VBA)](Get_Data_for_Surface_Flatten_Feature_Example_VB.htm)

## Remarks

Tear edges:

- indicate where to make relief cuts before flattening the surface. During flattening, regions of the flattened surface are stretched while other regions are compressed. Adding tear edges through regions of high stress can reduce these deformations, which increases the accuracy of the flattened surface.
- allow users to flatten closed surfaces, such as spheres or entire solid bodies, that would otherwise not be flattened. See the **Example** section.
- can be any of these types of selected entities:

  - edges,
  - reference curves, and
  - 2D/3D splines.
- must each intersect the face or surface being flattened while touching one boundary edge, which is an edge adjacent to exactly one face or surface.
- are only applied when [ISurfaceFlattenFeatureData::ShouldMakeTears](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData~ShouldMakeTears.html) is true.

The SOLIDWORKS API returns [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html) for the entities selected for the tear edges in a surface-flatten feature.

## See Also

[ISurfaceFlattenFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData.html)
[ISurfaceFlattenFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData_members.html)
[ISurfaceFlattenFeatureData::MapEdges Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData~MapEdges.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
