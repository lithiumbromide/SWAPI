---
title: "GetFireOutputTimeStepEvents Method (IMotionStudy)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IMotionStudy"
member: "GetFireOutputTimeStepEvents"
kind: "method"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~GetFireOutputTimeStepEvents.html"
---

# GetFireOutputTimeStepEvents Method (IMotionStudy)

Gets whether output time step change events are fired at output time steps or integrator time steps.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFireOutputTimeStepEvents() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMotionStudy
Dim value As System.Boolean

value = instance.GetFireOutputTimeStepEvents()
```

### C#

```csharp
System.bool GetFireOutputTimeStepEvents()
```

### C++/CLI

```cpp
System.bool GetFireOutputTimeStepEvents();
```

### Return Value

True if output time step change events are fired at output time steps; false if output time step change events are fired at integrator time steps

## VBA Syntax

See [MotionStudy::GetFireOutputTimeStepEvents](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~MotionStudy~GetFireOutputTimeStepEvents.html).

## Remarks

By default, these output time step change events are fired at integrator time steps:

- [ForceOutputTimeStepChangeNotify event](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.DMotionStudyEvents_ForceOutputTimeStepChangeNotifyEventHandler.html)
- [MotorOutputTimeStepChangeNotify event](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.DMotionStudyEvents_MotorOutputTimeStepChangeNotifyEventHandler.html)
- [OutputTimeStepChangeNotify event](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.DMotionStudyEvents_OutputTimeStepChangeNotifyEventHandler.html)

If you want to fire these events at output time steps, then set [IMotionStudy::SetFireOutputTimeStepEvents](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IMotionStudy~SetFireOutputTimeStepEvents.html) to true.

## See Also

[IMotionStudy Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy.html)
[IMotionStudy Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
