---
title: "GetAvailableRadii Method (ISheetMetalGaugeTableParameters)"
project: "SOLIDWORKS API Help"
interface: "ISheetMetalGaugeTableParameters"
member: "GetAvailableRadii"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~GetAvailableRadii.html"
---

# GetAvailableRadii Method (ISheetMetalGaugeTableParameters)

Gets the available bend radii for the gauge number currently selected from this gauge table.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAvailableRadii() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISheetMetalGaugeTableParameters
Dim value As System.Object

value = instance.GetAvailableRadii()
```

### C#

```csharp
System.object GetAvailableRadii()
```

### C++/CLI

```cpp
System.Object^ GetAvailableRadii();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of bend radii strings

## VBA Syntax

See [SheetMetalGaugeTableParameters::GetAvailableRadii](ms-its:sldworksapivb6.chm::/sldworks~SheetMetalGaugeTableParameters~GetAvailableRadii.html).

## Examples

See the [ISheetMetalGaugeTableParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters.html) examples.

## See Also

[ISheetMetalGaugeTableParameters Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters.html)
[ISheetMetalGaugeTableParameters Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters_members.html)
[ISheetMetalGaugeTableParameters::GetCurrentRadius Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~GetCurrentRadius.html)
[ISheetMetalGaugeTableParameters::GetRadiiCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~GetRadiiCount.html)
[ISheetMetalGaugeTableParameters::SetRadius Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~SetRadius.html)
[ISheetMetalGaugeTableParameters::OverrideRadius Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~OverrideRadius.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
