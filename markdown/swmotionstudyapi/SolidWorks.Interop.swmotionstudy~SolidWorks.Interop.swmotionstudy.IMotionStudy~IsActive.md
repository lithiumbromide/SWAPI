---
title: "IsActive Property (IMotionStudy)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IMotionStudy"
member: "IsActive"
kind: "property"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~IsActive.html"
---

# IsActive Property (IMotionStudy)

Gets whether this motion study is active.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property IsActive As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMotionStudy
Dim value As System.Boolean

value = instance.IsActive
```

### C#

```csharp
System.bool IsActive {get;}
```

### C++/CLI

```cpp
property System.bool IsActive {
   System.bool get();
}
```

### Property Value

True if the motion study is active, false if not

## VBA Syntax

See [MotionStudy::IsActive](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~MotionStudy~IsActive.html).

## Examples

[Get Motion Study Properties and Results (VBA)](Get_COSMOSMotion_Motion_Study_Properties_and_Results_Example_VB.htm)
[Fire Events for External Output Time Step Changes (C#)](Fire_Events_for_External_Output_Time_Step_Changes_Example_CSharp.htm)
[Fire Events for External Output Time Step Changes (VB.NET)](Fire_Events_for_External_Output_Time_Step_Changes_Example_VBNET.htm)
[Fire Events for External Output Time Step Changes (VBA)](Fire_Events_for_External_Output_Time_Step_Changes_Example_VB.htm)
[Duplicate, Delete, and Create Motion Study (C#)](Duplicate,_Delete,_and_Create_Motion_Study_Example_CSharp.htm)
[Duplicate, Delete, and Create Motion Study (VB.NET)](Duplicate,_Delete,_and_Create_Motion_Study_Example_VBNET.htm)
[Duplicate, Delete, and Create Motion Study (VBA)](Duplicate,_Delete,_and_Create_Motion_Study_Example_VB.htm)

## Remarks

To activate an inactive motion study, call [IMotionStudy::Activate](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IMotionStudy~Activate.html).

## See Also

[IMotionStudy Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy.html)
[IMotionStudy Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
