---
title: "CreateVector Method (IMathUtility)"
project: "SOLIDWORKS API Help"
interface: "IMathUtility"
member: "CreateVector"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility~CreateVector.html"
---

# CreateVector Method (IMathUtility)

Creates a math vector.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateVector( _
   ByVal ArrayDataIn As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMathUtility
Dim ArrayDataIn As System.Object
Dim value As System.Object

value = instance.CreateVector(ArrayDataIn)
```

### C#

```csharp
System.object CreateVector(
   System.object ArrayDataIn
)
```

### C++/CLI

```cpp
System.Object^ CreateVector(
   System.Object^ ArrayDataIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ArrayDataIn`: Array of doubles representing the x,y,z components of the vector

### Return Value

Newly created [math vector](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html) or NULL if the operation fails

## VBA Syntax

See [MathUtility::CreateVector](ms-its:sldworksapivb6.chm::/sldworks~MathUtility~CreateVector.html).

## Examples

[Create Temporary Extruded Body (VBA)](Create_Temporary_Extruded_Body_Example_VB.htm)
[Get Angle of Hole Not Normal to a Face (VBA)](Get_Angle_of_Hole_Not_Normal_to_a_Face_Example_VB.htm)
[Locate Apex of Conical Face (VBA)](Locate_Apex_of_Conical_Face_Example_VB.htm)
[Create Drag Arrow Manipulator (C#)](Create_Drag_Arrow_Manipulator_Example_CSharp.htm)
[Create Drag Arrow Manipulator (VB.NET)](Create_Drag_Arrow_Manipulator_Example_VBNET.htm)
[Create Drag Arrow Manipulator (VBA)](Create_Drag_Arrow_Manipulator_Example_VB.htm)

## See Also

[IMathUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility.html)
[IMathUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility_members.html)
[IMathUtility::ICreateVector Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility~ICreateVector.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
