---
title: "GetBaseCurve Method (ICurve)"
project: "SOLIDWORKS API Help"
interface: "ICurve"
member: "GetBaseCurve"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetBaseCurve.html"
---

# GetBaseCurve Method (ICurve)

Gets the base curve for this trimmed curve.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBaseCurve() As Curve
```

### Visual Basic (Usage)

```vb
Dim instance As ICurve
Dim value As Curve

value = instance.GetBaseCurve()
```

### C#

```csharp
Curve GetBaseCurve()
```

### C++/CLI

```cpp
Curve^ GetBaseCurve();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the [ICurve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html) object

## VBA Syntax

See [Curve::GetBaseCurve](ms-its:sldworksapivb6.chm::/sldworks~Curve~GetBaseCurve.html).

## Remarks

This method is a geometry function that applies only to SOLIDWORKS API applications.

## See Also

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.html)
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
