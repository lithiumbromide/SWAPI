---
title: "ExternalState Property (ISimulationForceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationForceFeatureData"
member: "ExternalState"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ExternalState.html"
---

# ExternalState Property (ISimulationForceFeatureData)

Gets or sets whether your application can listen to force-related motion study events.

## Syntax

### Visual Basic (Declaration)

```vb
Property ExternalState As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationForceFeatureData
Dim value As System.Boolean

instance.ExternalState = value

value = instance.ExternalState
```

### C#

```csharp
System.bool ExternalState {get; set;}
```

### C++/CLI

```cpp
property System.bool ExternalState {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to listen to [IMotionStudy](ms-its:swmotionstudyapi.chm::/SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IMotionStudy.html) [ForceTimeStepChangeNotify](ms-its:swmotionstudyapi.chm::/SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.DMotionStudyEvents_ForceTimeStepChangeNotifyEventHandler.html) and [ForceOutputTimeStampChangeNotify](ms-its:swmotionstudyapi.chm::/SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.DMotionStudyEvents_ForceOutputTimeStepChangeNotifyEventHandler.html) events, false to not

## VBA Syntax

See [SimulationForceFeatureData::ExternalState](ms-its:sldworksapivb6.chm::/sldworks~SimulationForceFeatureData~ExternalState.html).

## Examples

[Fire Events for External Output Time Step Changes (C#)](Fire_Events_for_External_Output_Time_Step_Changes_Example_CSharp.htm)
[Fire Events for External Output Time Step Changes (VB.NET)](Fire_Events_for_External_Output_Time_Step_Changes_Example_VBNET.htm)
[Fire Events for External Output Time Step Changes (VBA)](Fire_Events_for_External_Output_Time_Step_Changes_Example_VB.htm)

## Remarks

When a force is set to external, IMotionStudy ForceTimeStepChangeNotify and ForceOutputTimeStampChangeNotify events are called with the motor name, time, and a pointer for the return value. These events are called at every major time step from ADAMS. You can implement any force law after catching these events. The return value for each event is a double that specifies the new force or torque magnitude.

## See Also

[ISimulationForceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData.html)
[ISimulationForceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData_members.html)

## Availability

SOLIDWORKS 2008 SP1, Revision Number 16.1
