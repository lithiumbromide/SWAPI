---
title: "GetTableRadiiCount Method (IBaseFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBaseFlangeFeatureData"
member: "GetTableRadiiCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~GetTableRadiiCount.html"
---

# GetTableRadiiCount Method (IBaseFlangeFeatureData)

Gets the number of bend radii for the thickness names from the gauge table for this base flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTableRadiiCount( _
   ByVal ThicknessTableName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBaseFlangeFeatureData
Dim ThicknessTableName As System.String
Dim value As System.Integer

value = instance.GetTableRadiiCount(ThicknessTableName)
```

### C#

```csharp
System.int GetTableRadiiCount(
   System.string ThicknessTableName
)
```

### C++/CLI

```cpp
System.int GetTableRadiiCount(
   System.String^ ThicknessTableName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ThicknessTableName`: Thickness names

### Return Value

Number of bend radii

## VBA Syntax

See [BaseFlangeFeatureData::GetTableRadiiCount](ms-its:sldworksapivb6.chm::/sldworks~BaseFlangeFeatureData~GetTableRadiiCount.html).

## Remarks

Call this method before calling [IBaseFlangeFeatureData::IGetTableRadii](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBaseFlangeFeatureData~IGetTableRadii.html).

## See Also

[IBaseFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html)
[IBaseFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData_members.html)
[IBaseFlangeFeatureData::GetTableRadii Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~GetTableRadii.html)
[IBaseFlangeFeatureData::GaugeTablePath Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~GaugeTablePath.html)
[IBaseFlangeFeatureData::OverrideRadius Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~OverrideRadius.html)
[IBaseFlangeFeatureData::TableRadius Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~TableRadius.html)
[IBaseFlangeFeatureData::UseGaugeTable Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~UseGaugeTable.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
