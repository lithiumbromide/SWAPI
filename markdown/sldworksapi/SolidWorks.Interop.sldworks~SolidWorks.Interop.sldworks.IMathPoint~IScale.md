---
title: "IScale Method (IMathPoint)"
project: "SOLIDWORKS API Help"
interface: "IMathPoint"
member: "IScale"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~IScale.html"
---

# IScale Method (IMathPoint)

Scales a math point's magnitude.

## Syntax

### Visual Basic (Declaration)

```vb
Function IScale( _
   ByVal ValueIn As System.Double _
) As MathPoint
```

### Visual Basic (Usage)

```vb
Dim instance As IMathPoint
Dim ValueIn As System.Double
Dim value As MathPoint

value = instance.IScale(ValueIn)
```

### C#

```csharp
MathPoint IScale(
   System.double ValueIn
)
```

### C++/CLI

```cpp
MathPoint^ IScale(
   System.double ValueIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ValueIn`: Scale by which to multiply the magnitude of the math point

### Return Value

Newly created scaled [math point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) or NULL if the operation fails

## VBA Syntax

See [MathPoint::IScale](ms-its:sldworksapivb6.chm::/sldworks~MathPoint~IScale.html).

## See Also

[IMathPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.html)
[IMathPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint_members.html)
[IMathPoint::Scale Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~Scale.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
