---
title: "CreateTrimmedCurve Method (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "CreateTrimmedCurve"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~CreateTrimmedCurve.html"
---

# CreateTrimmedCurve Method (ICurve)

Obsolete. Superseded by [ICurve::CreateTrimmedCurve2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~CreateTrimmedCurve2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateTrimmedCurve( _
   ByVal X1 As System.Double, _
   ByVal Y1 As System.Double, _
   ByVal Z1 As System.Double, _
   ByVal X2 As System.Double, _
   ByVal Y2 As System.Double, _
   ByVal Z2 As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim X1 As System.Double
Dim Y1 As System.Double
Dim Z1 As System.Double
Dim X2 As System.Double
Dim Y2 As System.Double
Dim Z2 As System.Double
Dim value As System.Object

value = instance.CreateTrimmedCurve(X1, Y1, Z1, X2, Y2, Z2)
```

### C#

```csharp
System.object CreateTrimmedCurve(
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2
)
```

### C++/CLI

```cpp
System.Object^ CreateTrimmedCurve(
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X1`:
- `Y1`:
- `Z1`:
- `X2`:
- `Y2`:
- `Z2`:

## VBA Syntax

See [Curve::CreateTrimmedCurve](ms-its:sldworksapivb6.chm::/sldworks~Curve~CreateTrimmedCurve.html).

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html)
