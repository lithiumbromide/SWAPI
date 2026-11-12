---
title: "swMotionStudyNotify_e Enumeration"
project: "SOLIDWORKS Motion Study API Help"
interface: "swMotionStudyNotify_e"
member: ""
kind: "enum"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.swMotionStudyNotify_e.html"
---

# swMotionStudyNotify_e Enumeration

To receive notifications, a DLL application must register for the notifications by object type. This registration must be done for each instance of a particular object.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swMotionStudyNotify_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swMotionStudyNotify_e
```

### C#

```csharp
public enum swMotionStudyNotify_e : System.Enum
```

### C++/CLI

```cpp
public enum class swMotionStudyNotify_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swMotionStudyForceOutputTimeStepChangeNotify | 7= ForceOutputTimeStepChangeNotify |
| swMotionStudyForceTimeStepChangeNotify | 2= ForceTimeStepChangeNotify |
| swMotionStudyMotorOutputTimeStepChangeNotify | 4= MotorOutputTimeStepChangeNotify |
| swMotionStudyMotorTimeStepChangeNotify | 1= MotorTimeStepChangeNotify |
| swMotionStudyOutputTimeStepChangeNotify | 9 = OutputTimeStepChangeNotify |
| swMotionStudyPartCollideNotify | 3 = PartCollideNotify |
| swMotionStudySpecialEventNotify | 8 = SpecialMotionEventNotify |
| swMotionStudyStartCalculateNotify | 5 = StartCalculateNotify |
| swMotionStudyStopCalculateNotify | 6 = StopCalculateNotify |

## Remarks

If developing a C++ application, use the previously listed enumerators to register for notifications for these [IMotionStudy](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IMotionStudy.html) events.

## See Also

[SolidWorks.Interop.swmotionstudy Namespace](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy_namespace.html)
