---
title: "Add Method (IMathVector)"
project: "SOLIDWORKS API Help"
interface: "IMathVector"
member: "Add"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~Add.html"
---

# Add Method (IMathVector)

Adds this math vector with the specified math vector.

## Syntax

### Visual Basic (Declaration)

```vb
Function Add( _
   ByVal VectorObjIn As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMathVector
Dim VectorObjIn As System.Object
Dim value As System.Object

value = instance.Add(VectorObjIn)
```

### C#

```csharp
System.object Add(
   System.object VectorObjIn
)
```

### C++/CLI

```cpp
System.Object^ Add(
   System.Object^ VectorObjIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VectorObjIn`: [Math vector](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html) object to add to this math vector

### Return Value

Newly created [math vector](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html) object or NULL if the operation fails

## VBA Syntax

See [MathVector::Add](ms-its:sldworksapivb6.chm::/sldworks~MathVector~Add.html).

## See Also

[IMathVector Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.html)
[IMathVector Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector_members.html)
[IMathVector::IAdd Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~IAdd.html)
[IMathVector::Subtract Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~Subtract.html)
[IMathVector::ISubtract Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~ISubtract.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
