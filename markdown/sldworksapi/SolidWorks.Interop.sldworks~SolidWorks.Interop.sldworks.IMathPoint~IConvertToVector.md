---
title: "IConvertToVector Method (IMathPoint)"
project: "SOLIDWORKS API Help"
interface: "IMathPoint"
member: "IConvertToVector"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~IConvertToVector.html"
---

# IConvertToVector Method (IMathPoint)

Converts a math point to a math vector by using the three coordinates of the math point for the components of the math vector.

## Syntax

### Visual Basic (Declaration)

```vb
Function IConvertToVector() As MathVector
```

### Visual Basic (Usage)

```vb
Dim instance As IMathPoint
Dim value As MathVector

value = instance.IConvertToVector()
```

### C#

```csharp
MathVector IConvertToVector()
```

### C++/CLI

```cpp
MathVector^ IConvertToVector();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Newly created [math vector](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html) or NULL if the operation fails

## VBA Syntax

See [MathPoint::IConvertToVector](ms-its:sldworksapivb6.chm::/sldworks~MathPoint~IConvertToVector.html).

## See Also

[IMathPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.html)
[IMathPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint_members.html)
[IMathPoint::ConvertToVector Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~ConvertToVector.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
