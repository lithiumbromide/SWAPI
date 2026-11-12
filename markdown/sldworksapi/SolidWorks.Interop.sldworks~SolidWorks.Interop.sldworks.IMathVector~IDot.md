---
title: "IDot Method (IMathVector)"
project: "SOLIDWORKS API Help"
interface: "IMathVector"
member: "IDot"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~IDot.html"
---

# IDot Method (IMathVector)

Gets the value of the dot product between two math vectors.

## Syntax

### Visual Basic (Declaration)

```vb
Function IDot( _
   ByVal VectorObjIn As MathVector _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMathVector
Dim VectorObjIn As MathVector
Dim value As System.Double

value = instance.IDot(VectorObjIn)
```

### C#

```csharp
System.double IDot(
   MathVector VectorObjIn
)
```

### C++/CLI

```cpp
System.double IDot(
   MathVector^ VectorObjIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VectorObjIn`: [Math vector](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html) to use to determine the dot value

### Return Value

Value of the dot product

## VBA Syntax

See [MathVector::IDot](ms-its:sldworksapivb6.chm::/sldworks~MathVector~IDot.html).

## See Also

[IMathVector Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.html)
[IMathVector Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector_members.html)
[IMathVector::Dot Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~Dot.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
