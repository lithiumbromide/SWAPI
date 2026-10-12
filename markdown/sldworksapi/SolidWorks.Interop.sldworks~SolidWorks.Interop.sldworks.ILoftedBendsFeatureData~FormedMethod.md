---
title: "FormedMethod Property (ILoftedBendsFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILoftedBendsFeatureData"
member: "FormedMethod"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~FormedMethod.html"
---

# FormedMethod Property (ILoftedBendsFeatureData)

Gets or sets whether this lofted bend feature is formed.

## Syntax

### Visual Basic (Declaration)

```vb
Property FormedMethod As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILoftedBendsFeatureData
Dim value As System.Boolean

instance.FormedMethod = value

value = instance.FormedMethod
```

### C#

```csharp
System.bool FormedMethod {get; set;}
```

### C++/CLI

```cpp
property System.bool FormedMethod {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if this lofted bend feature is formed, false if it is bent

## VBA Syntax

See [LoftedBendsFeatureData::FormedMethod](ms-its:sldworksapivb6.chm::/sldworks~LoftedBendsFeatureData~FormedMethod.html).

## Examples

See examples for [ILoftedBendsFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoftedBendsFeatureData.html).

## See Also

[ILoftedBendsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData.html)
[ILoftedBendsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData_members.html)
[ILoftedBendsFeatureData::FacetingOption Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~FacetingOption.html)
[ILoftedBendsFeatureData::FacetValue Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~FacetValue.html)
[ILoftedBendsFeatureData::ReferToEndPoint Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~ReferToEndPoint.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
