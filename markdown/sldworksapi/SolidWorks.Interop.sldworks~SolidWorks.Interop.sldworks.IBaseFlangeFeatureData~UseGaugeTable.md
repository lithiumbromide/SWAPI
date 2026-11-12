---
title: "UseGaugeTable Property (IBaseFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBaseFlangeFeatureData"
member: "UseGaugeTable"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~UseGaugeTable.html"
---

# UseGaugeTable Property (IBaseFlangeFeatureData)

Gets or sets whether to use a gauge table for this base flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseGaugeTable As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBaseFlangeFeatureData
Dim value As System.Boolean

instance.UseGaugeTable = value

value = instance.UseGaugeTable
```

### C#

```csharp
System.bool UseGaugeTable {get; set;}
```

### C++/CLI

```cpp
property System.bool UseGaugeTable {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use a gauge table, false to not

## VBA Syntax

See [BaseFlangeFeatureData::UseGaugeTable](ms-its:sldworksapivb6.chm::/sldworks~BaseFlangeFeatureData~UseGaugeTable.html).

## Examples

[Create Base-Flange Feature Using Gauge Table (VBA)](Create_Base-Flange_Feature_Using_Gauge_Table_Example_VB.htm)

## See Also

[IBaseFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html)
[IBaseFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData_members.html)
[IBaseFlangeFeatureData::GetTableRadii Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~GetTableRadii.html)
[IBaseFlangeFeatureData::IGetTableRadii Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~IGetTableRadii.html)
[IBaseFlangeFeatureData::GetTableRadiiCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~GetTableRadiiCount.html)
[IBaseFlangeFeatureData::GetTableThicknesses Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~GetTableThicknesses.html)
[IBaseFlangeFeatureData::IGetTableThicknesses Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~IGetTableThicknesses.html)
[IBaseFlangeFeatureData::GetTableThicknessesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~GetTableThicknessesCount.html)
[IBaseFlangeFeatureData::GaugeTablePath Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~GaugeTablePath.html)
[IBaseFlangeFeatureData::KFactor Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~KFactor.html)
[IBaseFlangeFeatureData::OverrideKFactor Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~OverrideKFactor.html)
[IBaseFlangeFeatureData::OverrideRadius Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~OverrideRadius.html)
[IBaseFlangeFeatureData::OverrideThickness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~OverrideThickness.html)
[IBaseFlangeFeatureData::TableKFactor Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~TableKFactor.html)
[IBaseFlangeFeatureData::TableThickness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~TableThickness.html)
[IBaseFlangeFeatureData::ThicknessTableName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~ThicknessTableName.html)
[IBaseFlangeFeatureData::TableRadius Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~TableRadius.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
