---
title: "ISubtractVector Method (IMathPoint)"
project: "SOLIDWORKS API Help"
interface: "IMathPoint"
member: "ISubtractVector"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~ISubtractVector.html"
---

# ISubtractVector Method (IMathPoint)

Gets a math point that describes the difference between a math vector's magnitude from the calling math point

## Syntax

### Visual Basic (Declaration)

```vb
Function ISubtractVector( _
   ByVal VectorObjIn As MathVector _
) As MathPoint
```

### Visual Basic (Usage)

```vb
Dim instance As IMathPoint
Dim VectorObjIn As MathVector
Dim value As MathPoint

value = instance.ISubtractVector(VectorObjIn)
```

### C#

```csharp
MathPoint ISubtractVector(
   MathVector VectorObjIn
)
```

### C++/CLI

```cpp
MathPoint^ ISubtractVector(
   MathVector^ VectorObjIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VectorObjIn`: [Math vector](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html) by which to subtract this math point

### Return Value

Newly created [math point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) or NULL if the operation fails

## VBA Syntax

See [MathPoint::ISubtractVector](ms-its:sldworksapivb6.chm::/sldworks~MathPoint~ISubtractVector.html).

## See Also

[IMathPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.html)
[IMathPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint_members.html)
[IMathPoint::SubtractVector Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~SubtractVector.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
