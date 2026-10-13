---
title: "ExtendSurface Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "ExtendSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ExtendSurface.html"
---

# ExtendSurface Method (IBody2)

Creates a new temporary body by extending the selected edges.

## Syntax

### Visual Basic (Declaration)

```vb
Function ExtendSurface( _
   ByVal EdgesToExtend As System.Object, _
   ByVal ExtendLinear As System.Boolean, _
   ByVal EndCondition As System.Integer, _
   ByVal Dist As System.Double, _
   ByVal PUpToVtx As Vertex, _
   ByVal PUpToFace As Face _
) As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim EdgesToExtend As System.Object
Dim ExtendLinear As System.Boolean
Dim EndCondition As System.Integer
Dim Dist As System.Double
Dim PUpToVtx As Vertex
Dim PUpToFace As Face
Dim value As Body2

value = instance.ExtendSurface(EdgesToExtend, ExtendLinear, EndCondition, Dist, PUpToVtx, PUpToFace)
```

### C#

```csharp
Body2 ExtendSurface(
   System.object EdgesToExtend,
   System.bool ExtendLinear,
   System.int EndCondition,
   System.double Dist,
   Vertex PUpToVtx,
   Face PUpToFace
)
```

### C++/CLI

```cpp
Body2^ ExtendSurface(
   System.Object^ EdgesToExtend,
   System.bool ExtendLinear,
   System.int EndCondition,
   System.double Dist,
   Vertex^ PUpToVtx,
   Face^ PUpToFace
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `EdgesToExtend`: Array of the selected edges to extend
- `ExtendLinear`: True to extend the selected edges linearly along the tangent of the face at the edges; false to extend the selected edges in the same direction as the face
- `EndCondition`: - 0 = Extend selected edges per value specified for Dist

  1 = Extend selected edges to PUpToVtx

  2 = Extend selected edges to PUpToFace
- `Dist`: Distance by which to extend the selected edges (see **Remarks**)
- `PUpToVtx`: [Vertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex.html) up to which to extend the selected edges (see Remarks)
- `PUpToFace`: [Face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) up to which to extend the selected edges (see Remarks)

### Return Value

Pointer to the newly created [IBody2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) object

## VBA Syntax

See [Body2::ExtendSurface](ms-its:sldworksapivb6.chm::/sldworks~Body2~ExtendSurface.html).

## Examples

[Extend Surface (VBA)](Extend_Surface_Example_VB.htm)

## Remarks

This method supports surface bodies only.

You can extend the edges by a specified distance or up to a vertex or up to a face.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::IExtendSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IExtendSurface.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
