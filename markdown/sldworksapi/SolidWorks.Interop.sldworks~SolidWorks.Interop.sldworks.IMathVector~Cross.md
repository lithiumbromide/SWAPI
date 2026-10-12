---
title: "Cross Method (IMathVector)"
project: "SOLIDWORKS API Help"
interface: "IMathVector"
member: "Cross"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~Cross.html"
---

# Cross Method (IMathVector)

Gets the cross product between two math vectors.

## Syntax

### Visual Basic (Declaration)

```vb
Function Cross( _
   ByVal VectorObjIn As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMathVector
Dim VectorObjIn As System.Object
Dim value As System.Object

value = instance.Cross(VectorObjIn)
```

### C#

```csharp
System.object Cross(
   System.object VectorObjIn
)
```

### C++/CLI

```cpp
System.Object^ Cross(
   System.Object^ VectorObjIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VectorObjIn`: [Math vector](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html) to use to determine the cross product

### Return Value

Newly created [math vector](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html)

## VBA Syntax

See [MathVector::Cross](ms-its:sldworksapivb6.chm::/sldworks~MathVector~Cross.html).

## Examples

[Get Angle Between Plane and Line (VBA)](Get_Angle_Between_Plane_and_Line_Example_VB.htm)

## See Also

[IMathVector Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.html)
[IMathVector Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector_members.html)
[IMathVector::ICross Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~ICross.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
