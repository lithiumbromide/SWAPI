---
title: "OverrideDefaultSheetMetalParameters Property (IBaseFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBaseFlangeFeatureData"
member: "OverrideDefaultSheetMetalParameters"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~OverrideDefaultSheetMetalParameters.html"
---

# OverrideDefaultSheetMetalParameters Property (IBaseFlangeFeatureData)

Gets or sets whether to override the default sheet metal parameters for this sheet metal base flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property OverrideDefaultSheetMetalParameters As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBaseFlangeFeatureData
Dim value As System.Boolean

instance.OverrideDefaultSheetMetalParameters = value

value = instance.OverrideDefaultSheetMetalParameters
```

### C#

```csharp
System.bool OverrideDefaultSheetMetalParameters {get; set;}
```

### C++/CLI

```cpp
property System.bool OverrideDefaultSheetMetalParameters {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to override the default values, false to not

## VBA Syntax

See [BaseFlangeFeatureData::OverrideDefaultSheetMetalParameters](ms-its:sldworksapivb6.chm::/sldworks~BaseFlangeFeatureData~OverrideDefaultSheetMetalParameters.html).

## Examples

See the [IBaseFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html) examples.

## Remarks

This property is valid only when creating the base flange in a non-sheet-metal part.

If this property is:

- True, then [IBaseFlangeFeatureData::Thickness](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~Thickness.html) and [IBaseFlangeFeatureData::BendRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~BendRadius.html) get and set user-defined values.
- False, then IBaseFlangeFeatureData::Thickness and IBaseFlangeFeatureData::BendRadius are invalid setters; those properties only get default values.

## See Also

[IBaseFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html)
[IBaseFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
