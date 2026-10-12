---
title: "ReferToEndPoint Property (ILoftedBendsFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILoftedBendsFeatureData"
member: "ReferToEndPoint"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~ReferToEndPoint.html"
---

# ReferToEndPoint Property (ILoftedBendsFeatureData)

Gets or sets whether to calculate facet transitions using theoretical vertexes.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReferToEndPoint As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILoftedBendsFeatureData
Dim value As System.Boolean

instance.ReferToEndPoint = value

value = instance.ReferToEndPoint
```

### C#

```csharp
System.bool ReferToEndPoint {get; set;}
```

### C++/CLI

```cpp
property System.bool ReferToEndPoint {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to calculate facet transitions using theoretical vertexes, false to calculate them using the smallest possible arcs that avoid interference between bend areas

## VBA Syntax

See [LoftedBendsFeatureData::ReferToEndPoint](ms-its:sldworksapivb6.chm::/sldworks~LoftedBendsFeatureData~ReferToEndPoint.html).

## Examples

See examples for [ILoftedBendsFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoftedBendsFeatureData.html).

## Remarks

This property is valid only if [ILoftedBendsFeatureData::FormedMethod](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoftedBendsFeatureData~FormedMethod.html) is false.

## See Also

[ILoftedBendsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData.html)
[ILoftedBendsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData_members.html)
[ILoftedBendsFeatureData::FacetingOption Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~FacetingOption.html)
[ILoftedBendsFeatureData::FacetValue Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~FacetValue.html)
[ILoftedBendsFeatureData::FormedMethod Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~FormedMethod.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
