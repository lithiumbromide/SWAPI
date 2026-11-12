---
title: "GetCurrentGaugeNumber Method (ISheetMetalGaugeTableParameters)"
project: "SOLIDWORKS API Help"
interface: "ISheetMetalGaugeTableParameters"
member: "GetCurrentGaugeNumber"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~GetCurrentGaugeNumber.html"
---

# GetCurrentGaugeNumber Method (ISheetMetalGaugeTableParameters)

Gets the gauge number currently selected from this gauge table.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCurrentGaugeNumber() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISheetMetalGaugeTableParameters
Dim value As System.String

value = instance.GetCurrentGaugeNumber()
```

### C#

```csharp
System.string GetCurrentGaugeNumber()
```

### C++/CLI

```cpp
System.String^ GetCurrentGaugeNumber();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Currently selected gauge number

## VBA Syntax

See [SheetMetalGaugeTableParameters::GetCurrentGaugeNumber](ms-its:sldworksapivb6.chm::/sldworks~SheetMetalGaugeTableParameters~GetCurrentGaugeNumber.html).

## Examples

See the [ISheetMetalGaugeTableParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters.html) examples.

## See Also

[ISheetMetalGaugeTableParameters Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters.html)
[ISheetMetalGaugeTableParameters Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters_members.html)
[ISheetMetalGaugeTableParameters::GetAvailableGaugeNumbers Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~GetAvailableGaugeNumbers.html)
[ISheetMetalGaugeTableParameters::GetGaugeNumberCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~GetGaugeNumberCount.html)
[ISheetMetalGaugeTableParameters::SetCurrentGaugeNumber Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~SetCurrentGaugeNumber.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
