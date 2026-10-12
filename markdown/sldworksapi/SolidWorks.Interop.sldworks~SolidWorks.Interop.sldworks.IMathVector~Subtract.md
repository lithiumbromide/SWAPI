---
title: "Subtract Method (IMathVector)"
project: "SOLIDWORKS API Help"
interface: "IMathVector"
member: "Subtract"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~Subtract.html"
---

# Subtract Method (IMathVector)

Subtracts the specified math vector's magnitude from this math vector and returns a new math vector.

## Syntax

### Visual Basic (Declaration)

```vb
Function Subtract( _
   ByVal VectorObjIn As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMathVector
Dim VectorObjIn As System.Object
Dim value As System.Object

value = instance.Subtract(VectorObjIn)
```

### C#

```csharp
System.object Subtract(
   System.object VectorObjIn
)
```

### C++/CLI

```cpp
System.Object^ Subtract(
   System.Object^ VectorObjIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VectorObjIn`: [Math vector](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html) to subtract from this math vector

### Return Value

Newly created [math vector](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html) or NULL if the operation fails

## VBA Syntax

See [MathVector::Subtract](ms-its:sldworksapivb6.chm::/sldworks~MathVector~Subtract.html).

## See Also

[IMathVector Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.html)
[IMathVector Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector_members.html)
[IMathVector::ISubtract Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~ISubtract.html)
[IMathVector::Add Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~Add.html)
[IMathVector::IAdd Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~IAdd.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
