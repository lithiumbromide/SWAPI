---
title: "OverrideThickness Property (ISheetMetalGaugeTableParameters)"
project: "SOLIDWORKS API Help"
interface: "ISheetMetalGaugeTableParameters"
member: "OverrideThickness"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~OverrideThickness.html"
---

# OverrideThickness Property (ISheetMetalGaugeTableParameters)

Gets whether the gauge thickness of this gauge table is overridden.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property OverrideThickness As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISheetMetalGaugeTableParameters
Dim value As System.Boolean

value = instance.OverrideThickness
```

### C#

```csharp
System.bool OverrideThickness {get;}
```

### C++/CLI

```cpp
property System.bool OverrideThickness {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if gauge thickness is overridden, false if not

## VBA Syntax

See [SheetMetalGaugeTableParameters::OverrideThickness](ms-its:sldworksapivb6.chm::/sldworks~SheetMetalGaugeTableParameters~OverrideThickness.html).

## Examples

See the [ISheetMetalGaugeTableParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters.html) examples.

## See Also

[ISheetMetalGaugeTableParameters Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters.html)
[ISheetMetalGaugeTableParameters Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters_members.html)
[ISheetMetalGaugeTableParameters::ReverseDirection Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~ReverseDirection.html)
[ISheetMetalGaugeTableParameters::GetThickness Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~GetThickness.html)
[ISheetMetalGaugeTableParameters::SetThickness Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~SetThickness.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
