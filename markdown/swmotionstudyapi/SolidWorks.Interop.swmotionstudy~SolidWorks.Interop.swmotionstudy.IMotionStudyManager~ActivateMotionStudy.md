---
title: "ActivateMotionStudy Method (IMotionStudyManager)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IMotionStudyManager"
member: "ActivateMotionStudy"
kind: "method"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyManager~ActivateMotionStudy.html"
---

# ActivateMotionStudy Method (IMotionStudyManager)

Activates the specified study.

## Syntax

### Visual Basic (Declaration)

```vb
Function ActivateMotionStudy( _
   ByVal MotionStudyName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMotionStudyManager
Dim MotionStudyName As System.String
Dim value As System.Boolean

value = instance.ActivateMotionStudy(MotionStudyName)
```

### C#

```csharp
System.bool ActivateMotionStudy(
   System.string MotionStudyName
)
```

### C++/CLI

```cpp
System.bool ActivateMotionStudy(
   System.String^ MotionStudyName
)
```

### Parameters

- `MotionStudyName`: Name of study to activate

### Return Value

True if the specified study is activated, false if not

## VBA Syntax

See [MotionStudyManager::ActivateMotionStudy](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~MotionStudyManager~ActivateMotionStudy.html).

## Examples

[Create Motion Studies (VBA)](Create_Motion_Studies_Example_VB.htm)

## Remarks

To get the names of the available studies, you can call [IMotionStudyManager::GetMotionStudyNames](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IMotionStudyManager~GetMotionStudyNames.html) or [IMotionStudyManager::IGetMotionStudyNames](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IMotionStudyManager~IGetMotionStudyNames.html). The names of motion studies also appear on the MotionManager tabs.

## See Also

[IMotionStudyManager Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyManager.html)
[IMotionStudyManager Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyManager_members.html)
[IMotionStudyManager::CreateMotionStudy Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyManager~CreateMotionStudy.html)
[IMotionStudyManager::DeleteMotionStudy Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyManager~DeleteMotionStudy.html)
[IMotionStudyManager::GetMotionStudy Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyManager~GetMotionStudy.html)
[IMotionStudyManager::GetMotionStudyCount Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyManager~GetMotionStudyCount.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
