---
title: "CreateByRotateModel Method (IMotionStudy)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IMotionStudy"
member: "CreateByRotateModel"
kind: "method"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~CreateByRotateModel.html"
---

# CreateByRotateModel Method (IMotionStudy)

Creates an animation that rotates the model.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateByRotateModel( _
   ByVal DeleteExistingPath As System.Boolean, _
   ByVal Axis As System.Integer, _
   ByVal RotationCount As System.Integer, _
   ByVal Direction As System.Integer, _
   ByVal Duration As System.Double, _
   ByVal StartTime As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMotionStudy
Dim DeleteExistingPath As System.Boolean
Dim Axis As System.Integer
Dim RotationCount As System.Integer
Dim Direction As System.Integer
Dim Duration As System.Double
Dim StartTime As System.Double
Dim value As System.Boolean

value = instance.CreateByRotateModel(DeleteExistingPath, Axis, RotationCount, Direction, Duration, StartTime)
```

### C#

```csharp
System.bool CreateByRotateModel(
   System.bool DeleteExistingPath,
   System.int Axis,
   System.int RotationCount,
   System.int Direction,
   System.double Duration,
   System.double StartTime
)
```

### C++/CLI

```cpp
System.bool CreateByRotateModel(
   System.bool DeleteExistingPath,
   System.int Axis,
   System.int RotationCount,
   System.int Direction,
   System.double Duration,
   System.double StartTime
)
```

### Parameters

- `DeleteExistingPath`: True to delete any existing animation sequences, false to not
- `Axis`: Axis about which to rotate the model as defined by [swAnimatorAxisOfRotation_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAnimatorAxisOfRotation_e.html)
- `RotationCount`: Number of rotations
- `Direction`: Direction of rotation as defined by [swAnimatorDirectionOfRotation_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAnimatorDirectionOfRotation_e.html)
- `Duration`: Length of time of the animation in seconds
- `StartTime`: Time to start this animation (see Remarks)

### Return Value

True if the animation is created, false if not

## VBA Syntax

See [IMotionStudy::CreateByRotateModel](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~MotionStudy~CreateByRotateModel.html).

## Examples

[Duplicate, Delete, and Create Motion Study (C#)](Duplicate,_Delete,_and_Create_Motion_Study_Example_CSharp.htm)
[Duplicate, Delete, and Create Motion Study (VB.NET)](Duplicate,_Delete,_and_Create_Motion_Study_Example_VBNET.htm)
[Duplicate, Delete, and Create Motion Study (VBA)](Duplicate,_Delete,_and_Create_Motion_Study_Example_VB.htm)

## Remarks

If you have existing animation sequences, then the start time of this animation should account for the total time of all previous sequences. If this is a new animation sequence, set StartTime to 0 to start the animation immediately, or type a value to delay the start of the sequence.

Example:

```vb
' Precondition: Active document contains a part or an assembly.

Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swMotionMgr As SwMotionStudy.MotionStudyManager
Dim swMotion As SwMotionStudy.MotionStudy
Dim boolstatus As Boolean

Sub main()

Set swApp = Application.SldWorks
'
Set swModel = swApp.ActiveDoc
Set swModelDocExt = swModel.Extension
Set swMotionMgr = swModelDocExt.GetMotionStudyManager
' Create a new motion study
Set swMotion = swMotionMgr.CreateMotionStudy
' Delete any existing animation sequences,
' set the animation duration to 5 seconds, and play
' the animation immediately when IMotionStudy::Play is called
boolstatus = swMotion.CreateByRotateModel(True, swRotationAboutXAxis, 1, swRotationClockwise, 10, 0)
' Play the animation
swMotion.Play

End Sub
```

## See Also

[IMotionStudy Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy.html)
[IMotionStudy Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy_members.html)
[IMotionStudy::CreateByCollapse Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~CreateByCollapse.html)
[IMotionStudy::CreateByExplode Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~CreateByExplode.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
