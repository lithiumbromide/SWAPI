---
title: "SetDuration Method (IMotionStudy)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IMotionStudy"
member: "SetDuration"
kind: "method"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~SetDuration.html"
---

# SetDuration Method (IMotionStudy)

Sets the duration, in seconds, of this motion study.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetDuration( _
   ByVal Time As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMotionStudy
Dim Time As System.Double
Dim value As System.Boolean

value = instance.SetDuration(Time)
```

### C#

```csharp
System.bool SetDuration(
   System.double Time
)
```

### C++/CLI

```cpp
System.bool SetDuration(
   System.double Time
)
```

### Parameters

- `Time`: Duration, in seconds, of this motion study

### Return Value

True if the duration is set, false if not

## VBA Syntax

See [MotionStudy::SetDuration](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~MotionStudy~SetDuration.html).

## Examples

[Duplicate, Delete, and Create Motion Study (C#)](Duplicate,_Delete,_and_Create_Motion_Study_Example_CSharp.htm)
[Duplicate, Delete, and Create Motion Study (VB.NET)](Duplicate,_Delete,_and_Create_Motion_Study_Example_VBNET.htm)
[Duplicate, Delete, and Create Motion Study (VBA)](Duplicate,_Delete,_and_Create_Motion_Study_Example_VB.htm)

## See Also

[IMotionStudy Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy.html)
[IMotionStudy Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy_members.html)
[IMotionStudy::GetDuration Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~GetDuration.html)
[IMotionStudy::GetTime Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~GetTime.html)
[IMotionStudy::SetTime Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~SetTime.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
