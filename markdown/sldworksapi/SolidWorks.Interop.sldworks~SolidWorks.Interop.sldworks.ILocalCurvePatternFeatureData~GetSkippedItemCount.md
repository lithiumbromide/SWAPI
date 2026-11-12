---
title: "GetSkippedItemCount Method (ILocalCurvePatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalCurvePatternFeatureData"
member: "GetSkippedItemCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~GetSkippedItemCount.html"
---

# GetSkippedItemCount Method (ILocalCurvePatternFeatureData)

Gets the number of components skipped in this curve-driven component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSkippedItemCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalCurvePatternFeatureData
Dim value As System.Integer

value = instance.GetSkippedItemCount()
```

### C#

```csharp
System.int GetSkippedItemCount()
```

### C++/CLI

```cpp
System.int GetSkippedItemCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of components skipped

## VBA Syntax

See [LocalCurvePatternFeatureData::GetSkippedItemCount](ms-its:sldworksapivb6.chm::/sldworks~LocalCurvePatternFeatureData~GetSkippedItemCount.html).

## Examples

[Create Local Curve-driven Pattern (C#)](Create_Local_Curve-driven_Pattern_Example_CSharp.htm)
[Create Local Curve-driven Pattern (VB.NET)](Create_Local_Curve-driven_Pattern_Example_VBNET.htm)
[Create Local Curve-driven Pattern (VBA)](Create_Local_Curve-driven_Pattern_Example_VB.htm)

## See Also

[ILocalCurvePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData.html)
[ILocalCurvePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData_members.html)
[ILocalCurveDrivenPatternFeature::SkippedItemArray Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~SkippedItemArray.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
