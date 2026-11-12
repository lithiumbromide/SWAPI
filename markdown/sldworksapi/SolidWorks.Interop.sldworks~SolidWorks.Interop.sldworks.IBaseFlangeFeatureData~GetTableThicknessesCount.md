---
title: "GetTableThicknessesCount Method (IBaseFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBaseFlangeFeatureData"
member: "GetTableThicknessesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~GetTableThicknessesCount.html"
---

# GetTableThicknessesCount Method (IBaseFlangeFeatureData)

Gets the number of names of the thicknesses in the gauge table for this base flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTableThicknessesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBaseFlangeFeatureData
Dim value As System.Integer

value = instance.GetTableThicknessesCount()
```

### C#

```csharp
System.int GetTableThicknessesCount()
```

### C++/CLI

```cpp
System.int GetTableThicknessesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of names of the thicknesses

## VBA Syntax

See [BaseFlangeFeatureData::GetTableThicknessesCount](ms-its:sldworksapivb6.chm::/sldworks~BaseFlangeFeatureData~GetTableThicknessesCount.html).

## Remarks

Call this method before calling [IBaseFlangeFeatureData::IGetTableThicknesses](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBaseFlangeFeatureData~IGetTableThicknesses.html) to get the size of the array for that method.

## See Also

[IBaseFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html)
[IBaseFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData_members.html)
[IBaseFlangeFeatureData::GetTableThicknesses Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~GetTableThicknesses.html)
[IBaseFlangeFeatureData::GaugeTablePath Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~GaugeTablePath.html)
[IBaseFlangeFeatureData::OverrideThickness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~OverrideThickness.html)
[IBaseFlangeFeatureData::TableThickness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~TableThickness.html)
[IBaseFlangeFeatureData::ThicknessTableName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~ThicknessTableName.html)
[IBaseFlangeFeatureData::UseGaugeTable Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~UseGaugeTable.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
