---
title: "ICross Method (IMathVector)"
project: "SOLIDWORKS API Help"
interface: "IMathVector"
member: "ICross"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~ICross.html"
---

# ICross Method (IMathVector)

Gets the cross product between two math vectors.

## Syntax

### Visual Basic (Declaration)

```vb
Function ICross( _
   ByVal VectorObjIn As MathVector _
) As MathVector
```

### Visual Basic (Usage)

```vb
Dim instance As IMathVector
Dim VectorObjIn As MathVector
Dim value As MathVector

value = instance.ICross(VectorObjIn)
```

### C#

```csharp
MathVector ICross(
   MathVector VectorObjIn
)
```

### C++/CLI

```cpp
MathVector^ ICross(
   MathVector^ VectorObjIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VectorObjIn`: [Math vector](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html) to use to determine the cross product

### Return Value

Newly created [math vector](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html)

## VBA Syntax

See [MathVector::ICross](ms-its:sldworksapivb6.chm::/sldworks~MathVector~ICross.html).

## See Also

[IMathVector Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.html)
[IMathVector Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector_members.html)
[IMathVector::Cross Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~Cross.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
