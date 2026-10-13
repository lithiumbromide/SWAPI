---
title: "SetFitValues Method (IDimensionTolerance)"
project: "SOLIDWORKS API Help"
interface: "IDimensionTolerance"
member: "SetFitValues"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~SetFitValues.html"
---

# SetFitValues Method (IDimensionTolerance)

Sets the tolerance hole fit and shaft fit values.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetFitValues( _
   ByVal HoleFit As System.String, _
   ByVal ShaftFit As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimensionTolerance
Dim HoleFit As System.String
Dim ShaftFit As System.String
Dim value As System.Boolean

value = instance.SetFitValues(HoleFit, ShaftFit)
```

### C#

```csharp
System.bool SetFitValues(
   System.string HoleFit,
   System.string ShaftFit
)
```

### C++/CLI

```cpp
System.bool SetFitValues(
   System.String^ HoleFit,
   System.String^ ShaftFit
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `HoleFit`: Tolerance hole fit value
- `ShaftFit`: Tolerance shaft fit value

### Return Value

True if the setting of the fit values is successful, false if not

## VBA Syntax

See [DimensionTolerance::SetFitValues](ms-its:sldworksapivb6.chm::/sldworks~DimensionTolerance~SetFitValues.html).

## Remarks

| To get tolerance... | Use... |
| --- | --- |
| Hole fit value | IDimensionTolerance::GetHoleFitValue |
| Shaft fit value | IDimensionTolerance::GetShaftFitValue |

To see the effects of changing the tolerance fit values, use [IModelDoc2::GraphicsRedraw2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GraphicsRedraw2.html).

## See Also

[IDimensionTolerance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance.html)
[IDimensionTolerance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance_members.html)
[IDimensionTolerance::FitType Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~FitType.html)
[ICalloutVariable::HoleFit Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~HoleFit.html)
[ICalloutVariable::ShaftFit Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~ShaftFit.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
