---
title: "SetFireOutputTimeStepEvents Method (IMotionStudy)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IMotionStudy"
member: "SetFireOutputTimeStepEvents"
kind: "method"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~SetFireOutputTimeStepEvents.html"
---

# SetFireOutputTimeStepEvents Method (IMotionStudy)

Sets whether output time step change events are fired at output time steps or integrator time steps.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetFireOutputTimeStepEvents( _
   ByVal FireOutputEvents As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IMotionStudy
Dim FireOutputEvents As System.Boolean

instance.SetFireOutputTimeStepEvents(FireOutputEvents)
```

### C#

```csharp
void SetFireOutputTimeStepEvents(
   System.bool FireOutputEvents
)
```

### C++/CLI

```cpp
void SetFireOutputTimeStepEvents(
   System.bool FireOutputEvents
)
```

### Parameters

- `FireOutputEvents`: True if output time step change events are fired at output time steps; false if output time step change events are fired at integrator time steps

## VBA Syntax

See [MotionStudy::SetFireOutputTimeStepEvents](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~MotionStudy~SetFireOutputTimeStepEvents.html).

## Examples

[Fire Events for External Output Time Step Changes (C#)](Fire_Events_for_External_Output_Time_Step_Changes_Example_CSharp.htm)
[Fire Events for External Output Time Step Changes (VB.NET)](Fire_Events_for_External_Output_Time_Step_Changes_Example_VBNET.htm)
[Fire Events for External Output Time Step Changes (VBA)](Fire_Events_for_External_Output_Time_Step_Changes_Example_VB.htm)

## Remarks

By default, these output time step change events are fired at integrator time steps:

- [ForceOutputTimeStepChangeNotify event](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.DMotionStudyEvents_ForceOutputTimeStepChangeNotifyEventHandler.html)
- [MotorOutputTimeStepChangeNotify event](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.DMotionStudyEvents_MotorOutputTimeStepChangeNotifyEventHandler.html)
- [OutputTimeStepChangeNotify event](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.DMotionStudyEvents_OutputTimeStepChangeNotifyEventHandler.html)

If you want to fire these events at output time steps, then set this method to true.

## See Also

[IMotionStudy Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy.html)
[IMotionStudy Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy_members.html)
[IMotionStudy::GetFireOutputTimeStepEvents Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~GetFireOutputTimeStepEvents.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
