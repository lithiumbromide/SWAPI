---
title: "SetThickness Method (ISheetMetalGaugeTableParameters)"
project: "SOLIDWORKS API Help"
interface: "ISheetMetalGaugeTableParameters"
member: "SetThickness"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~SetThickness.html"
---

# SetThickness Method (ISheetMetalGaugeTableParameters)

Sets the gauge thickness in this gauge table.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetThickness( _
   ByVal Thickness As System.Double, _
   ByVal Override As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISheetMetalGaugeTableParameters
Dim Thickness As System.Double
Dim Override As System.Boolean
Dim value As System.Boolean

value = instance.SetThickness(Thickness, Override)
```

### C#

```csharp
System.bool SetThickness(
   System.double Thickness,
   System.bool Override
)
```

### C++/CLI

```cpp
System.bool SetThickness(
   System.double Thickness,
   System.bool Override
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Thickness`: Gauge thickness
- `Override`: True to override an existing value, false to not (see **Remarks**)

### Return Value

True if gauge thickness successfully set, false if not

## VBA Syntax

See [SheetMetalGaugeTableParameters::SetThickness](ms-its:sldworksapivb6.chm::/sldworks~SheetMetalGaugeTableParameters~SetThickness.html).

## Examples

See the [ISheetMetalGaugeTableParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters.html) examples.

## Remarks

If Override is:

- true, then specify Thickness using an override gauge thickness. You should also use [ISheetMetalGaugeTableParameters::SetRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~SetRadius.html) to override the bend radius.
- false, instead of calling this method use [ISheetMetalGaugeTableParameters::GetAvailableGaugeNumbers](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~GetAvailableGaugeNumbers.html) and [ISheetMetalGaugeTableParameters::SetCurrentGaugeNumber](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~SetCurrentGaugeNumber.html) to change the current gauge number. Each gauge number has a default thickness.

## See Also

[ISheetMetalGaugeTableParameters Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters.html)
[ISheetMetalGaugeTableParameters Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters_members.html)
[ISheetMetalGaugeTableParameters::GetThickness Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~GetThickness.html)
[ISheetMetalGaugeTableParameters::OverrideThickness Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~OverrideThickness.html)
[ISheetMetalGaugeTableParameters::ReverseDirection Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~ReverseDirection.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
