---
title: "BendRadius Property (IBaseFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBaseFlangeFeatureData"
member: "BendRadius"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~BendRadius.html"
---

# BendRadius Property (IBaseFlangeFeatureData)

Gets or sets the bend radius of this bend flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property BendRadius As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IBaseFlangeFeatureData
Dim value As System.Double

instance.BendRadius = value

value = instance.BendRadius
```

### C#

```csharp
System.double BendRadius {get; set;}
```

### C++/CLI

```cpp
property System.double BendRadius {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Value of the bend radius

## VBA Syntax

See [BaseFlangeFeatureData::BendRadius](ms-its:sldworksapivb6.chm::/sldworks~BaseFlangeFeatureData~BendRadius.html).

## Examples

See [IBaseFlangeFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBaseFlangeFeatureData.html) examples.

## Remarks

The setter of this property is valid only if [IBaseFlangeFeatureData::OverrideDefaultSheetMetalParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~OverrideDefaultSheetMetalParameters.html) is true and [IBaseFlangeFeatureData::UseMaterialSheetMetalParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~UseMaterialSheetMetalParameters.html) is false.

This property gets a:

- Default bend radius if:

- IBaseFlangeFeatureData::UseMaterialSheetMetalParameters is true,

- and -

- IBaseFlangeFeatureData:: OverrideDefaultSheetMetalParameters is false.

- Custom bend radius if:

- IBaseFlangeFeatureData::UseDefaultRadius is false,

- and -

- IBaseFlangeFeatureData:: OverrideDefaultSheetMetalParameters is true.

## See Also

[IBaseFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html)
[IBaseFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData_members.html)

## Availability

SOLIDWORKS 2001 SP2, Revision 9.2
