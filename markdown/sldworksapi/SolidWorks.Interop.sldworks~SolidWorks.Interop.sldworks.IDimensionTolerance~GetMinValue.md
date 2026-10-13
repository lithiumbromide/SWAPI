---
title: "GetMinValue Method (IDimensionTolerance)"
project: "SOLIDWORKS API Help"
interface: "IDimensionTolerance"
member: "GetMinValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetMinValue.html"
---

# GetMinValue Method (IDimensionTolerance)

Obsolete. Superseded by [IDimensionTolerance::GetMinValue2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetMinValue2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMinValue() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDimensionTolerance
Dim value As System.Double

value = instance.GetMinValue()
```

### C#

```csharp
System.double GetMinValue()
```

### C++/CLI

```cpp
System.double GetMinValue();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Tolerance minimum value

## VBA Syntax

See [DimensionTolerance::GetMinValue](ms-its:sldworksapivb6.chm::/sldworks~DimensionTolerance~GetMinValue.html).

## Remarks

Depending on the [tolerance type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~Type.html), the tolerance minimum and maximum values might not be visible.

To:

- get the tolerance maximum value, use [IDimensionTolerance::GetMaxValue](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~GetMaxValue.html).
- set the tolerance values, use [IDimensionTolerance::SetValues](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~SetValues.html).

## See Also

[IDimensionTolerance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance.html)
[IDimensionTolerance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
