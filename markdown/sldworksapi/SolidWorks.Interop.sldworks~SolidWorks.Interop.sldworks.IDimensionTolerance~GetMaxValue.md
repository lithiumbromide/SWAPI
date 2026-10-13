---
title: "GetMaxValue Method (IDimensionTolerance)"
project: "SOLIDWORKS API Help"
interface: "IDimensionTolerance"
member: "GetMaxValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetMaxValue.html"
---

# GetMaxValue Method (IDimensionTolerance)

Obsolete. Superseded by [IDimensionTolerance::GetMaxValue2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetMaxValue2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMaxValue() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDimensionTolerance
Dim value As System.Double

value = instance.GetMaxValue()
```

### C#

```csharp
System.double GetMaxValue()
```

### C++/CLI

```cpp
System.double GetMaxValue();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Tolerance maximum value

## VBA Syntax

See [DimensionTolerance::GetMaxValue](ms-its:sldworksapivb6.chm::/sldworks~DimensionTolerance~GetMaxValue.html).

## Remarks

Depending on the [tolerance type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~Type.html), the tolerance minimum and maximum values might not be visible.

To:

- get the tolerance minimum value, use [IDimensionTolerance::GetMinValue](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~GetMinValue.html).
- set the tolerance values, use [IDimensionTolerance::SetValues](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~SetValues.html).

## See Also

[IDimensionTolerance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance.html)
[IDimensionTolerance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
