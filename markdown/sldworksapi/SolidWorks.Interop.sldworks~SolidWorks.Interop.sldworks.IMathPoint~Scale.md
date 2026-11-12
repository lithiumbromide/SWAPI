---
title: "Scale Method (IMathPoint)"
project: "SOLIDWORKS API Help"
interface: "IMathPoint"
member: "Scale"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~Scale.html"
---

# Scale Method (IMathPoint)

Scales a math point's magnitude.

## Syntax

### Visual Basic (Declaration)

```vb
Function Scale( _
   ByVal ValueIn As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMathPoint
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

- `ValueIn`: Scale by which to multiply the magnitude of the math point

### Return Value

Newly created scaled [math point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) or NULL if the operation fails

## VBA Syntax

See [MathPoint::Scale](ms-its:sldworksapivb6.chm::/sldworks~MathPoint~Scale.html).

## See Also

[IMathPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.html)
[IMathPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint_members.html)
[IMathPoint::IScale Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~IScale.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
