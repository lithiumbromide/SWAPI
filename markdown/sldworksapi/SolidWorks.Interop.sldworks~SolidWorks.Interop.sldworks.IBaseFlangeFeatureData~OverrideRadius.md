---
title: "OverrideRadius Property (IBaseFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBaseFlangeFeatureData"
member: "OverrideRadius"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~OverrideRadius.html"
---

# OverrideRadius Property (IBaseFlangeFeatureData)

Gets or sets whether to override the bend radius value specified in the gauge table for this base flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property OverrideRadius As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBaseFlangeFeatureData
Dim value As System.Boolean

instance.OverrideRadius = value

value = instance.OverrideRadius
```

### C#

```csharp
System.bool OverrideRadius {get; set;}
```

### C++/CLI

```cpp
property System.bool OverrideRadius {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to override the bend radius value, false to not

## VBA Syntax

See [BaseFlangeFeatureData::OverrideRadius](ms-its:sldworksapivb6.chm::/sldworks~BaseFlangeFeatureData~OverrideRadius.html).

## Examples

[Create Base-Flange Feature Using Gauge Table (VBA)](Create_Base-Flange_Feature_Using_Gauge_Table_Example_VB.htm)

## See Also

[IBaseFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html)
[IBaseFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData_members.html)
[IBaseFlangeFeatureData::GetTableRadii Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~GetTableRadii.html)
[IBaseFlangeFeatureData::GetTableRadiiCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~GetTableRadiiCount.html)
[IBaseFlangeFeatureData::IGetTableRadii Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~IGetTableRadii.html)
[IBaseFlangeFeatureData::TableRadius Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~TableRadius.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
