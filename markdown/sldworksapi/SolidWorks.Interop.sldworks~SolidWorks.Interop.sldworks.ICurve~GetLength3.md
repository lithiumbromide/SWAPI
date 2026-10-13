---
title: "GetLength3 Method (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "GetLength3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetLength3.html"
---

# GetLength3 Method (ICurve)

Gets the length of a curve between the specified parameters.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLength3( _
   ByVal StartParam As System.Double, _
   ByVal EndParam As System.Double _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim StartParam As System.Double
Dim EndParam As System.Double
Dim value As System.Double

value = instance.GetLength3(StartParam, EndParam)
```

### C#

```csharp
System.double GetLength3(
   System.double StartParam,
   System.double EndParam
)
```

### C++/CLI

```cpp
System.double GetLength3(
   System.double StartParam,
   System.double EndParam
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `StartParam`: Start parameter
- `EndParam`: End parameter

### Return Value

Length of the curve between the two parameters

## VBA Syntax

See [Curve::GetLength3](ms-its:sldworksapivb6.chm::/sldworks~Curve~GetLength3.html).

## Remarks

This method returns the length of the holding (e.g., trimmed) curve and not the base curve. The now obsolete [ICurve::Length2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~GetLength2.html) returned the length of the base curve.

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html)

## Availability

SOLIDWORKS 2008 SP1, Revision Number 16.1
