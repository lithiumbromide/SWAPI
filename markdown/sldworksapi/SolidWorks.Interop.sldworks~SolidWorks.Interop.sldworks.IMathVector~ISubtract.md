---
title: "ISubtract Method (IMathVector)"
project: "SOLIDWORKS API Help"
interface: "IMathVector"
member: "ISubtract"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~ISubtract.html"
---

# ISubtract Method (IMathVector)

Subtracts the specified math vector's magnitude from this math vector and returns a new math vector.

## Syntax

### Visual Basic (Declaration)

```vb
Function ISubtract( _
   ByVal VectorObjIn As MathVector _
) As MathVector
```

### Visual Basic (Usage)

```vb
Dim instance As IMathVector
Dim VectorObjIn As MathVector
Dim value As MathVector

value = instance.ISubtract(VectorObjIn)
```

### C#

```csharp
MathVector ISubtract(
   MathVector VectorObjIn
)
```

### C++/CLI

```cpp
MathVector^ ISubtract(
   MathVector^ VectorObjIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VectorObjIn`: [Math vector](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html) to subtract from this math vector

### Return Value

Newly created [math vector](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html) or NULL if the operation fails

## VBA Syntax

See [MathVector::ISubtract](ms-its:sldworksapivb6.chm::/sldworks~MathVector~ISubtract.html).

## See Also

[IMathVector Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.html)
[IMathVector Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector_members.html)
[IMathVector::Subtract Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~Subtract.html)
[IMathVector::Add Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~Add.html)
[IMathVector::IAdd Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~IAdd.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
