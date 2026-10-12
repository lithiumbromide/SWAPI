---
title: "SetValues Method (IDimensionTolerance)"
project: "SOLIDWORKS API Help"
interface: "IDimensionTolerance"
member: "SetValues"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~SetValues.html"
---

# SetValues Method (IDimensionTolerance)

Obsolete. Superseded by [IDimensionTolerance::SetValues2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~SetValues2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetValues( _
   ByVal MinValue As System.Double, _
   ByVal MaxValue As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimensionTolerance
Dim MinValue As System.Double
Dim MaxValue As System.Double
Dim value As System.Boolean

value = instance.SetValues(MinValue, MaxValue)
```

### C#

```csharp
System.bool SetValues(
   System.double MinValue,
   System.double MaxValue
)
```

### C++/CLI

```cpp
System.bool SetValues(
   System.double MinValue,
   System.double MaxValue
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `MinValue`: Tolerance minimum value
- `MaxValue`: Tolerance maximum value

### Return Value

True if the minimum and maximum tolerance values are set, false if not

## VBA Syntax

See [DimensionTolerance::SetValues](ms-its:sldworksapivb6.chm::/sldworks~DimensionTolerance~SetValues.html).

## Remarks

You cannot set the dimension tolerance values if the [tolerance type](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~Type.html) is [swTolType_e.swTolNONE](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTolType_e.html). Depending on the tolerance type, the dimension tolerance minimum and maximum values might not be visible.

| To get tolerance... | Use... |
| --- | --- |
| Minimum value | IDimensionTolerance::GetMinValue |
| Maximum value | IDimensionTolerance::GetMaxValue |

To see the effects of changing the tolerance values, call [IModelDoc2::GraphicsRedraw2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GraphicsRedraw2.html).

## See Also

[IDimensionTolerance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance.html)
[IDimensionTolerance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
