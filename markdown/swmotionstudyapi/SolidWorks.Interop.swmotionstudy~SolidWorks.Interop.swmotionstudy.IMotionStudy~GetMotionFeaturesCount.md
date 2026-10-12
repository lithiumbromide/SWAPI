---
title: "GetMotionFeaturesCount Method (IMotionStudy)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IMotionStudy"
member: "GetMotionFeaturesCount"
kind: "method"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~GetMotionFeaturesCount.html"
---

# GetMotionFeaturesCount Method (IMotionStudy)

Gets the number of motion features in this motion study.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMotionFeaturesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMotionStudy
Dim value As System.Integer

value = instance.GetMotionFeaturesCount()
```

### C#

```csharp
System.int GetMotionFeaturesCount()
```

### C++/CLI

```cpp
System.int GetMotionFeaturesCount();
```

### Return Value

Number of motion features

## VBA Syntax

See [MotionStudy::GetMotionFeaturesCount](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~MotionStudy~GetMotionFeaturesCount.html).

## Examples

[Get Motion Study Properties and Results (VBA)](Get_COSMOSMotion_Motion_Study_Properties_and_Results_Example_VB.htm)

## Remarks

Call this method before calling [IMotionStudy::IGetMotionFeatures](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IMotionStudy~IGetMotionFeatures.html) to get the size of the array for that method.

## See Also

[IMotionStudy Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy.html)
[IMotionStudy Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy_members.html)
[IMotionStudy::GetMotionFeatures Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~GetMotionFeatures.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
