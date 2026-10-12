---
title: "FacetValue Property (ILoftedBendsFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILoftedBendsFeatureData"
member: "FacetValue"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~FacetValue.html"
---

# FacetValue Property (ILoftedBendsFeatureData)

Gets or sets the value corresponding to [ILoftedBendsFeatureData::FacetingOption](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoftedBendsFeatureData~FacetingOption.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property FacetValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ILoftedBendsFeatureData
Dim value As System.Double

instance.FacetValue = value

value = instance.FacetValue
```

### C#

```csharp
System.double FacetValue {get; set;}
```

### C++/CLI

```cpp
property System.double FacetValue {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Faceting option value

## VBA Syntax

See [LoftedBendsFeatureData::FacetValue](ms-its:sldworksapivb6.chm::/sldworks~LoftedBendsFeatureData~FacetValue.html).

## Examples

See examples for [ILoftedBendsFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoftedBendsFeatureData.html).

## Remarks

This property is valid only if [ILoftedBendsFeatureData::FormedMethod](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoftedBendsFeatureData~FormedMethod.html) is false.

## See Also

[ILoftedBendsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData.html)
[ILoftedBendsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData_members.html)
[ILoftedBendsFeatureData::ReferToEndPoint Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~ReferToEndPoint.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
