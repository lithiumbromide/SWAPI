---
title: "OverrideThickness Property (IBaseFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBaseFlangeFeatureData"
member: "OverrideThickness"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~OverrideThickness.html"
---

# OverrideThickness Property (IBaseFlangeFeatureData)

Gets or sets whether to override the thickness value specified in the gauge table for this base flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property OverrideThickness As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBaseFlangeFeatureData
Dim value As System.Boolean

instance.OverrideThickness = value

value = instance.OverrideThickness
```

### C#

```csharp
System.bool OverrideThickness {get; set;}
```

### C++/CLI

```cpp
property System.bool OverrideThickness {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to override the thickness, false to not

## VBA Syntax

See [BaseFlangeFeatureData::OverrideThickness](ms-its:sldworksapivb6.chm::/sldworks~BaseFlangeFeatureData~OverrideThickness.html).

## Examples

[Create Base-Flange Feature Using Gauge Table (VBA)](Create_Base-Flange_Feature_Using_Gauge_Table_Example_VB.htm)

## See Also

[IBaseFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html)
[IBaseFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData_members.html)
[IBaseFlangeFeatureData::GaugeTablePath Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~GaugeTablePath.html)
[IBaseFlangeFeatureData::GetTableThicknesses Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~GetTableThicknesses.html)
[IBaseFlangeFeatureData::IGetTableThicknesses Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~IGetTableThicknesses.html)
[IBaseFlangeFeatureData::GetTableThicknessesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~GetTableThicknessesCount.html)
[IBaseFlangeFeatureData::TableThickness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~TableThickness.html)
[IBaseFlangeFeatureData::UseGaugeTable Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~UseGaugeTable.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
