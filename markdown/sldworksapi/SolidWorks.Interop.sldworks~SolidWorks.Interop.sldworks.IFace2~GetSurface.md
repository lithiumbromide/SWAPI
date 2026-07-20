---
title: "GetSurface Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "GetSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetSurface.html"
---

# GetSurface Method (IFace2)

Gets the surface referenced by this face.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSurface() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim value As System.Object

value = instance.GetSurface()
```

### C#

```csharp
System.object GetSurface()
```

### C++/CLI

```cpp
System.Object^ GetSurface();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Return Value

Underlying[surface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface.html)for this face

## VBA Syntax

See

[Face2::GetSurface](ms-its:sldworksapivb6.chm::/sldworks~Face2~GetSurface.html)

.

## Examples

[Calculate Closest Distance Between Faces (VBA)](Calculate_Closest_Distance_Between_Faces_Example_VB.htm)

[Determine Type of Face (VBA)](Determine_Type_of_Face_Example_VB.htm)

[Get Intersecting Face and Edge (VBA)](Get_Intersecting_Face_and_Edge_Example_VB.htm)

[Get Intersecting Faces (VBA)](Get_Intersecting_Faces_Example_VB.htm)

[Get Parameters of Planar Surface (VBA)](Get_Parameters_of_Planar_Surface_Example_VB.htm)

[Get Parameters of Toroidal Surface (VBA)](Get_Parameters_of_Toroidal_Surface_Example_VB.htm)

[Get Surface Type (VBA)](Get_Surface_Type_Example_VB.htm)

[Select Tangent Faces (VBA)](Select_Tangent_Faces_Example_VB.htm)

[Fill Holes in Part (C#)](Fill_Holes_in_Part_Example_CSharp.htm)

[Fill Holes in Part (VB.NET)](Fill_Holes_in_Part_Example_VBNET.htm)

[Fill Holes in Part (VBA)](Fill_Holes_in_Part_Example_VB.htm)

[Select Edges of All Holes on Face (C#)](Select_Edges_of_All_Holes_on_Face_Example_CSharp.htm)

[Select Edges of All Holes on Face (VB.NET)](Select_Edges_of_All_Holes_on_Face_Example_VBNET.htm)

[Select Edges of All Holes on Face (VBA)](Select_Edges_of_All_Holes_on_Face_Example_VB.htm)

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)

[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)

[IFace2::IGetSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetSurface.html)

[IFace2::AttachSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~AttachSurface.html)

[IFace2::DetachSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~DetachSurface.html)

[IFace2::HasTextureCoordinates Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~HasTextureCoordinates.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
