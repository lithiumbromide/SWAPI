---
title: "EntityParams Property (IMateEntity2)"
project: "SOLIDWORKS API Help"
interface: "IMateEntity2"
member: "EntityParams"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2~EntityParams.html"
---

# EntityParams Property (IMateEntity2)

Gets the parameters for this mate entity.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property EntityParams As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMateEntity2
Dim value As System.Object

value = instance.EntityParams
```

### C#

```csharp
System.object EntityParams {get;}
```

### C++/CLI

```cpp
property System.Object^ EntityParams {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of doubles representing the mate entity parameters (see **Remarks**)

## VBA Syntax

See [MateEntity2::EntityParams](ms-its:sldworksapivb6.chm::/sldworks~MateEntity2~EntityParams.html).

## Examples

[Edit Mate (VBA)](Edit_Mate_Example_VB.htm)
[Get Mate Definition (VBA)](Get_Mate_Definition_Example_VB.htm)
[Get Mates and Mate Entities (C#)](Get_Mates_and_Mate_Entities_Example_CSharp.htm)
[Get Mates and Mate Entities (VB.NET)](Get_Mates_and_Mate_Entities_Example_VBNET.htm)
[Get Mates and Mate Entities (VBA)](Get_Mates_and_Mate_Entities_Example_VB.htm)

## Remarks

The return value is the following array of doubles:

[ pointX, pointY, pointZ, vectorI, vectorJ, vectorK, radius1, radius2 ]

where

- pointX is the X location of this mate entity in the assembly model space
- pointY is the Y location of this mate entity in the assembly model space
- pointZ is the Z location of this mate entity in the assembly model space
- vectorI is the i component of the assembly mate vector
- vectorJ is the j component of the assembly mate vector
- vectorK is the k component of the assembly mate vector
- radius1 is the value for the first radius
- radius2 is the value for the second radius

To define the mate entity, the following information is returned based on the mate type. All coordinate information is given in terms of the assembly coordinate system where the mate resides.

| Mate Type | Returned |
| --- | --- |
| swMatePoint | pointX, pointY, pointZ |
| swMateLine | pointX, pointY, pointZ, vectorI, vectorJ, vectorK where the point is a point on the line and the vector represents the line direction. |
| swMatePlane | pointX, pointY, pointZ, vectorI, vectorJ, vectorK where the point is a point on the plane and the vector represents the plane normal. |
| swMateCylinder | pointX, pointY, pointZ, vectorI, vectorJ, vectorK, radius1 where the point is a point on the cylinder axis and the vector represents the cylinder axis. |
| swMateCone | pointX, pointY, pointZ, vectorI, vectorJ, vectorK, radius1, radius2 where the point is a point on the cone axis and the vector represents the cone axis. |

To get the [IMateEntity2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMateEntity2.html) interface, use [IMate2::MateEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMate2~MateEntity.html).

## See Also

[IMateEntity2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2.html)
[IMateEntity2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2_members.html)
[IMateEntity2::GetEntityParamsSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2~GetEntityParamsSize.html)
[IMateEntity2::IGetEntityParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2~IGetEntityParams.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
