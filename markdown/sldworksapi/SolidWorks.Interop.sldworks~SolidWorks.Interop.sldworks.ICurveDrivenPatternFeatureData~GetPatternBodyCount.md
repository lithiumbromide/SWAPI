---
title: "GetPatternBodyCount Method (ICurveDrivenPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICurveDrivenPatternFeatureData"
member: "GetPatternBodyCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~GetPatternBodyCount.html"
---

# GetPatternBodyCount Method (ICurveDrivenPatternFeatureData)

Gets the number of seed bodies in this curve-driven pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPatternBodyCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICurveDrivenPatternFeatureData
Dim value As System.Integer

value = instance.GetPatternBodyCount()
```

### C#

```csharp
System.int GetPatternBodyCount()
```

### C++/CLI

```cpp
System.int GetPatternBodyCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of seed bodies

## VBA Syntax

See [CurveDrivenPatternFeatureData::GetPatternBodyCount](ms-its:sldworksapivb6.chm::/sldworks~CurveDrivenPatternFeatureData~GetPatternBodyCount.html).

## Examples

[Create and Access Curve-driven Pattern Feature (C#)](Create_and_Access_Curve-driven_Pattern_Feature_Example_CSharp.htm)
[Create and Access Curve-driven Pattern Feature (VB.NET)](Create_and_Access_Curve-driven_Pattern_Feature_Example_VBNET.htm)
[Create and Access Curve-driven Pattern Feature (VBA)](Create_and_Access_Curve-driven_Pattern_Feature_Example_VB.htm)

## See Also

[ICurveDrivenPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData.html)
[ICurveDrivenPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData_members.html)
[ICurveDrivenPatternFeatureData::IGetPatternBodyArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~IGetPatternBodyArray.html)
[ICurveDrivenPatternFeatureData::ISetPatternBodyArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~ISetPatternBodyArray.html)
[ICurveDrivenPatternFeatureData::PatternBodyArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~PatternBodyArray.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
