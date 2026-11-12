---
title: "Normalise Method (IMathVector)"
project: "SOLIDWORKS API Help"
interface: "IMathVector"
member: "Normalise"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~Normalise.html"
---

# Normalise Method (IMathVector)

Gets the unit-length vector for this math vector.

## Syntax

### Visual Basic (Declaration)

```vb
Function Normalise() As MathVector
```

### Visual Basic (Usage)

```vb
Dim instance As IMathVector
Dim value As MathVector

value = instance.Normalise()
```

### C#

```csharp
MathVector Normalise()
```

### C++/CLI

```cpp
MathVector^ Normalise();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Unit-length vector

## VBA Syntax

See [MathVector::Normalise](ms-its:sldworksapivb6.chm::/sldworks~MathVector~Normalise.html).

## See Also

[IMathVector Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.html)
[IMathVector Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector_members.html)

## Availability

SOLIDWORKS 2001Plus SP2, Revision Number 10.2
