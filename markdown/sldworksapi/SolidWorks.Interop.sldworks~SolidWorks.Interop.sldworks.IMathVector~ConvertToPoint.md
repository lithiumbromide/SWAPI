---
title: "ConvertToPoint Method (IMathVector)"
project: "SOLIDWORKS API Help"
interface: "IMathVector"
member: "ConvertToPoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~ConvertToPoint.html"
---

# ConvertToPoint Method (IMathVector)

Converts this math vector to a point by using the three components of the math vector to be the coordinates of a new math point.

## Syntax

### Visual Basic (Declaration)

```vb
Function ConvertToPoint() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMathVector
Dim value As System.Object

value = instance.ConvertToPoint()
```

### C#

```csharp
System.object ConvertToPoint()
```

### C++/CLI

```cpp
System.Object^ ConvertToPoint();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Newly created [IMathPoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) object or NULL if the operation fails

## VBA Syntax

See [MathVector::ConvertToPoint](ms-its:sldworksapivb6.chm::/sldworks~MathVector~ConvertToPoint.html).

## See Also

[IMathVector Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.html)
[IMathVector Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector_members.html)
[IMathVector::IConvertToPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~IConvertToPoint.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
