---
title: "MapEdges Property (ISurfaceFlattenFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceFlattenFeatureData"
member: "MapEdges"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData~MapEdges.html"
---

# MapEdges Property (ISurfaceFlattenFeatureData)

Gets or sets the map edges for this surface-flatten feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property MapEdges As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceFlattenFeatureData
Dim value As System.Object

instance.MapEdges = value

value = instance.MapEdges
```

### C#

```csharp
System.object MapEdges {get; set;}
```

### C++/CLI

```cpp
property System.Object^ MapEdges {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of entities that lie on the selected faces or surfaces to flatten (see **Remarks**)

## VBA Syntax

See [SurfaceFlattenFeatureData::MapEdges](ms-its:sldworksapivb6.chm::/sldworks~SurfaceFlattenFeatureData~MapEdges.html).

## Remarks

Map edges:

- are entities to map to the flattened surface. By default, any entity that lies on top of a face or surface to flatten is ignored unless the user selects the entity as a map edge.
- are useful when users want to see where a selected entity on the original body would lie on a flattened surface. For example, users might select edges as map lines to serve as bend lines in the flattened surface.
- can be any of these types of selected entities:

  - edges,
  - reference curves,
  - 2D/3D splines,
  - sketches, and
  - sketch text.

The SOLIDWORKS API returns [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html) for the entities selected for the map edges in a surface-flatten feature.

## See Also

[ISurfaceFlattenFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData.html)
[ISurfaceFlattenFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData_members.html)
[ISurfaceFlattenFeatureData::TearEdges Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData~TearEdges.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
