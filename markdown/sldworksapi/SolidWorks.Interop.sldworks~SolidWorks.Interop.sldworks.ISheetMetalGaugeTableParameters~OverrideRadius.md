---
title: "OverrideRadius Property (ISheetMetalGaugeTableParameters)"
project: "SOLIDWORKS API Help"
interface: "ISheetMetalGaugeTableParameters"
member: "OverrideRadius"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~OverrideRadius.html"
---

# OverrideRadius Property (ISheetMetalGaugeTableParameters)

Gets whether the bend radius of this gauge table is overridden.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property OverrideRadius As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISheetMetalGaugeTableParameters
Dim value As System.Boolean

value = instance.OverrideRadius
```

### C#

```csharp
System.bool OverrideRadius {get;}
```

### C++/CLI

```cpp
property System.bool OverrideRadius {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if gauge table bend radius is overridden, false if not

## VBA Syntax

See [SheetMetalGaugeTableParameters::OverrideRadius](ms-its:sldworksapivb6.chm::/sldworks~SheetMetalGaugeTableParameters~OverrideRadius.html).

## Examples

See the [ISheetMetalGaugeTableParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters.html) examples.

## See Also

[ISheetMetalGaugeTableParameters Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters.html)
[ISheetMetalGaugeTableParameters Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters_members.html)
[ISheetMetalGaugeTableParameters::SetRadius Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~SetRadius.html)
[ISheetMetalGaugeTableParameters::GetAvailableRadii Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~GetAvailableRadii.html)
[ISheetMetalGaugeTableParameters::GetCurrentRadius Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~GetCurrentRadius.html)
[ISheetMetalGaugeTableParameters::GetRadiiCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~GetRadiiCount.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
