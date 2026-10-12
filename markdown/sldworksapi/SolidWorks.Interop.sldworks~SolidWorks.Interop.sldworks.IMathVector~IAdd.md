---
title: "IAdd Method (IMathVector)"
project: "SOLIDWORKS API Help"
interface: "IMathVector"
member: "IAdd"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~IAdd.html"
---

# IAdd Method (IMathVector)

Adds this math vector with the specified math vector.

## Syntax

### Visual Basic (Declaration)

```vb
Function IAdd( _
   ByVal VectorObjIn As MathVector _
) As MathVector
```

### Visual Basic (Usage)

```vb
Dim instance As IMathVector
Dim VectorObjIn As MathVector
Dim value As MathVector

value = instance.IAdd(VectorObjIn)
```

### C#

```csharp
MathVector IAdd(
   MathVector VectorObjIn
)
```

### C++/CLI

```cpp
MathVector^ IAdd(
   MathVector^ VectorObjIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VectorObjIn`: [Math vector](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html) object to add to this math vector

### Return Value

Newly created [math vector](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html) object or NULL if the operation fails

## VBA Syntax

See [MathVector::IAdd](ms-its:sldworksapivb6.chm::/sldworks~MathVector~IAdd.html).

## See Also

[IMathVector Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.html)
[IMathVector Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector_members.html)
[MathVector::Add Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~Add.html)
[IMathVector::ISubtract Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~ISubtract.html)
[IMathVector::Subtract Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~Subtract.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
