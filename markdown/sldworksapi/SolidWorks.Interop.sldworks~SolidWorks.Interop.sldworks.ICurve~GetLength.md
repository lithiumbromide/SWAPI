---
title: "GetLength Method (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "GetLength"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetLength.html"
---

# GetLength Method (ICurve)

Obsolete. Superseded by [ICurve::GetLength2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~GetLength2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLength( _
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

value = instance.GetLength(StartParam, EndParam)
```

### C#

```csharp
System.double GetLength(
   System.double StartParam,
   System.double EndParam
)
```

### C++/CLI

```cpp
System.double GetLength(
   System.double StartParam,
   System.double EndParam
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `StartParam`:
- `EndParam`:

## VBA Syntax

See [Curve::GetLength](ms-its:sldworksapivb6.chm::/sldworks~Curve~GetLength.html).

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html)
