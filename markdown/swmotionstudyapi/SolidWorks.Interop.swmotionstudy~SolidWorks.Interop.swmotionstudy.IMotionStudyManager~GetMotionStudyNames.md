---
title: "GetMotionStudyNames Method (IMotionStudyManager)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IMotionStudyManager"
member: "GetMotionStudyNames"
kind: "method"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyManager~GetMotionStudyNames.html"
---

# GetMotionStudyNames Method (IMotionStudyManager)

Gets the names of the studies for this model.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMotionStudyNames() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMotionStudyManager
Dim value As System.Object

value = instance.GetMotionStudyNames()
```

### C#

```csharp
System.object GetMotionStudyNames()
```

### C++/CLI

```cpp
System.Object^ GetMotionStudyNames();
```

### Return Value

Names of the studies for this model

## VBA Syntax

See [MotionStudyManager::GetMotionStudyNames](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~MotionStudyManager~GetMotionStudyNames.html).

## Examples

[Create Motion Studies (VBA)](Create_Motion_Studies_Example_VB.htm)

## Remarks

This method gets the names of both SOLIDWORKS Simulation and SOLIDWORKS Motion studies. Use [IMotionStudy::StudyType](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~StudyType.html) to ensure that a given study is a motion study before using other Motion APIs.

## See Also

[IMotionStudyManager Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyManager.html)
[IMotionStudyManager Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyManager_members.html)
[IMotionStudyManager::IGetMotionStudyNames Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyManager~IGetMotionStudyNames.html)
[IMotionStudyManager::GetMotionStudyCount Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyManager~GetMotionStudyCount.html)
[IMotionStudyManager::GetMotionStudy Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyManager~GetMotionStudy.html)
[IMotionStudyManager::DeleteMotionStudy Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyManager~DeleteMotionStudy.html)
[IMotionStudyManager::CreateMotionStudy Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyManager~CreateMotionStudy.html)
[IMotionStudyManager::ActivateMotionStudy Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyManager~ActivateMotionStudy.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
