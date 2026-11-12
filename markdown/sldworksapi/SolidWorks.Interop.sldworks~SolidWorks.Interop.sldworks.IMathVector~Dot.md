---
title: "Dot Method (IMathVector)"
project: "SOLIDWORKS API Help"
interface: "IMathVector"
member: "Dot"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~Dot.html"
---

# Dot Method (IMathVector)

Gets the value of the dot product between two math vectors.

## Syntax

### Visual Basic (Declaration)

```vb
Function Dot( _
   ByVal VectorObjIn As System.Object _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMathVector
Dim VectorObjIn As System.Object
Dim value As System.Double

value = instance.Dot(VectorObjIn)
```

### C#

```csharp
System.double Dot(
   System.object VectorObjIn
)
```

### C++/CLI

```cpp
System.double Dot(
   System.Object^ VectorObjIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VectorObjIn`: [Math vector](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html) to use to determine the dot value

### Return Value

Value of the dot product

## VBA Syntax

See [MathVector::Dot](ms-its:sldworksapivb6.chm::/sldworks~MathVector~Dot.html).

## Examples

[Get Angle of Hole Not Normal to Face (VBA)](Get_Angle_of_Hole_Not_Normal_to_a_Face_Example_VB.htm)

## See Also

[IMathVector Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.html)
[IMathVector Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector_members.html)
[IMathVector::IDot Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~IDot.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
