---
title: "GetTableRadii Method (IBaseFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBaseFlangeFeatureData"
member: "GetTableRadii"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~GetTableRadii.html"
---

# GetTableRadii Method (IBaseFlangeFeatureData)

Gets the bend radii from the gauge table for this base flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTableRadii( _
   ByVal ThicknessTableName As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBaseFlangeFeatureData
Dim ThicknessTableName As System.String
Dim value As System.Object

value = instance.GetTableRadii(ThicknessTableName)
```

### C#

```csharp
System.object GetTableRadii(
   System.string ThicknessTableName
)
```

### C++/CLI

```cpp
System.Object^ GetTableRadii(
   System.String^ ThicknessTableName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ThicknessTableName`: Gauge table thickness names (see **Remarks**)

### Return Value

Array of bend radii

## VBA Syntax

See [BaseFlangeFeatureData::GetTableRadii](ms-its:sldworksapivb6.chm::/sldworks~BaseFlangeFeatureData~GetTableRadii.html).

## Examples

[Create Base-Flange Feature Using Gauge Table (VBA)](Create_Base-Flange_Feature_Using_Gauge_Table_Example_VB.htm)

## Remarks

Before calling this method call, [IBaseFlangeFeatureData::GetTableThicknesses](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBaseFlangeFeatureData~GetTableThicknesses.html) to get the names of the thicknesses in the gauge table.

## See Also

[IBaseFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html)
[IBaseFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData_members.html)
[IBaseFlangeFeatureData::IGetTableRadii Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~IGetTableRadii.html)
[IBaseFlangeFeatureData::GaugeTablePath Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~GaugeTablePath.html)
[IBaseFlangeFeatureData::GetTableRadiiCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~GetTableRadiiCount.html)
[IBaseFlangeFeatureData::OverrideRadius Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~OverrideRadius.html)
[IBaseFlangeFeatureData::TableRadius Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~TableRadius.html)
[IBaseFlangeFeatureData::UseGaugeTable Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~UseGaugeTable.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
