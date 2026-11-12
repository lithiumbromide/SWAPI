---
title: "SetValues2 Method (IDimensionTolerance)"
project: "SOLIDWORKS API Help"
interface: "IDimensionTolerance"
member: "SetValues2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~SetValues2.html"
---

# SetValues2 Method (IDimensionTolerance)

Sets the tolerance minimum and maximum values of a [dimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimension.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetValues2( _
   ByVal MinValue As System.Double, _
   ByVal MaxValue As System.Double, _
   ByVal WhichConfigurations As System.Integer, _
   ByVal Config_names As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimensionTolerance
Dim MinValue As System.Double
Dim MaxValue As System.Double
Dim WhichConfigurations As System.Integer
Dim Config_names As System.Object
Dim value As System.Boolean

value = instance.SetValues2(MinValue, MaxValue, WhichConfigurations, Config_names)
```

### C#

```csharp
System.bool SetValues2(
   System.double MinValue,
   System.double MaxValue,
   System.int WhichConfigurations,
   System.object Config_names
)
```

### C++/CLI

```cpp
System.bool SetValues2(
   System.double MinValue,
   System.double MaxValue,
   System.int WhichConfigurations,
   System.Object^ Config_names
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `MinValue`: Dimension tolerance minimum value
- `MaxValue`: Dimension tolerance maximum value
- `WhichConfigurations`: Configurations to which to set the dimension tolerance minimum and maximum values as defined in [swSetValueInConfiguration_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSetValueInConfiguration_e.html)
- `Config_names`: Names of the configurations for which to set dimension tolerance values

### Return Value

True if the dimension tolerance values are set, false if not

## VBA Syntax

See [DimensionTolerance::SetValues2](ms-its:sldworksapivb6.chm::/sldworks~DimensionTolerance~SetValues2.html).

## Examples

[Change Dimension Tolerance in a Configuration (C#)](Change_Dimension_Tolerance_in_Configuration_Example_CSharp.htm)
[Change Dimension Tolerance in a Configuration (VB.NET)](Change_Dimension_Tolerance_in_Configuration_Example_VBNET.htm)
[Change Dimension Tolerance in a Configuration (VBA)](Change_Dimension_Tolerance_in_Configuration_Example_VB.htm)

## Remarks

You cannot set the dimension tolerance values if the [tolerance type](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~Type.html) is [swTolType_e.swTolNONE](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTolType_e.html). Depending on the tolerance type, the dimension tolerance minimum and maximum values might not be visible.

| To get the dimension tolerance... | Use... |
| --- | --- |
| Minimum value | IDimensionTolerance::GetMinValue |
| Maximum value | IDimensionTolerance::GetMaxValue |

To see the effects of changing the dimension tolerance values, call [IModelView::GraphicsRedraw](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~GraphicsRedraw.html).

## See Also

[IDimensionTolerance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance.html)
[IDimensionTolerance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance_members.html)

## Availability

SOLIDWORKS 2013 SP04, Revision Number 21.4
