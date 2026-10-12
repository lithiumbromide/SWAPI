---
title: "FaceInSurfaceSense Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "FaceInSurfaceSense"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~FaceInSurfaceSense.html"
---

# FaceInSurfaceSense Method (IFace2)

Checks whether the face normal has the opposite direction (sense) as the underlying surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function FaceInSurfaceSense() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim value As System.Boolean

value = instance.FaceInSurfaceSense()
```

### C#

```csharp
System.bool FaceInSurfaceSense()
```

### C++/CLI

```cpp
System.bool FaceInSurfaceSense();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if face normal and surface normal are in the opposite direction, false if they are in same direction

## VBA Syntax

See [Face2::FaceInSurfaceSense](ms-its:sldworksapivb6.chm::/sldworks~Face2~FaceInSurfaceSense.html).

## Examples

[Determine Type of Face (VBA)](Determine_Type_of_Face_Example_VB.htm)
[Get Normal of Planar Surface (VBA)](Get_Normal_of_Planar_Surface_Example_VB.htm)
[Select Edges of All Holes on Face (C#)](Select_Edges_of_All_Holes_on_Face_Example_CSharp.htm)
[Select Edges of All Holes on Face (VB.NET)](Select_Edges_of_All_Holes_on_Face_Example_VBNET.htm)
[Select Edges of All Holes on Face (VBA)](Select_Edges_of_All_Holes_on_Face_Example_VB.htm)

## Remarks

Although the name of this method and its results are somewhat contradictory, the results are:

- True if face normal and surface normal are in the opposite direction.
- False if they are in the same direction.

You might need this method because the underlying surface geometry can have an orientation where its normal vector points toward or away from the body material. The normal vector of faces, however, are directed away from the body material.

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
