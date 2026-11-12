---
title: "UseMaterialSheetMetalParameters Property (IBaseFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBaseFlangeFeatureData"
member: "UseMaterialSheetMetalParameters"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~UseMaterialSheetMetalParameters.html"
---

# UseMaterialSheetMetalParameters Property (IBaseFlangeFeatureData)

Gets whether the properties of the material applied are used when creating this base flange.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property UseMaterialSheetMetalParameters As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBaseFlangeFeatureData
Dim value As System.Boolean

value = instance.UseMaterialSheetMetalParameters
```

### C#

```csharp
System.bool UseMaterialSheetMetalParameters {get;}
```

### C++/CLI

```cpp
property System.bool UseMaterialSheetMetalParameters {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True uses the applied material's sheet metal parameters, false does not

## VBA Syntax

See [BaseFlangeFeatureData::UseMaterialSheetMetalParameters](ms-its:sldworksapivb6.chm::/sldworks~BaseFlangeFeatureData~UseMaterialSheetMetalParameters.html).

## Examples

See the [IBaseFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html) examples.

## Remarks

This property is valid only:

- when not creating the base flange on an existing sheet metal feature,

- and -

- when [IBaseFlangeFeatureData::UseGaugeTable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~UseGaugeTable.html) is false.

If this property returns false, then specify sheet metal parameters using:

- [IBaseFlangeFeatureData::BendRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~BendRadius.html)
- [IBaseFlangeFeatureData::Thickness](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~Thickness.html)
- [IBaseFlangeFeatureData::ReverseThickness](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~ReverseThickness.html)

Whether to use the applied material's sheet metal parameters was set during the [initialization](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~Initialize.html) of this base flange and cannot be changed.

## See Also

[IBaseFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html)
[IBaseFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
