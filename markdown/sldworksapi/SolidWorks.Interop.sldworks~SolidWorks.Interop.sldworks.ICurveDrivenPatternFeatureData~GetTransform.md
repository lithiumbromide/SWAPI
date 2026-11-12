---
title: "GetTransform Method (ICurveDrivenPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICurveDrivenPatternFeatureData"
member: "GetTransform"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~GetTransform.html"
---

# GetTransform Method (ICurveDrivenPatternFeatureData)

Gets the transform for the specified instance of this curve-driven pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTransform( _
   ByVal Instance As System.Integer _
) As MathTransform
```

### Visual Basic (Usage)

```vb
Dim instance As ICurveDrivenPatternFeatureData
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

See [CurveDrivenPatternFeatureData::GetTransform](ms-its:sldworksapivb6.chm::/sldworks~CurveDrivenPatternFeatureData~GetTransform.html).

## Remarks

1 <= `Instance` <= ([ICurveDrivenPatternFeatureData::D1InstanceCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurveDrivenPatternFeatureData~D1InstanceCount.html) + [ICurveDrivenPatternFeatureData::D2InstanceCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurveDrivenPatternFeatureData~D2InstanceCount.html))

## See Also

[ICurveDrivenPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData.html)
[ICurveDrivenPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData_members.html)
[ICurveDrivenPatternFeatureData::SkippedItemArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~SkippedItemArray.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
