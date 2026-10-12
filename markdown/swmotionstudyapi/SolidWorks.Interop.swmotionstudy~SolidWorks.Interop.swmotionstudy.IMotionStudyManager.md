---
title: "IMotionStudyManager Interface"
project: "SOLIDWORKS Motion Study API Help"
interface: "IMotionStudyManager"
member: ""
kind: "interface"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyManager.html"
---

# IMotionStudyManager Interface

Allows access to the MotionManager.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IMotionStudyManager
```

### Visual Basic (Usage)

```vb
Dim instance As IMotionStudyManager
```

### C#

```csharp
public interface IMotionStudyManager
```

### C++/CLI

```cpp
public interface class IMotionStudyManager
```

## VBA Syntax

See [MotionStudyManager](ms-its:swmotionstudyapivb6.chm::/swmotionstudy~MotionStudyManager.html).

## Examples

[Create Motion Studies (VBA)](Create_Motion_Studies_Example_VB.htm)
[Create Plots and Get Values (C#)](Create_Plots_and_Get_Values_Example_CSharp.htm)
[Create Plots and Get Values (VB.NET)](Create_Plots_and_Get_Values_Example_VBNET.htm)
[Create Plots and Get Values (VBA)](Create_Plots_and_Get_Values_Example_VB.htm)
[Duplicate, Delete, and Create Motion Study (C#)](Duplicate,_Delete,_and_Create_Motion_Study_Example_CSharp.htm)
[Duplicate, Delete, and Create Motion Study (VB.NET)](Duplicate,_Delete,_and_Create_Motion_Study_Example_VBNET.htm)
[Duplicate, Delete, and Create Motion Study (VBA)](Duplicate,_Delete,_and_Create_Motion_Study_Example_VB.htm)

## Remarks

The getters of this interface return all studies currently defined, SOLIDWORKS Motion studies as well as SOLIDWORKS Simulation studies. Use [IMotionStudy::StudyType](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~StudyType.html) to ensure that a given study is a motion study before using other Motion APIs.

## Accessors

[IModelDocExtension::GetMotionStudyManager](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetMotionStudyManager.html)

## See Also

[IMotionStudyManager Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudyManager_members.html)
[SolidWorks.Interop.swmotionstudy Namespace](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy_namespace.html)
[IAVIParameter Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IAVIParameter.html)
[IMotionStudy Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy.html)
