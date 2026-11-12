---
title: "GaugeTablePath Property (IBaseFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBaseFlangeFeatureData"
member: "GaugeTablePath"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~GaugeTablePath.html"
---

# GaugeTablePath Property (IBaseFlangeFeatureData)

Gets or sets the path to a gauge table file for this base flange feature

## Syntax

### Visual Basic (Declaration)

```vb
Property GaugeTablePath As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IBaseFlangeFeatureData
Dim value As System.String

instance.GaugeTablePath = value

value = instance.GaugeTablePath
```

### C#

```csharp
System.string GaugeTablePath {get; set;}
```

### C++/CLI

```cpp
property System.String^ GaugeTablePath {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Fully qualified path to a gauge table file

## VBA Syntax

See [BaseFlangeFeatureData::GaugeTablePath](ms-its:sldworksapivb6.chm::/sldworks~BaseFlangeFeatureData~GaugeTablePath.html).

## Examples

[Create Base-Flange Feature Using Gauge Table (VBA)](Create_Base-Flange_Feature_Using_Gauge_Table_Example_VB.htm)

## See Also

[IBaseFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html)
[IBaseFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData_members.html)
[IBaseFlangeFeatureData::UseGaugeTable Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~UseGaugeTable.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
