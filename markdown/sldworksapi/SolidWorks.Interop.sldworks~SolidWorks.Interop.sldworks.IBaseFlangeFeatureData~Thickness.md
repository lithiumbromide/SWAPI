---
title: "Thickness Property (IBaseFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBaseFlangeFeatureData"
member: "Thickness"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~Thickness.html"
---

# Thickness Property (IBaseFlangeFeatureData)

Gets or sets the thickness for this base flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Thickness As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IBaseFlangeFeatureData
Dim value As System.Double

instance.Thickness = value

value = instance.Thickness
```

### C#

```csharp
System.double Thickness {get; set;}
```

### C++/CLI

```cpp
property System.double Thickness {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Value for thickness

## VBA Syntax

See [BaseFlangeFeatureData::Thickness](ms-its:sldworksapivb6.chm::/sldworks~BaseFlangeFeatureData~Thickness.html).

## Examples

See the [IBaseFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html) examples.

## Remarks

This property is valid only when not creating the base flange on an existing sheet metal feature.

The setter of this property is valid only if [IBaseFlangeFeatureData::OverrideDefaultSheetMetalParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~OverrideDefaultSheetMetalParameters.html) is true and [IBaseFlangeFeatureData::UseMaterialSheetMetalParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~UseMaterialSheetMetalParameters.html) is false.

This property gets:

- Default thickness if IBaseFlangeFeatureData::OverrideDefaultSheetMetalParameters is false.

- Custom thickness if IBaseFlangeFeatureData::OverrideDefaultSheetMetalParameters is true.

## See Also

[IBaseFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html)
[IBaseFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData_members.html)
[IBaseFlangeFeatureData::ReverseThickness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~ReverseThickness.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
