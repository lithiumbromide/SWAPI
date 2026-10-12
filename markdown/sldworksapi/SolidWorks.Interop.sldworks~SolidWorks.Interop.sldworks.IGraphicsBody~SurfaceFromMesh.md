---
title: "SurfaceFromMesh Method (IGraphicsBody)"
project: "SOLIDWORKS API Help"
interface: "IGraphicsBody"
member: "SurfaceFromMesh"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGraphicsBody~SurfaceFromMesh.html"
---

# SurfaceFromMesh Method (IGraphicsBody)

Creates a surface from the selected facets in this graphics body.

## Syntax

### Visual Basic (Declaration)

```vb
Function SurfaceFromMesh( _
   ByVal SurfaceType As System.Integer, _
   ByVal FacetTolerance As System.Double, _
   ByVal ExtendSurfaceSize As System.Double, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IGraphicsBody
Dim SurfaceType As System.Integer
Dim FacetTolerance As System.Double
Dim ExtendSurfaceSize As System.Double
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.SurfaceFromMesh(SurfaceType, FacetTolerance, ExtendSurfaceSize, ErrorCode)
```

### C#

```csharp
System.object SurfaceFromMesh(
   System.int SurfaceType,
   System.double FacetTolerance,
   System.double ExtendSurfaceSize,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ SurfaceFromMesh(
   System.int SurfaceType,
   System.double FacetTolerance,
   System.double ExtendSurfaceSize,
   [Out] System.int ErrorCode
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SurfaceType`: Type of surface to create as defined by [swSurfaceTypes_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSurfaceTypes_e.html) (see **Remarks**)
- `FacetTolerance`: 0.0 (High tolerance) <= Percent facet selection <= 100.0 (Low tolerance)
- `ExtendSurfaceSize`: Extension in meters of the surface body to fit the selected facets and geometric shape
- `ErrorCode`: 0 if successful, -1 if not

### Return Value

[IBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)

## VBA Syntax

See [GraphicsBody::SurfaceFromMesh](ms-its:sldworksapivb6.chm::/sldworks~GraphicsBody~SurfaceFromMesh.html).

## Examples

See the [IBody2::ConvertToMeshBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ConvertToMeshBody.html) examples.

## Remarks

This method:

- is analogous to the **Insert menu > Mesh > Surface From Mesh** functionality in the user interface.
- creates a **Surface-From-Mesh**`X` feature in the FeatureManager design tree.

Before calling this method, select as many facets in the graphics body as are needed to create the surface type.

SurfaceType can be one of only swSurfaceTypes_e.:

- PLANE_TYPE
- SPHERE_TYPE
- CYLINDER_TYPE
- CONE_TYPE

For more information, see the **SOLIDWORKS Design user-interface help > Parts and Features > Graphics Mesh and Mesh BREP Bodies > Creating a Surface from Mesh Featur**e topic.

## See Also

[IGraphicsBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGraphicsBody.html)
[IGraphicsBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGraphicsBody_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
