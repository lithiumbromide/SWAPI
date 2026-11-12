---
title: "Calculate Method (IMotionStudy)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IMotionStudy"
member: "Calculate"
kind: "method"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~Calculate.html"
---

# Calculate Method (IMotionStudy)

Performs the calculation for this motion study.

## Syntax

### Visual Basic (Declaration)

```vb
Function Calculate() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMotionStudy
Dim value As System.Boolean

value = instance.Calculate()
```

### C#

```csharp
System.bool Calculate()
```

### C++/CLI

```cpp
System.bool Calculate();
```

### Return Value

True if the calculation is performed, false if not

## VBA Syntax

See [MotionStudy::Calculate](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~MotionStudy~Calculate.html).

## Examples

[Create Plots and Get Values (C#)](Create_Plots_and_Get_Values_Example_CSharp.htm)
[Create Plots and Get Values (VB.NET)](Create_Plots_and_Get_Values_Example_VBNET.htm)
[Create Plots and Get Values (VBA)](Create_Plots_and_Get_Values_Example_VB.htm)
[Duplicate, Delete, and Create Motion Study (C#)](Duplicate,_Delete,_and_Create_Motion_Study_Example_CSharp.htm)
[Duplicate, Delete, and Create Motion Study (VB.NET)](Duplicate,_Delete,_and_Create_Motion_Study_Example_VBNET.htm)
[Duplicate, Delete, and Create Motion Study (VBA)](Duplicate,_Delete,_and_Create_Motion_Study_Example_VB.htm)

## Remarks

You can only use this method on an active motion study. To determine whether a motion study is active, use [IMotionStudy::IsActive](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IMotionStudy~IsActive.html).

## See Also

[IMotionStudy Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy.html)
[IMotionStudy Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
