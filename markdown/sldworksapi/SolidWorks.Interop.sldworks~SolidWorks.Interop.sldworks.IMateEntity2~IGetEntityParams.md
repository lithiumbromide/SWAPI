---
title: "IGetEntityParams Method (IMateEntity2)"
project: "SOLIDWORKS API Help"
interface: "IMateEntity2"
member: "IGetEntityParams"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2~IGetEntityParams.html"
---

# IGetEntityParams Method (IMateEntity2)

Gets the parameters of this mate entity.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetEntityParams( _
   ByVal NParamsSize As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMateEntity2
Dim NParamsSize As System.Integer
Dim value As System.Double

value = instance.IGetEntityParams(NParamsSize)
```

### C#

```csharp
System.double IGetEntityParams(
   System.int NParamsSize
)
```

### C++/CLI

```cpp
System.double IGetEntityParams(
   System.int NParamsSize
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NParamsSize`: Number of parameters for this mate entity

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles representing the parameters for this mate entity (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [IMateEntity2::GetEntityParamsSize](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMateEntity2~GetEntityParamsSize.html) to get the value for the size of the array.

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
[IMateEntity2::EntityParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2~EntityParams.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number
