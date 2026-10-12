---
title: "GetPatternFeatureCount Method (ICurveDrivenPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICurveDrivenPatternFeatureData"
member: "GetPatternFeatureCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~GetPatternFeatureCount.html"
---

# GetPatternFeatureCount Method (ICurveDrivenPatternFeatureData)

Gets the number of seed features for this curve-driven pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPatternFeatureCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICurveDrivenPatternFeatureData
Dim value As System.Integer

value = instance.GetPatternFeatureCount()
```

### C#

```csharp
System.int GetPatternFeatureCount()
```

### C++/CLI

```cpp
System.int GetPatternFeatureCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of features

## VBA Syntax

See [CurveDrivenPatternFeatureData::GetPatternFeatureCount](ms-its:sldworksapivb6.chm::/sldworks~CurveDrivenPatternFeatureData~GetPatternFeatureCount.html).

## Examples

[Create and Access Curve-driven Pattern Feature (C#)](Create_and_Access_Curve-driven_Pattern_Feature_Example_CSharp.htm)
[Create and Access Curve-driven Pattern Feature (VB.NET)](Create_and_Access_Curve-driven_Pattern_Feature_Example_VBNET.htm)
[Create and Access Curve-driven Pattern Feature (VBA)](Create_and_Access_Curve-driven_Pattern_Feature_Example_VB.htm)

## See Also

[ICurveDrivenPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData.html)
[ICurveDrivenPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData_members.html)
[ICurveDrivenPatternFeatureData::IGetPatternFeatureArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~IGetPatternFeatureArray.html)
[ICurveDrivenPatternFeatureData::ISetPatternFeatureArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~ISetPatternFeatureArray.html)
[ICurveDrivenPatternFeatureData::PatternFeatureArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~PatternFeatureArray.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
