---
title: "GetMotionStudy Method (IMotionStudyManager)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IMotionStudyManager"
member: "GetMotionStudy"
kind: "method"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyManager~GetMotionStudy.html"
---

# GetMotionStudy Method (IMotionStudyManager)

Gets the specified motion study.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMotionStudy( _
   ByVal MotionStudyName As System.String _
) As MotionStudy
```

### Visual Basic (Usage)

```vb
Dim instance As IMotionStudyManager
Dim MotionStudyName As System.String
Dim value As MotionStudy

value = instance.GetMotionStudy(MotionStudyName)
```

### C#

```csharp
MotionStudy GetMotionStudy(
   System.string MotionStudyName
)
```

### C++/CLI

```cpp
MotionStudy^ GetMotionStudy(
   System.String^ MotionStudyName
)
```

### Parameters

- `MotionStudyName`: Name of motion study to get

### Return Value

[Motion study](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IMotionStudy.html)

## VBA Syntax

See [IMotionStudyManager::GetMotionStudy](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~MotionStudyManager~GetMotionStudy.html).

## Examples

[Create Motion Studies (VBA)](Create_Motion_Studies_Example_VB.htm)
[Get Motion Study Properties and Results (VBA)](Get_COSMOSMotion_Motion_Study_Properties_and_Results_Example_VB.htm)
[Add Spring to Motion Study (C#)](Add_Spring_to_Motion_Study_Example_CSharp.htm)
[Add Spring to Motion Study (VB.NET)](Add_Spring_to_Motion_Study_Example_VBNET.htm)
[Add Spring to Motion Study (VBA)](Add_Spring_to_Motion_Study_Example_VB.htm)
[Duplicate, Delete, and Create Motion Study (C#)](Duplicate,_Delete,_and_Create_Motion_Study_Example_CSharp.htm)
[Duplicate, Delete, and Create Motion Study (VB.NET)](Duplicate,_Delete,_and_Create_Motion_Study_Example_VBNET.htm)
[Duplicate, Delete, and Create Motion Study (VBA)](Duplicate,_Delete,_and_Create_Motion_Study_Example_VB.htm)

## Remarks

This method gets the names of both SOLIDWORKS Simulation and SOLIDWORKS Motion studies. Use [IMotionStudy::StudyType](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~StudyType.html) to ensure that a given study is a motion study before using other Motion APIs.

To get the names of the available motion studies, you can call [IMotionStudyManager::GetMotionStudyNames](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IMotionStudyManager~GetMotionStudyNames.html) or [IMotionStudyManager::IGetMotionStudyNames](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IMotionStudyManager~IGetMotionStudyNames.html). The names of motion studies also appear on the MotionManager tabs.

## See Also

[IMotionStudyManager Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyManager.html)
[IMotionStudyManager Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyManager_members.html)
[IMotionStudyManager::ActivateMotionStudy Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyManager~ActivateMotionStudy.html)
[IMotionStudyManager::CreateMotionStudy Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyManager~CreateMotionStudy.html)
[IMotionStudyManager::DeleteMotionStudy Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyManager~DeleteMotionStudy.html)
[IMotionStudyManager::GetMotionStudyCount Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyManager~GetMotionStudyCount.html)
[IMotionStudyManager::GetMotionStudy Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyManager~GetMotionStudy.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
