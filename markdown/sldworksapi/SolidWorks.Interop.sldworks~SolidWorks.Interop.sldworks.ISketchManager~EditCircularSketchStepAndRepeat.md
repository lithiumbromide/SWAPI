---
title: "EditCircularSketchStepAndRepeat Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "EditCircularSketchStepAndRepeat"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~EditCircularSketchStepAndRepeat.html"
---

# EditCircularSketchStepAndRepeat Method (ISketchManager)

Edits a circular sketch pattern.

## Syntax

### Visual Basic (Declaration)

```vb
Function EditCircularSketchStepAndRepeat( _
   ByVal ArcRadius As System.Double, _
   ByVal ArcAngle As System.Double, _
   ByVal PatternNum As System.Integer, _
   ByVal PatternSpacing As System.Double, _
   ByVal PatternRotate As System.Boolean, _
   ByVal DeleteInstances As System.String, _
   ByVal RadiusDim As System.Boolean, _
   ByVal AngleDim As System.Boolean, _
   ByVal CreateNumOfInstancesDim As System.Boolean, _
   ByVal Seeds As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim ArcRadius As System.Double
Dim ArcAngle As System.Double
Dim PatternNum As System.Integer
Dim PatternSpacing As System.Double
Dim PatternRotate As System.Boolean
Dim DeleteInstances As System.String
Dim RadiusDim As System.Boolean
Dim AngleDim As System.Boolean
Dim CreateNumOfInstancesDim As System.Boolean
Dim Seeds As System.String
Dim value As System.Boolean

value = instance.EditCircularSketchStepAndRepeat(ArcRadius, ArcAngle, PatternNum, PatternSpacing, PatternRotate, DeleteInstances, RadiusDim, AngleDim, CreateNumOfInstancesDim, Seeds)
```

### C#

```csharp
System.bool EditCircularSketchStepAndRepeat(
   System.double ArcRadius,
   System.double ArcAngle,
   System.int PatternNum,
   System.double PatternSpacing,
   System.bool PatternRotate,
   System.string DeleteInstances,
   System.bool RadiusDim,
   System.bool AngleDim,
   System.bool CreateNumOfInstancesDim,
   System.string Seeds
)
```

### C++/CLI

```cpp
System.bool EditCircularSketchStepAndRepeat(
   System.double ArcRadius,
   System.double ArcAngle,
   System.int PatternNum,
   System.double PatternSpacing,
   System.bool PatternRotate,
   System.String^ DeleteInstances,
   System.bool RadiusDim,
   System.bool AngleDim,
   System.bool CreateNumOfInstancesDim,
   System.String^ Seeds
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ArcRadius`: Radius of the circular sketch pattern
- `ArcAngle`: Angle relative to the sketch entities being patterned
- `PatternNum`: Total number of instances, including the seed geometry
- `PatternSpacing`: Spacing between pattern instances
- `PatternRotate`: True to rotate the pattern, false to not
- `DeleteInstances`: Number of instances to delete, passed as a string formatted as: "(a) (b) (c) "
- `RadiusDim`: True to display the radius dimension in the graphics area, false to not
- `AngleDim`: True to display the angle dimension in the graphics area, false to not
- `CreateNumOfInstancesDim`: True to display the number of instances dimension in the graphics area, false to not
- `Seeds`: Array of the names of the entities, separated by the underscore character (_), that comprise the seed pattern (e.g., "Line1_Line2_Line3_Line4" for a rectangular-shaped seed pattern)

### Return Value

True if the circular sketch pattern is successfully edited, false if not

## VBA Syntax

See [SketchManager::EditCircularSketchStepAndRepeat](ms-its:sldworksapivb6.chm::/Sldworks~SketchManager~EditCircularSketchStepAndRepeat.html).

## Examples

[Create and Edit Circular Sketch Pattern (VB.NET)](Create_and_Edit_Circular_Sketch_Pattern_Example_VBNET.htm)
[Create and Edit Circular Sketch Pattern (VBA)](Create_and_Edit_Circular_Sketch_Pattern_Example_VB.htm)
[Create and Edit Circular Sketch Pattern (C#)](Create_and_Edit_Circular_Sketch_Pattern_Example_CSharp.htm)

## Remarks

The radius, angle, and number of instances dimensions displayed in the graphics area can be modified by interactive users.

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)
[ISketchManager::CreateCircularSketchStepAndRepeat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateCircularSketchStepAndRepeat.html)
[ISketchManager::CreateLinearSketchStepAndRepeat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateLinearSketchStepAndRepeat.html)
[ISketchManager::EditLinearSketchStepAndRepeat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~EditLinearSketchStepAndRepeat.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
