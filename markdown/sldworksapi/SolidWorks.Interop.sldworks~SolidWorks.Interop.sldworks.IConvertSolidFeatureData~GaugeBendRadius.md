---
title: "GaugeBendRadius Property (IConvertSolidFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IConvertSolidFeatureData"
member: "GaugeBendRadius"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~GaugeBendRadius.html"
---

# GaugeBendRadius Property (IConvertSolidFeatureData)

Gets or sets the gauge bend radius in this convert solid feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property GaugeBendRadius As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IConvertSolidFeatureData
Dim value As System.Double

instance.GaugeBendRadius = value

value = instance.GaugeBendRadius
```

### C#

```csharp
System.double GaugeBendRadius {get; set;}
```

### C++/CLI

```cpp
property System.double GaugeBendRadius {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Gauge bend radius

## VBA Syntax

See [ConvertSolidFeatureData::GaugeBendRadius](ms-its:sldworksapivb6.chm::/sldworks~ConvertSolidFeatureData~GaugeBendRadius.html).

## Remarks

This property is related to the gauge table only. This property is valid only before calling [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.html) to create a new sheet metal feature.

## See Also

[IConvertSolidFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.html)
[IConvertSolidFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData_members.html)

## Availability

SOLIDWORKS 2025 SP03, Revision Number 33.3
