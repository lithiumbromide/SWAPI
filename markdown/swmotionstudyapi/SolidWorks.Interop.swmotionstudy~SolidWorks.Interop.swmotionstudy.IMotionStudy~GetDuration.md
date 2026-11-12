---
title: "GetDuration Method (IMotionStudy)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IMotionStudy"
member: "GetDuration"
kind: "method"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~GetDuration.html"
---

# GetDuration Method (IMotionStudy)

Gets the duration, in seconds, of the motion study.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDuration() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMotionStudy
Dim value As System.Double

value = instance.GetDuration()
```

### C#

```csharp
System.double GetDuration()
```

### C++/CLI

```cpp
System.double GetDuration();
```

### Return Value

Duration, in seconds, of motion study

## VBA Syntax

See [MotionStudy::GetDuration](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~MotionStudy~GetDuration.html).

## Examples

[Get Motion Study Properties and Results (VBA)](Get_COSMOSMotion_Motion_Study_Properties_and_Results_Example_VB.htm)
[Duplicate, Delete, and Create Motion Study (C#)](Duplicate,_Delete,_and_Create_Motion_Study_Example_CSharp.htm)
[Duplicate, Delete, and Create Motion Study (VB.NET)](Duplicate,_Delete,_and_Create_Motion_Study_Example_VBNET.htm)
[Duplicate, Delete, and Create Motion Study (VBA)](Duplicate,_Delete,_and_Create_Motion_Study_Example_VB.htm)

## See Also

[IMotionStudy Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy.html)
[IMotionStudy Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy_members.html)
[IMotionStudy::GetTime Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~GetTime.html)
[IMotionStudy::SetDuration Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~SetDuration.html)
[IMotionStudy::SetTime Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~SetTime.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
