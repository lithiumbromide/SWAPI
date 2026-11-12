---
title: "TableRadius Property (IBaseFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBaseFlangeFeatureData"
member: "TableRadius"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~TableRadius.html"
---

# TableRadius Property (IBaseFlangeFeatureData)

Gets or sets the bend radius, if is not [overridden](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBaseFlangeFeatureData~OverrideRadius.html), in the gauge table for this base flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property TableRadius As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IBaseFlangeFeatureData
Dim value As System.Double

instance.TableRadius = value

value = instance.TableRadius
```

### C#

```csharp
System.double TableRadius {get; set;}
```

### C++/CLI

```cpp
property System.double TableRadius {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Bend radius

## VBA Syntax

See [BaseFlangeFeatureData::TableRadius](ms-its:sldworksapivb6.chm::/sldworks~BaseFlangeFeatureData~TableRadius.html).

## Examples

[Create Base-Flange Feature Using Gauge Table (VBA)](Create_Base-Flange_Feature_Using_Gauge_Table_Example_VB.htm)

## Remarks

If the bend radius is not overridden, then the value for the bend radius is the value returned or set by [IBaseFlangeFeatureData::BendRadius](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBaseFlangeFeatureData~BendRadius.html).

## See Also

[IBaseFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html)
[IBaseFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData_members.html)
[IBaseFlangeFeatureData::GetTableRadii Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~GetTableRadii.html)
[IBaseFlangeFeatureData::IGetTableRadii Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~IGetTableRadii.html)
[IBaseFlangeFeatureData::GetTableRadiiCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~GetTableRadiiCount.html)
[IBaseFlangeFeatureData::GaugeTablePath Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~GaugeTablePath.html)
[IBaseFlangeFeatureData::OverrideRadius Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~OverrideRadius.html)
[IBaseFlangeFeatureData::UseGaugeTable Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~UseGaugeTable.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
