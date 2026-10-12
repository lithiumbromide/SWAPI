---
title: "OverrideDefaultSheetMetalParameters Property (ISweptFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweptFlangeFeatureData"
member: "OverrideDefaultSheetMetalParameters"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~OverrideDefaultSheetMetalParameters.html"
---

# OverrideDefaultSheetMetalParameters Property (ISweptFlangeFeatureData)

Gets or sets whether to override the default sheet metal parameters for this swept flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property OverrideDefaultSheetMetalParameters As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISweptFlangeFeatureData
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

See [SweptFlangeFeatureData::OverrideDefaultSheetMetalParameters](ms-its:sldworksapivb6.chm::/sldworks~SweptFlangeFeatureData~OverrideDefaultSheetMetalParameters.html).

## Examples

See the [ISweptFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.html) examples.

## Remarks

This property is valid only when creating the swept flange in a non-sheet-metal part.

If this property is:

- True, then [ISweptFlangeFeatureData::Thickness](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~Thickness.html) and [ISweptFlangeFeatureData::BendRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~BendRadius.html) get and set user-defined values.
- False, then ISweptFlangeFeatureData::Thickness and ISweptFlangeFeatureData::BendRadius are invalid as setters and get only default values.

## See Also

[ISweptFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.html)
[ISweptFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData_members.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
