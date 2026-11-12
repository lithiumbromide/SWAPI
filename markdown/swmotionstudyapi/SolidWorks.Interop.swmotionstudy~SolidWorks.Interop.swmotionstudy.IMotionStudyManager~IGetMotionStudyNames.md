---
title: "IGetMotionStudyNames Method (IMotionStudyManager)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IMotionStudyManager"
member: "IGetMotionStudyNames"
kind: "method"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyManager~IGetMotionStudyNames.html"
---

# IGetMotionStudyNames Method (IMotionStudyManager)

Gets the names of the studies for this model.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetMotionStudyNames( _
   ByVal Count As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IMotionStudyManager
Dim Count As System.Integer
Dim value As System.String

value = instance.IGetMotionStudyNames(Count)
```

### C#

```csharp
System.string IGetMotionStudyNames(
   System.int Count
)
```

### C++/CLI

```cpp
System.String^ IGetMotionStudyNames(
   System.int Count
)
```

### Parameters

- `Count`: Number of studies for this model

### Return Value

Names of the studies for this model

## VBA Syntax

See [MotionStudyManager::IGetMotionStudyNames](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~MotionStudyManager~IGetMotionStudyNames.html).

## Remarks

This method gets the names of both SOLIDWORKS Simulation and SOLIDWORKS Motion studies. Use [IMotionStudy::StudyType](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~StudyType.html) to ensure that a given study is a motion study before using other Motion APIs.

Before calling this method, call [IMotionStudyManager::GetMotionStudyCount](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IMotionStudyManager~GetMotionStudyCount.html) to get the size of Count.

## See Also

[IMotionStudyManager Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyManager.html)
[IMotionStudyManager Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyManager_members.html)
[IMotionStudyManager::GetMotionStudyNames Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyManager~GetMotionStudyNames.html)
[IMotionStudyManager::GetMotionStudy Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyManager~GetMotionStudy.html)
[IMotionStudyManager::DeleteMotionStudy Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyManager~DeleteMotionStudy.html)
[IMotionStudyManager::CreateMotionStudy Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyManager~CreateMotionStudy.html)
[IMotionStudyManager::ActivateMotionStudy Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyManager~ActivateMotionStudy.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
