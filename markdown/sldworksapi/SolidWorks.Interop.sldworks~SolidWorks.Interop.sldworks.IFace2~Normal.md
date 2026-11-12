---
title: "Normal Property (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "Normal"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~Normal.html"
---

# Normal Property (IFace2)

Gets the unit normal vector for any planar face.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property Normal As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim value As System.Object

instance.Normal = value

value = instance.Normal
```

### C#

```csharp
System.object Normal {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Normal {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of 3 doubles (i,j,k)

## VBA Syntax

See [Face2::Normal](ms-its:sldworksapivb6.chm::/sldworks~Face2~Normal.html).

## Examples

[Get Normal of Planar Face (VBA)](Get_Normal_of_Planar_Face_Example_VB.htm)
[Get Normal of Planar Surface (VBA)](Get_Normal_of_Planar_Surface_Example_VB.htm)
[Get Plane or Face for Sketch (VBA)](Get_Plane_or_Face_for_Sketch_Example_VB.htm)

## Remarks

If the face is not a planar face, then this property returns 0,0,0.

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::INormal Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~INormal.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
