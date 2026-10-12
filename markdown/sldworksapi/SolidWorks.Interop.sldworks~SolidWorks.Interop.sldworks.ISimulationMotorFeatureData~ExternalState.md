---
title: "ExternalState Property (ISimulationMotorFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationMotorFeatureData"
member: "ExternalState"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~ExternalState.html"
---

# ExternalState Property (ISimulationMotorFeatureData)

Gets or sets whether your application can listen to motor-related motion study event.

## Syntax

### Visual Basic (Declaration)

```vb
Property ExternalState As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationMotorFeatureData
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

True to listen to [IMotionStudy](ms-its:swmotionstudyapi.chm::/SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IMotionStudy.html) [MotorTimeStepChangeNotify](ms-its:swmotionstudyapi.chm::/SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.DMotionStudyEvents_MotorTimeStepChangeNotifyEventHandler.html) and [MotorOutputTimeStepChangeNotify](ms-its:swmotionstudyapi.chm::/SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.DMotionStudyEvents_MotorOutputTimeStepChangeNotifyEventHandler.html), false to not

## VBA Syntax

See [SimulationMotorFeatureData::ExternalState](ms-its:sldworksapivb6.chm::/sldworks~SimulationMotorFeatureData~ExternalState.html).

## Examples

[Fire Events for External Output Time Step Changes (C#)](Fire_Events_for_External_Output_Time_Step_Changes_Example_CSharp.htm)
[Fire Events for External Output Time Step Changes (VB.NET)](Fire_Events_for_External_Output_Time_Step_Changes_Example_VBNET.htm)
[Fire Events for External Output Time Step Changes (VBA)](Fire_Events_for_External_Output_Time_Step_Changes_Example_VB.htm)

## Remarks

When a motor's state is set to external, IMotionStudy MotorTimeStepChangeNotify and MotorOutputTimeStepChangeNotify events are called with the motor name, time, and a pointer for the return value. These events are called at every major step from ADAMS. You can implement any motion law after catching these events. The return value for each event is a double that specifies the new motor speed.

## See Also

[ISimulationMotorFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData.html)
[ISimulationMotorFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData_members.html)

## Availability

SOLIDWORKS 2008 SP1, Revision Number 16.1
