---
title: "IGetMotionFeatures Method (IMotionStudy)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IMotionStudy"
member: "IGetMotionFeatures"
kind: "method"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~IGetMotionFeatures.html"
---

# IGetMotionFeatures Method (IMotionStudy)

Gets the motion features in this motion study.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetMotionFeatures( _
   ByVal Count As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMotionStudy
Dim Count As System.Integer
Dim value As System.Object

value = instance.IGetMotionFeatures(Count)
```

### C#

```csharp
System.object IGetMotionFeatures(
   System.int Count
)
```

### C++/CLI

```cpp
System.Object^ IGetMotionFeatures(
   System.int Count
)
```

### Parameters

- `Count`: Number of motion features in this motion study

### Return Value

Array of motion features in this motion study

## VBA Syntax

See [MotionStudy::IGetMotionFeatures](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~MotionStudy~IGetMotionFeatures.html).

## Remarks

Before calling this method, call [IMotionStudy::GetMotionFeaturesCount](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IMotionStudy~GetMotionFeaturesCount.html) to get the value of Count.

## See Also

[IMotionStudy Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy.html)
[IMotionStudy Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy_members.html)
[IMotionStudy::GetMotionFeatures Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~GetMotionFeatures.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
