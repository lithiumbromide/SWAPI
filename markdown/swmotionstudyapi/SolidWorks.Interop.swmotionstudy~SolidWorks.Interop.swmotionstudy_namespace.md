---
title: "SolidWorks.Interop.swmotionstudy Namespace"
project: "SOLIDWORKS Motion Study API Help"
interface: "SolidWorks.Interop.swmotionstudy"
member: ""
kind: "namespace"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy_namespace.html"
---

# SolidWorks.Interop.swmotionstudy Namespace

SOLIDWORKS Motion Study API

## Interfaces

| Interface | Description |
| --- | --- |
| IAVIParameter | Allows access to the parameters of a file containing an animation. |
| ICosmosMotionStudyProperties | Allows access to a motion study's properties. |
| ICosmosMotionStudyResults | Allows access to a motion study's results. |
| IMotionPlotFeatureOutput | Allows access to a plot's values. |
| IMotionStudy | Allows access to a SOLIDWORKS motion study's results. |
| IMotionStudyManager | Allows access to the MotionManager. |
| IMotionStudyProperties | Allows access to a SOLIDWORKS motion study's properties. |
| IMotionStudyResults | Allows access to a SOLIDWORKS motion study's results. |
| IPhysicalSimulationMotionStudyProperties | Allows access to a Physical Simulation motion study's properties. |

## Delegates

| Delegate | Description |
| --- | --- |
| DMotionStudyEvents_ForceOutputTimeStepChangeNotifyEventHandler | Fired at every integrator or output time step when a motion simulation is occurring and external forces exist. |
| DMotionStudyEvents_ForceTimeStepChangeNotifyEventHandler | Fired when a motion study is calculated and there are external forces. |
| DMotionStudyEvents_MotorOutputTimeStepChangeNotifyEventHandler | Fired at every integrator or output time step when a motion simulation is occurring and external motors exist. |
| DMotionStudyEvents_MotorTimeStepChangeNotifyEventHandler | Fired when a motion study is calculated and there are external motors . |
| DMotionStudyEvents_OutputTimeStepChangeNotifyEventHandler | Fired at every integrator or output time step when a motion simulation is occurring. |
| DMotionStudyEvents_PartCollideNotifyEventHandler | Fired when a collision between two components occurs. |
| DMotionStudyEvents_SpecialMotionEventNotifyEventHandler | Fired for motion-related special events, such as contacts. |
| DMotionStudyEvents_StartCalculateNotifyEventHandler | Fired when a motion study is calculated . |
| DMotionStudyEvents_StopCalculateNotifyEventHandler | Fired when a motion study's calculation ends. |

## Enumerations

| Enumeration | Description |
| --- | --- |
| swMotionIntegratorType_e | Integration methods for solving numerically stiff systems. |
| swMotionStudyNotify_e | To receive notifications, a DLL application must register for the notifications by object type. This registration must be done for each instance of a particular object. |
| swMotionStudyType_e | Motion study types. Bitmask . |
| swSaveAVIImageSize_e | AVI image sizes. |
| swSpecialMotionEventType_e | Motion-related special events. |

## See Also

[SolidWorks.Interop.swmotionstudy Assembly](SolidWorks.Interop.swmotionstudy.html)
