---
title: "IScale Method (IMathVector)"
project: "SOLIDWORKS API Help"
interface: "IMathVector"
member: "IScale"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~IScale.html"
---

# IScale Method (IMathVector)

Scales this math vector's magnitude by a factor and returns a new math vector.

## Syntax

### Visual Basic (Declaration)

```vb
Function IScale( _
   ByVal ValueIn As System.Double _
) As MathVector
```

### Visual Basic (Usage)

```vb
Dim instance As IMathVector
Dim ValueIn As System.Double
Dim value As MathVector

value = instance.IScale(ValueIn)
```

### C#

```csharp
MathVector IScale(
   System.double ValueIn
)
```

### C++/CLI

```cpp
MathVector^ IScale(
   System.double ValueIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ValueIn`: Value by which to scale the math vector

### Return Value

Newly created [math vector](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html) or NULL if the operation fails

## VBA Syntax

See [MathVector::IScale](ms-its:sldworksapivb6.chm::/sldworks~MathVector~IScale.html).

## See Also

[IMathVector Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.html)
[IMathVector Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector_members.html)
[IMathVector::Scale Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~Scale.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
