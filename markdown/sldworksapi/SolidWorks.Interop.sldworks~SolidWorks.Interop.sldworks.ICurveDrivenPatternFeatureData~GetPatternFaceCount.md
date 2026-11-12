---
title: "GetPatternFaceCount Method (ICurveDrivenPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICurveDrivenPatternFeatureData"
member: "GetPatternFaceCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~GetPatternFaceCount.html"
---

# GetPatternFaceCount Method (ICurveDrivenPatternFeatureData)

Gets a list of pattern faces for this curve-driven pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPatternFaceCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICurveDrivenPatternFeatureData
Dim value As System.Integer

value = instance.GetPatternFaceCount()
```

### C#

```csharp
System.int GetPatternFaceCount()
```

### C++/CLI

```cpp
System.int GetPatternFaceCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of faces

## VBA Syntax

See [CurveDrivenPatternFeatureData::GetPatternFaceCount](ms-its:sldworksapivb6.chm::/sldworks~CurveDrivenPatternFeatureData~GetPatternFaceCount.html).

## See Also

[ICurveDrivenPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData.html)
[ICurveDrivenPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData_members.html)
[ICurveDrivenPatternFeatureData::IGetPatternFaceArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~IGetPatternFaceArray.html)
[ICurveDrivenPatternFeatureData::ISetPatternFaceArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~ISetPatternFaceArray.html)
[ICurveDrivenPatternFeatureData::PatternFaceArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~PatternFaceArray.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
