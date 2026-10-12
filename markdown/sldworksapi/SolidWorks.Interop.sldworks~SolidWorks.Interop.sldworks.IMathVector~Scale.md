---
title: "Scale Method (IMathVector)"
project: "SOLIDWORKS API Help"
interface: "IMathVector"
member: "Scale"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~Scale.html"
---

# Scale Method (IMathVector)

Scales this math vector's magnitude by a factor and returns a new math vector.

## Syntax

### Visual Basic (Declaration)

```vb
Function Scale( _
   ByVal ValueIn As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMathVector
Dim ValueIn As System.Double
Dim value As System.Object

value = instance.Scale(ValueIn)
```

### C#

```csharp
System.object Scale(
   System.double ValueIn
)
```

### C++/CLI

```cpp
System.Object^ Scale(
   System.double ValueIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ValueIn`: Value by which to scale the math vector

### Return Value

Newly created [math vector](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html) or NULL if the operation fails

## VBA Syntax

See [MathVector::Scale](ms-its:sldworksapivb6.chm::/sldworks~MathVector~Scale.html).

## See Also

[IMathVector Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.html)
[IMathVector Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector_members.html)
[IMathVector::IScale Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~IScale.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
