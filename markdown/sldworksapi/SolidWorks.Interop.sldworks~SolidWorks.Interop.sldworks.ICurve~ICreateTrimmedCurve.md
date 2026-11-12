---
title: "ICreateTrimmedCurve Method (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "ICreateTrimmedCurve"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ICreateTrimmedCurve.html"
---

# ICreateTrimmedCurve Method (ICurve)

Obsolete. Superseded by [ICurve::CreateTrimmedCurve2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve~CreateTrimmedCurve2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateTrimmedCurve( _
   ByRef Start As System.Double, _
   ByRef End As System.Double _
) As Curve
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim Start As System.Double
Dim End As System.Double
Dim value As Curve

value = instance.ICreateTrimmedCurve(Start, End)
```

### C#

```csharp
Curve ICreateTrimmedCurve(
   ref System.double Start,
   ref System.double End
)
```

### C++/CLI

```cpp
Curve^ ICreateTrimmedCurve(
   System.double% Start,
   System.double% End
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Start`:
- `End`:

## VBA Syntax

See [Curve::ICreateTrimmedCurve](ms-its:sldworksapivb6.chm::/sldworks~Curve~ICreateTrimmedCurve.html).

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html)
