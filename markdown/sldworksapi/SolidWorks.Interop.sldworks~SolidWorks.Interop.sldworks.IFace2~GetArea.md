---
title: "GetArea Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "GetArea"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetArea.html"
---

# GetArea Method (IFace2)

Gets the area of this face.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetArea() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim value As System.Double

value = instance.GetArea()
```

### C#

```csharp
System.double GetArea()
```

### C++/CLI

```cpp
System.double GetArea();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Face area in square meters (see **Remarks**)

## VBA Syntax

See [Face2::GetArea](ms-its:sldworksapivb6.chm::/sldworks~Face2~GetArea.html).

## Examples

[Find Outside Edges of Face (VBA)](Find_Outside_Edges_of_Face_Example_VB.htm)
[Sweep Planar Loop Along Vector (VBA)](Sweep_Planar_Loop_Along_Vector_Example_VB.htm)
[Get Areas of MidSurface Faces (C#)](Get_Areas_of_MidSurface_Faces_Example_CSharp.htm)
[Get Areas of MidSurface Faces (VB.NET)](Get_Areas_of_MidSurface_FAces_Example_VBNET.htm)
[Get Areas of MidSurface Faces (VBA)](Get_Areas_of_MidSurface_Faces_Example_VB.htm)

## Remarks

This method calculates and returns an approximate value. If your application requires a more accurate value for a face area, then use tessellation. See [IBody2::GetTessellation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~GetTessellation.html) and [ITessellation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITessellation.html) for details.

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
