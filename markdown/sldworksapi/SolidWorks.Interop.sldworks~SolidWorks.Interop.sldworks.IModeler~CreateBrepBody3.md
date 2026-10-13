---
title: "CreateBrepBody3 Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "CreateBrepBody3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBrepBody3.html"
---

# CreateBrepBody3 Method (IModeler)

Creates a temporary body from BREP (boundary representation) data.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateBrepBody3( _
   ByVal Type As System.Integer, _
   ByVal NTopologies As System.Integer, _
   ByVal Topologies As System.Object, _
   ByVal EdgeToleranceArray As System.Object, _
   ByVal VertexToleranceArray As System.Object, _
   ByVal PointArray As System.Object, _
   ByVal CurveArray1 As System.Object, _
   ByVal CurveSurfaceArray1 As System.Object, _
   ByVal CurveArray2 As System.Object, _
   ByVal CurveSurfaceArray2 As System.Object, _
   ByVal SurfaceArray As System.Object, _
   ByVal NRelations As System.Integer, _
   ByVal Parents As System.Object, _
   ByVal Children As System.Object, _
   ByVal Senses As System.Object, _
   ByVal Option As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim Type As System.Integer
Dim NTopologies As System.Integer
Dim Topologies As System.Object
Dim EdgeToleranceArray As System.Object
Dim VertexToleranceArray As System.Object
Dim PointArray As System.Object
Dim CurveArray1 As System.Object
Dim CurveSurfaceArray1 As System.Object
Dim CurveArray2 As System.Object
Dim CurveSurfaceArray2 As System.Object
Dim SurfaceArray As System.Object
Dim NRelations As System.Integer
Dim Parents As System.Object
Dim Children As System.Object
Dim Senses As System.Object
Dim Option As System.Integer
Dim value As System.Object

value = instance.CreateBrepBody3(Type, NTopologies, Topologies, EdgeToleranceArray, VertexToleranceArray, PointArray, CurveArray1, CurveSurfaceArray1, CurveArray2, CurveSurfaceArray2, SurfaceArray, NRelations, Parents, Children, Senses, Option)
```

### C#

```csharp
System.object CreateBrepBody3(
   System.int Type,
   System.int NTopologies,
   System.object Topologies,
   System.object EdgeToleranceArray,
   System.object VertexToleranceArray,
   System.object PointArray,
   System.object CurveArray1,
   System.object CurveSurfaceArray1,
   System.object CurveArray2,
   System.object CurveSurfaceArray2,
   System.object SurfaceArray,
   System.int NRelations,
   System.object Parents,
   System.object Children,
   System.object Senses,
   System.int Option
)
```

### C++/CLI

```cpp
System.Object^ CreateBrepBody3(
   System.int Type,
   System.int NTopologies,
   System.Object^ Topologies,
   System.Object^ EdgeToleranceArray,
   System.Object^ VertexToleranceArray,
   System.Object^ PointArray,
   System.Object^ CurveArray1,
   System.Object^ CurveSurfaceArray1,
   System.Object^ CurveArray2,
   System.Object^ CurveSurfaceArray2,
   System.Object^ SurfaceArray,
   System.int NRelations,
   System.Object^ Parents,
   System.Object^ Children,
   System.Object^ Senses,
   System.int Option
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Type`: Type of body to create as defined in [swTopology_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTopology_e.html)
- `NTopologies`: Number of topological entities in the topologies argument
- `Topologies`: Array of topologies (see [swTopoEntity_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTopoEntity_e.html)), one for each topological entity
- `EdgeToleranceArray`: Array of tolerances for edges
- `VertexToleranceArray`: Array of tolerances for vertices
- `PointArray`: Array of coordinates of vertices (geometry for vertices)
- `CurveArray1`: Array of [curves](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html) (geometry for edges; 3D curve) and coedges (geometry for coedges; 2D curve)
- `CurveSurfaceArray1`: Array of [surfaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface.html) that lie on CurveArray1 2D curve
- `CurveArray2`: Array of [curves](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html) (geometry for edges; 3D curve) and array of coedges (geometry for coedges; 2D curve)
- `CurveSurfaceArray2`: Array of [surfaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface.html) that on lie on CurveArray2 2D curve
- `SurfaceArray`: Array of [surfaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface.html) (geometry for faces)
- `NRelations`: Number of 1-to-1 relationships between topological entities
- `Parents`: Array of parents, one in each relationship
- `Children`: Array of parents, one in each relationship
- `Senses`: Array of senses in which child is used by parent in the relationship
- `Option`: - 0 = Default

  1 = Repair and simplify body

  2 = Simplify body

### Return Value

[Body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

## VBA Syntax

See [Modeler::CreateBrepBody3](ms-its:sldworksapivb6.chm::/sldworks~Modeler~CreateBrepBody3.html).

## Remarks

The CurveArray1 and CurveArray2 must be paired with CurveSurfaceArray1 and CurveSurfaceArray2, respectively. Order is not important. The 2D curve has to be created in the direction of the loop.

If non-negative values are packed into the EdgeToleranceArray and VertexToleranceArray arrays, then tolerances are applied to the corresponding edges or vertices. These arrays should be the same size as CurveArray1 and PointArray, respectively. Otherwise, a default value of 1.0e-8 (modeler precision) is used.

NOTE: [IModeler::SetInitKnitGapWidth](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~SetInitKnitGapWidth.html) does not affect this method.

Useful methods for creating geometry for the topological entities are:

- [IBody2::CreatePlanarSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~CreatePlanarSurface.html) or [IBody2::ICreatePlanarSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ICreatePlanarSurface.html)
- [IBody2::AddProfileArc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~AddProfileArc.html) or [IBody2::IAddProfileArc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IAddProfileArc.html)
- [IBody2::AddProfileLine](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~AddProfileLine.html) or [IBody2::IAddProfileLine](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IAddProfileLine.html)
- [IBody2::CreateRevolutionSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~CreateRevolutionSurface.html) or [IBody2::ICreateRevolutionSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ICreateRevolutionSurface.html)

For example, to create a cone, find topological relationships and form relevant arrays. A complete solid cone consists of 8 topological entities:

There are 8 relations:

The topologies array:

| Index | Value |
| --- | --- |
| 0 | swTopoShell |
| 1 | swTopoFace |
| 2 | swTopoFace |
| 3 | swTopoLoop |
| 4 | swTopoEdge |
| 5 | swTopoLoop |
| 6 | swTopoLoop |
| 7 | swTopoVertex |

The set of arrays:

| index | parents | children | senses | relation |
| --- | --- | --- | --- | --- |
| 0 | 0 | 1 | 0 | shell to face |
| 1 | 0 | 2 | 0 | shell to face |
| 2 | 1 | 3 | 0 | face to loop |
| 3 | 3 | 4 | -1 | loop to edge |
| 4 | 2 | 5 | 0 | face to loop |
| 5 | 2 | 6 | 0 | face to loop |
| 6 | 5 | 4 | 1 | loop to edge |
| 7 | 6 | 7 | 0 | loop to vertex |

Values in the parents and children arrays correspond to the indices of the topology array.

Each face or edge created by IModeler::CreateBrepBody3 or [IModeler::ICreateBrepBody3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICreateBrepBody3.html) has an associated integer ID that is the same as the index to the input topologies. Use [IFace2::GetFaceId](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~GetFaceId.html) or [IEdge::GetId](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge~GetID.html) to get the associated integer ID.

Every shell should be a closed shell. Sheet bodies should have additional back faces to form a closed shell. When creating a sheet body, these extra back faces are retained in the result and should be removed using [IModeler::DeleteFacesFromSheetBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~DeleteFacesFromSheetBody.html) or [IModeler::IDeleteFacesFromSheetBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~IDeleteFacesFromSheetBody.html).

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::CreateBodiesFromSheets2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodiesFromSheets2.html)
[IModeler::CreateBodyFromBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromBox.html)
[IModeler::CreateBodyFromCone Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromCone.html)
[IModeler::CreateBodyFromCyl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromCyl.html)
[IModeler::CreateBodyFromFaces2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromFaces2.html)
[IModeler::CreateSweptBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSweptBody.html)
[IModeler::CreateWireBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateWireBody.html)
[IModeler::ICreateBodiesFromSheets2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodiesFromSheets2.html)
[IModeler::ICreateBodyFromBox2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromBox2.html)
[IModeler::ICreateBodyFromCone2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromCone2.html)
[IModeler::ICreateBodyFromCyl2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromCyl2.html)
[IModeler::ICreateBodyFromFaces3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromFaces3.html)
[IModeler::ICreateWireBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateWireBody.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
