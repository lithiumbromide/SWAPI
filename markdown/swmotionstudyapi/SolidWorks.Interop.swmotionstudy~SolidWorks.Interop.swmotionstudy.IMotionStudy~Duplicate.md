---
title: "Duplicate Method (IMotionStudy)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IMotionStudy"
member: "Duplicate"
kind: "method"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~Duplicate.html"
---

# Duplicate Method (IMotionStudy)

Creates a new motion study based on the specified motion study.

## Syntax

### Visual Basic (Declaration)

```vb
Function Duplicate() As MotionStudy
```

### Visual Basic (Usage)

```vb
Dim instance As IMotionStudy
Dim value As MotionStudy

value = instance.Duplicate()
```

### C#

```csharp
MotionStudy Duplicate()
```

### C++/CLI

```cpp
MotionStudy^ Duplicate();
```

### Return Value

Duplicated [motion study](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.IMotionStudy.html)

## VBA Syntax

See [MotionStudy::Duplicate](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~MotionStudy~Duplicate.html).

## Examples

[Duplicate, Delete, and Create Motion Study (C#)](Duplicate,_Delete,_and_Create_Motion_Study_Example_CSharp.htm)
[Duplicate, Delete, and Create Motion Study (VB.NET)](Duplicate,_Delete,_and_Create_Motion_Study_Example_VBNET.htm)
[Duplicate, Delete, and Create Motion Study (VBA)](Duplicate,_Delete,_and_Create_Motion_Study_Example_VB.htm)

## Remarks

The name of the duplicated motion study is Motion Study followed by a number. The number for the duplicated motion study is determined by incrementing the number of the Motion Study with the highest number by 1 and adding that number to the duplicated motion study's name (e.g., only Motion Study 1 exists; duplicated motion study's name is Motion Study 2).

## See Also

[IMotionStudy Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy.html)
[IMotionStudy Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
