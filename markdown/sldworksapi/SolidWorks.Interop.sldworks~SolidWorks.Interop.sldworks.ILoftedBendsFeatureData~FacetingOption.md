---
title: "FacetingOption Property (ILoftedBendsFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILoftedBendsFeatureData"
member: "FacetingOption"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~FacetingOption.html"
---

# FacetingOption Property (ILoftedBendsFeatureData)

Gets or sets how facets are created in this lofted bend feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property FacetingOption As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ILoftedBendsFeatureData
Dim value As System.Integer

instance.FacetingOption = value

value = instance.FacetingOption
```

### C#

```csharp
System.int FacetingOption {get; set;}
```

### C++/CLI

```cpp
property System.int FacetingOption {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Faceting option as defined in [swLoftedBendFacetOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLoftedBendFacetOptions_e.html)

## VBA Syntax

See [LoftedBendsFeatureData::FacetingOption](ms-its:sldworksapivb6.chm::/sldworks~LoftedBendsFeatureData~FacetingOption.html).

## Examples

See examples for [ILoftedBendsFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoftedBendsFeatureData.html).

## Remarks

This property is valid only if [ILoftedBendsFeatureData::FormedMethod](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoftedBendsFeatureData~FormedMethod.html) is false.

After setting this property, set [ILoftedBendsFeatureData::FacetValue](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoftedBendsFeatureData~FacetValue.html).

## See Also

[ILoftedBendsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData.html)
[ILoftedBendsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData_members.html)
[ILoftedBendsFeatureData::ReferToEndPoint Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~ReferToEndPoint.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
