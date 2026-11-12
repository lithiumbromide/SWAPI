---
title: "GetTransform Method (IDerivedPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDerivedPatternFeatureData"
member: "GetTransform"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData~GetTransform.html"
---

# GetTransform Method (IDerivedPatternFeatureData)

Gets the transform for the specified instance of this derived-pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTransform( _
   ByVal Instance As System.Integer _
) As MathTransform
```

### Visual Basic (Usage)

```vb
Dim instance As IDerivedPatternFeatureData
Dim Instance As System.Integer
Dim value As MathTransform

value = instance.GetTransform(Instance)
```

### C#

```csharp
MathTransform GetTransform(
   System.int Instance
)
```

### C++/CLI

```cpp
MathTransform^ GetTransform(
   System.int Instance
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Instance`: Index of one repeating element in this pattern (see **Remarks**)

### Return Value

[Transform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html)

## VBA Syntax

See [DerivedPatternFeatureData::GetTransform](ms-its:sldworksapivb6.chm::/sldworks~DerivedPatternFeatureData~GetTransform.html).

## Remarks

To get the number of instances in this pattern, get the number of subfeatures of the pattern by traversing the FeatureManager design tree, getting the derived-pattern feature, getting the derived-pattern feature's subfeatures, and keeping count of the number of subfeatures. You can use [IModelDoc2::FirstFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~FirstFeature.html), [IFeature::GetFirstSubFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetFirstSubFeature.html), and [IFeature::GetNextSubFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetNextSubFeature.html) to traverse the FeatureManager design tree and get the derived-pattern feature's subfeatures.

Transform each instance by calling this method, setting its parameter `Instance` as follows:

1 <= `Instance` <= total number of instances in this pattern

## See Also

[IDerivedPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData.html)
[IDerivedPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData_members.html)
[IDerivedPatternFeatureData::SkippedItemArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~SkippedItemArray.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
