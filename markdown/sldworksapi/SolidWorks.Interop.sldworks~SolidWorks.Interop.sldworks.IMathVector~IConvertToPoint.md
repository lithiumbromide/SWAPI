---
title: "IConvertToPoint Method (IMathVector)"
project: "SOLIDWORKS API Help"
interface: "IMathVector"
member: "IConvertToPoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~IConvertToPoint.html"
---

# IConvertToPoint Method (IMathVector)

Converts this math vector to a point by using the three components of the math vector to be the coordinates of a new math point.

## Syntax

### Visual Basic (Declaration)

```vb
Function IConvertToPoint() As MathPoint
```

### Visual Basic (Usage)

```vb
Dim instance As IMathVector
Dim value As MathPoint

value = instance.IConvertToPoint()
```

### C#

```csharp
MathPoint IConvertToPoint()
```

### C++/CLI

```cpp
MathPoint^ IConvertToPoint();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Newly created [IMathPoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) object or NULL if the operation fails

## VBA Syntax

See [MathVector::IConvertToPoint](ms-its:sldworksapivb6.chm::/sldworks~MathVector~IConvertToPoint.html).

## See Also

[IMathVector Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.html)
[IMathVector Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector_members.html)
[IMathVector::ConvertToPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~ConvertToPoint.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
