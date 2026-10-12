---
title: "WireFrameGraphics Property (ICosmosMotionStudyProperties)"
project: "SOLIDWORKS Motion Study API Help"
interface: "ICosmosMotionStudyProperties"
member: "WireFrameGraphics"
kind: "property"
source: "swmotionstudyapi/SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyProperties~WireFrameGraphics.html"
---

# WireFrameGraphics Property (ICosmosMotionStudyProperties)

Gets or sets whether to display the results as wireframe.

## Syntax

### Visual Basic (Declaration)

```vb
Property WireFrameGraphics As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmosMotionStudyProperties
Dim value As System.Boolean

instance.WireFrameGraphics = value

value = instance.WireFrameGraphics
```

### C#

```csharp
System.bool WireFrameGraphics {get; set;}
```

### C++/CLI

```cpp
property System.bool WireFrameGraphics {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to display results as wireframe, false to display the results rendered

## VBA Syntax

See [CosmosMotionStudyProperties::WireFrameGraphics](ms-its:swmotionstudyapivb6.chm::/SwMotionStudy~CosmosMotionStudyProperties~WireFrameGraphics.html).

## Examples

[Get Motion Study Properties and Results (VBA)](Get_COSMOSMotion_Motion_Study_Properties_and_Results_Example_VB.htm)

## Remarks

If the result is set to rendered mode, result vectors may be completely or partially hidden on the screen by rendered model geometry. In wireframe mode, results vectors are always visible on top of the model display.

## See Also

[ICosmosMotionStudyProperties Interface](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyProperties.html)
[ICosmosMotionStudyProperties Members](SolidWorks.Interop.swmotionstudy~SolidWorks.Interop.swmotionstudy.ICosmosMotionStudyProperties_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
