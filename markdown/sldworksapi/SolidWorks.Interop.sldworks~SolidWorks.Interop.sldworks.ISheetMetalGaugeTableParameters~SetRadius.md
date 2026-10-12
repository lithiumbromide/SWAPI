---
title: "SetRadius Method (ISheetMetalGaugeTableParameters)"
project: "SOLIDWORKS API Help"
interface: "ISheetMetalGaugeTableParameters"
member: "SetRadius"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~SetRadius.html"
---

# SetRadius Method (ISheetMetalGaugeTableParameters)

Sets the bend radius in this gauge table.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetRadius( _
   ByVal Radius As System.Double, _
   ByVal Override As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISheetMetalGaugeTableParameters
Dim Radius As System.Double
Dim Override As System.Boolean
Dim value As System.Boolean

value = instance.SetRadius(Radius, Override)
```

### C#

```csharp
System.bool SetRadius(
   System.double Radius,
   System.bool Override
)
```

### C++/CLI

```cpp
System.bool SetRadius(
   System.double Radius,
   System.bool Override
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Radius`: Bend radius
- `Override`: True to override an existing value, false to not (see **Remarks**)

### Return Value

True if bend radius successfully set, false if not

## VBA Syntax

See [SheetMetalGaugeTableParameters::SetRadius](ms-its:sldworksapivb6.chm::/sldworks~SheetMetalGaugeTableParameters~SetRadius.html).

## Examples

See the [ISheetMetalGaugeTableParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters.html) examples.

## Remarks

If Override is:

- true, then specify an override bend radius in Radius.
- false, then specify Radius using one of the default bend radii for the current gauge number from the gauge table. Use [ISheetMetalGaugeTableParameters::GetAvailableRadii](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~GetAvailableRadii.html) to choose a value for Radius.

## See Also

[ISheetMetalGaugeTableParameters Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters.html)
[ISheetMetalGaugeTableParameters Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters_members.html)
[ISheetMetalGaugeTableParameters::OverrideRadius Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~OverrideRadius.html)
[ISheetMetalGaugeTableParameters::GetCurrentRadius Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~GetCurrentRadius.html)
[ISheetMetalGaugeTableParameters::GetRadiiCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~GetRadiiCount.html)
[ISheetMetalGaugeTableParameters::SetThickness Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~SetThickness.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
