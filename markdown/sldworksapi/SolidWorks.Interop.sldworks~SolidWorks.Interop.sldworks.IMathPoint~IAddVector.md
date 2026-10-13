---
title: "IAddVector Method (IMathPoint)"
project: "SOLIDWORKS API Help"
interface: "IMathPoint"
member: "IAddVector"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~IAddVector.html"
---

# IAddVector Method (IMathPoint)

Translates a math point by a math vector to create a new math point.

## Syntax

### Visual Basic (Declaration)

```vb
Function IAddVector( _
   ByVal VectorObjIn As MathVector _
) As MathPoint
```

### Visual Basic (Usage)

```vb
Dim instance As IMathPoint
Dim VectorObjIn As MathVector
Dim value As MathPoint

value = instance.IAddVector(VectorObjIn)
```

### C#

```csharp
MathPoint IAddVector(
   MathVector VectorObjIn
)
```

### C++/CLI

```cpp
MathPoint^ IAddVector(
   MathVector^ VectorObjIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VectorObjIn`: [Math vector](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html) by which to translate this math point

### Return Value

Newly created translated [math point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) or NULL if the operation fails

## VBA Syntax

See [MathPoint::IAddVector](ms-its:sldworksapivb6.chm::/sldworks~MathPoint~IAddVector.html).

## See Also

[IMathPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.html)
[IMathPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint_members.html)
[IMathPoint::AddVector Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~AddVector.html)
[IMathPoint::SubtractVector Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~SubtractVector.html)
[IMathPoint::ISubtractVector Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~ISubtractVector.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
