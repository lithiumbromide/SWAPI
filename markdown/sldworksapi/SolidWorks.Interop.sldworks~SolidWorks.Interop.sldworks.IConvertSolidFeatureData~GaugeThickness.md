---
title: "GaugeThickness Property (IConvertSolidFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IConvertSolidFeatureData"
member: "GaugeThickness"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~GaugeThickness.html"
---

# GaugeThickness Property (IConvertSolidFeatureData)

See [ConvertSolidFeatureData::GaugeTableFile](ms-its:sldworksapivb6.chm::/sldworks~ConvertSolidFeatureData~GaugeTableFile.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property GaugeThickness As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IConvertSolidFeatureData
Dim value As System.String

instance.GaugeThickness = value

value = instance.GaugeThickness
```

### C#

```csharp
System.string GaugeThickness {get; set;}
```

### C++/CLI

```cpp
property System.String^ GaugeThickness {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Gauge thickness

## VBA Syntax

See [ConvertSolidFeatureData::GaugeThickness](ms-its:sldworksapivb6.chm::/sldworks~ConvertSolidFeatureData~GaugeThickness.html).

## Remarks

This property is related to the gauge table only. This property is valid only before calling [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.html) to create a new sheet metal feature.

## See Also

[IConvertSolidFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.html)
[IConvertSolidFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData_members.html)

## Availability

SOLIDWORKS 2025 SP03, Revision Number 33.3
