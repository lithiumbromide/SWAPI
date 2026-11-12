---
title: "ThicknessTableName Property (IBaseFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBaseFlangeFeatureData"
member: "ThicknessTableName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~ThicknessTableName.html"
---

# ThicknessTableName Property (IBaseFlangeFeatureData)

Gets or sets the name of the thickness from the gauge table, if thickness not [overridden](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBaseFlangeFeatureData~OverrideThickness.html), for this base flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ThicknessTableName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IBaseFlangeFeatureData
Dim value As System.String

instance.ThicknessTableName = value

value = instance.ThicknessTableName
```

### C#

```csharp
System.string ThicknessTableName {get; set;}
```

### C++/CLI

```cpp
property System.String^ ThicknessTableName {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Name of thickness

## VBA Syntax

See [BaseFlangeFeatureData::ThicknessTableName](ms-its:sldworksapivb6.chm::/sldworks~BaseFlangeFeatureData~ThicknessTableName.html).

## Examples

[Create Base-Flange Feature Using Gauge Table (VBA)](Create_Base-Flange_Feature_Using_Gauge_Table_Example_VB.htm)

## See Also

[IBaseFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html)
[IBaseFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData_members.html)
[IBaseFlangeFeatureData::GetTableThicknesses Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~GetTableThicknesses.html)
[IBaseFlangeFeatureData::IGetTableThicknesses Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~IGetTableThicknesses.html)
[IBaseFlangeFeatureData::GetTableThicknessesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~GetTableThicknessesCount.html)
[IBaseFlangeFeatureData::GaugeTablePath Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~GaugeTablePath.html)
[IBaseFlangeFeatureData::TableThickness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~TableThickness.html)
[IBaseFlangeFeatureData::UseGaugeTable Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~UseGaugeTable.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
