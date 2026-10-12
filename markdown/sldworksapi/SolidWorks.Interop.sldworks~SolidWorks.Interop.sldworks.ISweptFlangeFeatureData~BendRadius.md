---
title: "BendRadius Property (ISweptFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweptFlangeFeatureData"
member: "BendRadius"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~BendRadius.html"
---

# BendRadius Property (ISweptFlangeFeatureData)

Gets or sets the bend radius of this swept flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property BendRadius As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISweptFlangeFeatureData
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

Bend radius

## VBA Syntax

See [SweptFlangeFeatureData::BendRadius](ms-its:sldworksapivb6.chm::/sldworks~SweptFlangeFeatureData~BendRadius.html).

## Remarks

The setter of this property is valid only if [ISweptFlangeFeatureData::OverrideDefaultSheetMetalParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~OverrideDefaultSheetMetalParameters.html) is true.

This property gets a:

- Default bend radius if:

- [ISweptFlangeFeatureData::UseDefaultRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~UseDefaultRadius.html) is true,

- and -

- ISweptFlangeFeatureData::OverrideDefaultSheetMetalParameters is false.

- Custom bend radius if:

- ISweptFlangeFeatureData::UseDefaultRadius is false,

- and -

- ISweptFlangeFeatureData::OverrideDefaultSheetMetalParameters is true.

## See Also

[ISweptFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.html)
[ISweptFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData_members.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
