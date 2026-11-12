---
title: "SetCurrentGaugeNumber Method (ISheetMetalGaugeTableParameters)"
project: "SOLIDWORKS API Help"
interface: "ISheetMetalGaugeTableParameters"
member: "SetCurrentGaugeNumber"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~SetCurrentGaugeNumber.html"
---

# SetCurrentGaugeNumber Method (ISheetMetalGaugeTableParameters)

Sets the current gauge number in this gauge table.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetCurrentGaugeNumber( _
   ByVal GaugeNumber As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISheetMetalGaugeTableParameters
Dim GaugeNumber As System.String
Dim value As System.Boolean

value = instance.SetCurrentGaugeNumber(GaugeNumber)
```

### C#

```csharp
System.bool SetCurrentGaugeNumber(
   System.string GaugeNumber
)
```

### C++/CLI

```cpp
System.bool SetCurrentGaugeNumber(
   System.String^ GaugeNumber
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `GaugeNumber`: Gauge number string (see **Remarks**)

### Return Value

True if current gauge number successfully set, false if not

## VBA Syntax

See [SheetMetalGaugeTableParameters::SetCurrentGaugeNumber](ms-its:sldworksapivb6.chm::/sldworks~SheetMetalGaugeTableParameters~SetCurrentGaugeNumber.html).

## Examples

See the [ISheetMetalGaugeTableParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters.html) examples.

## Remarks

Use [ISheetMetalGaugeTableParameters::GetAvailableGaugeNumbers](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~GetAvailableGaugeNumbers.html) to determine GaugeNumber.

## See Also

[ISheetMetalGaugeTableParameters Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters.html)
[ISheetMetalGaugeTableParameters Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters_members.html)
[ISheetMetalGaugeTableParameters::GetCurrentGaugeNumber Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~GetCurrentGaugeNumber.html)
[ISheetMetalGaugeTableParameters::GetGaugeNumberCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~GetGaugeNumberCount.html)
[ISheetMetalGaugeTableParameters::SetThickness Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~SetThickness.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
