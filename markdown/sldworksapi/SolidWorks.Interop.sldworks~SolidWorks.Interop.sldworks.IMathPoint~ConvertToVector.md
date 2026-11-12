---
title: "ConvertToVector Method (IMathPoint)"
project: "SOLIDWORKS API Help"
interface: "IMathPoint"
member: "ConvertToVector"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~ConvertToVector.html"
---

# ConvertToVector Method (IMathPoint)

Converts a math point to a math vector by using the three coordinates of the math point for the components of the math vector.

## Syntax

### Visual Basic (Declaration)

```vb
Function ConvertToVector() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMathPoint
Dim value As System.Object

value = instance.ConvertToVector()
```

### C#

```csharp
System.object ConvertToVector()
```

### C++/CLI

```cpp
System.Object^ ConvertToVector();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Newly created [math vector](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html) or NULL if the operation fails

## VBA Syntax

See [MathPoint::ConvertToVector](ms-its:sldworksapivb6.chm::/sldworks~MathPoint~ConvertToVector.html).

## See Also

[IMathPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.html)
[IMathPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint_members.html)
[IMathPoint::IConvertToVector Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~IConvertToVector.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
