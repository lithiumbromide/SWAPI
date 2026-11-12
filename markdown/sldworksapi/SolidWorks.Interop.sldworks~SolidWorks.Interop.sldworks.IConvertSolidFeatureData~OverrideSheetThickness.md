---
title: "OverrideSheetThickness Property (IConvertSolidFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IConvertSolidFeatureData"
member: "OverrideSheetThickness"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~OverrideSheetThickness.html"
---

# OverrideSheetThickness Property (IConvertSolidFeatureData)

Gets or sets whether to override the gauge thickness for this convert solid feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property OverrideSheetThickness As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IConvertSolidFeatureData
Dim value As System.Boolean

instance.OverrideSheetThickness = value

value = instance.OverrideSheetThickness
```

### C#

```csharp
System.bool OverrideSheetThickness {get; set;}
```

### C++/CLI

```cpp
property System.bool OverrideSheetThickness {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to override the gauge thickness, false to not

## VBA Syntax

See [ConvertSolidFeatureData::OverrideSheetThickness](ms-its:sldworksapivb6.chm::/sldworks~ConvertSolidFeatureData~OverrideSheetThickness.html).

## Remarks

This property is related to the gauge table only. This property is valid only before calling [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.html) to create a new sheet metal feature.

## See Also

[IConvertSolidFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.html)
[IConvertSolidFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData_members.html)

## Availability

SOLIDWORKS 2025 SP03, Revision Number 33.3
