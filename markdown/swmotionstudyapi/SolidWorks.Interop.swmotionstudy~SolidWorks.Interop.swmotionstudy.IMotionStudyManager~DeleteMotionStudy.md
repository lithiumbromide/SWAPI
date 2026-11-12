---
title: "DeleteMotionStudy Method (IMotionStudyManager)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IMotionStudyManager"
member: "DeleteMotionStudy"
kind: "method"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyManager~DeleteMotionStudy.html"
---

# DeleteMotionStudy Method (IMotionStudyManager)

Deletes the specified motion study.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteMotionStudy( _
   ByVal MotionStudyName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMotionStudyManager
Dim MotionStudyName As System.String
Dim value As System.Boolean

value = instance.DeleteMotionStudy(MotionStudyName)
```

### C#

```csharp
System.bool DeleteMotionStudy(
   System.string MotionStudyName
)
```

### C++/CLI

```cpp
System.bool DeleteMotionStudy(
   System.String^ MotionStudyName
)
```

### Parameters

- `MotionStudyName`: Name of motion study to delete

### Return Value

True if the motion study is deleted, false if not

## VBA Syntax

See [MotionStudyManager::DeleteMotionStudy](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~MotionStudyManager~DeleteMotionStudy.html).

## Examples

[Create Motion Studies (VBA)](Create_Motion_Studies_Example_VB.htm)

## See Also

[IMotionStudyManager Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyManager.html)
[IMotionStudyManager Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyManager_members.html)
[IMotionStudyManager::CreateMotionStudy Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyManager~CreateMotionStudy.html)
[IMotionStudyManager::GetMotionStudy Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyManager~GetMotionStudy.html)
[IMotionStudyManager::GetMotionStudyCount Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyManager~GetMotionStudyCount.html)
[IMotionStudyManager::GetMotionStudyNames Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyManager~GetMotionStudyNames.html)
[IMotionStudyManager::IGetMotionStudyNames Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyManager~IGetMotionStudyNames.html)
[IMotionStudyManager::ActivateMotionStudy Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyManager~ActivateMotionStudy.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
