---
title: "IGetTableRadii Method (IBaseFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBaseFlangeFeatureData"
member: "IGetTableRadii"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~IGetTableRadii.html"
---

# IGetTableRadii Method (IBaseFlangeFeatureData)

Gets the bend radii from the gauge table for this base flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTableRadii( _
   ByVal ThicknessTableName As System.String, _
   ByVal NCount As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IBaseFlangeFeatureData
Dim ThicknessTableName As System.String
Dim NCount As System.Integer
Dim value As System.Double

value = instance.IGetTableRadii(ThicknessTableName, NCount)
```

### C#

```csharp
System.double IGetTableRadii(
   System.string ThicknessTableName,
   System.int NCount
)
```

### C++/CLI

```cpp
System.double IGetTableRadii(
   System.String^ ThicknessTableName,
   System.int NCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ThicknessTableName`: Gauge table thickness names (see **Remarks**)
- `NCount`: Number of bend radii (see **Remarks**)

### Return Value

- in-process, unmanaged C++: Pointer to an array of bend radii

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method call:

- [IBaseFlangeFeatureData::IGetTableThicknesses](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBaseFlangeFeatureData~IGetTableThicknesses.html) to get the names of the thicknesses in the gauge table.
- [IBaseFlangeFeatureData::GetTableRadiiCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBaseFlangeFeatureData~GetTableRadiiCount.html) to get the value for NCount.

## See Also

[IBaseFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html)
[IBaseFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData_members.html)
[IBaseFlangeFeatureData::GetTableRadii Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~GetTableRadii.html)
[IBaseFlangeFeatureData::GaugeTablePath Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~GaugeTablePath.html)
[IBaseFlangeFeatureData::OverrideThickness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~OverrideThickness.html)
[IBaseFlangeFeatureData::ThicknessTableName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~ThicknessTableName.html)
[IBaseFlangeFeatureData::UseGaugeTable Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~UseGaugeTable.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
