---
title: "OverrideBendRadius Property (IConvertSolidFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IConvertSolidFeatureData"
member: "OverrideBendRadius"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~OverrideBendRadius.html"
---

# OverrideBendRadius Property (IConvertSolidFeatureData)

Gets or sets whether to override the gauge bend radius for this convert solid feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property OverrideBendRadius As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IConvertSolidFeatureData
Dim value As System.Boolean

instance.OverrideBendRadius = value

value = instance.OverrideBendRadius
```

### C#

```csharp
System.bool OverrideBendRadius {get; set;}
```

### C++/CLI

```cpp
property System.bool OverrideBendRadius {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to override the gauge bend radius, false to not

## VBA Syntax

See [ConvertSolidFeatureData::OverrideBendRadius](ms-its:sldworksapivb6.chm::/sldworks~ConvertSolidFeatureData~OverrideBendRadius.html).

## Remarks

This property is related to the gauge table only. This property is valid only before calling [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.html) to create a new sheet metal feature.

## See Also

[IConvertSolidFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.html)
[IConvertSolidFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData_members.html)

## Availability

SOLIDWORKS 2025 SP03, Revision Number 33.3
