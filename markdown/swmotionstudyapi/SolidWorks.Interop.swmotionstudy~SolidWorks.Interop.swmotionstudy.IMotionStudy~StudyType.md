---
title: "StudyType Property (IMotionStudy)"
project: "SOLIDWORKS Motion Study API Help"
interface: "IMotionStudy"
member: "StudyType"
kind: "property"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~StudyType.html"
---

# StudyType Property (IMotionStudy)

Gets or sets the type of this study.

## Syntax

### Visual Basic (Declaration)

```vb
Property StudyType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMotionStudy
Dim value As System.Integer

instance.StudyType = value

value = instance.StudyType
```

### C#

```csharp
System.int StudyType {get; set;}
```

### C++/CLI

```cpp
property System.int StudyType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Study type as defined by [swMotionStudyType_e](SOLIDWORKS.Interop.swmotionstudy~SOLIDWORKS.Interop.swmotionstudy.swMotionStudyType_e.html); 0 if not a SOLIDWORKS Motion study

## VBA Syntax

See [MotionStudy::StudyType](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~MotionStudy~StudyType.html).

## Examples

[Create Simulation Gravity Feature (VBA)](Create_Simulation_Gravity_Feature_Example_VB.htm)
[Create Simulation Gravity Feature (VB.NET)](Create_Simulation_Gravity_Feature_Example_VBNET.htm)
[Create Simulation Gravity Feature (C#)](Create_Simulation_Gravity_Feature_Example_CSharp.htm)

## See Also

[IMotionStudy Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy.html)
[IMotionStudy Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy_members.html)
[IMotionStudy::GetSupportedStudyTypes Method](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.IMotionStudy~GetSupportedStudyTypes.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
