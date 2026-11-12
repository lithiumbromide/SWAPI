---
title: "CreateLinearSketchStepAndRepeat Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "CreateLinearSketchStepAndRepeat"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateLinearSketchStepAndRepeat.html"
---

# CreateLinearSketchStepAndRepeat Method (ISketchManager)

Creates a linear sketch pattern.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateLinearSketchStepAndRepeat( _
   ByVal NumX As System.Integer, _
   ByVal NumY As System.Integer, _
   ByVal SpacingX As System.Double, _
   ByVal SpacingY As System.Double, _
   ByVal AngleX As System.Double, _
   ByVal AngleY As System.Double, _
   ByVal DeleteInstances As System.String, _
   ByVal XSpacingDim As System.Boolean, _
   ByVal YSpacingDim As System.Boolean, _
   ByVal AngleDim As System.Boolean, _
   ByVal CreateNumOfInstancesDimInXDir As System.Boolean, _
   ByVal CreateNumOfInstancesDimInYDir As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim NumX As System.Integer
Dim NumY As System.Integer
Dim SpacingX As System.Double
Dim SpacingY As System.Double
Dim AngleX As System.Double
Dim AngleY As System.Double
Dim DeleteInstances As System.String
Dim XSpacingDim As System.Boolean
Dim YSpacingDim As System.Boolean
Dim AngleDim As System.Boolean
Dim CreateNumOfInstancesDimInXDir As System.Boolean
Dim CreateNumOfInstancesDimInYDir As System.Boolean
Dim value As System.Boolean

value = instance.CreateLinearSketchStepAndRepeat(NumX, NumY, SpacingX, SpacingY, AngleX, AngleY, DeleteInstances, XSpacingDim, YSpacingDim, AngleDim, CreateNumOfInstancesDimInXDir, CreateNumOfInstancesDimInYDir)
```

### C#

```csharp
System.bool CreateLinearSketchStepAndRepeat(
   System.int NumX,
   System.int NumY,
   System.double SpacingX,
   System.double SpacingY,
   System.double AngleX,
   System.double AngleY,
   System.string DeleteInstances,
   System.bool XSpacingDim,
   System.bool YSpacingDim,
   System.bool AngleDim,
   System.bool CreateNumOfInstancesDimInXDir,
   System.bool CreateNumOfInstancesDimInYDir
)
```

### C++/CLI

```cpp
System.bool CreateLinearSketchStepAndRepeat(
   System.int NumX,
   System.int NumY,
   System.double SpacingX,
   System.double SpacingY,
   System.double AngleX,
   System.double AngleY,
   System.String^ DeleteInstances,
   System.bool XSpacingDim,
   System.bool YSpacingDim,
   System.bool AngleDim,
   System.bool CreateNumOfInstancesDimInXDir,
   System.bool CreateNumOfInstancesDimInYDir
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumX`: Total number of instances along the x axis, including the seed
- `NumY`: Total number of instances along the y axis, including the seed
- `SpacingX`: Spacing between instances along the x axis
- `SpacingY`: Spacing between instances along the y axis
- `AngleX`: Angle for direction 1 relative to the x axis
- `AngleY`: Angle for direction 2 relative to the y axis
- `DeleteInstances`: Number of instances to delete, passed as a string in the format: "(a) (b) (c) "
- `XSpacingDim`: True to display the spacing between instances dimension along the x axis in the graphics area, false to not
- `YSpacingDim`: True to display the spacing between instances dimension along the y axis in the graphics area, false to not
- `AngleDim`: True to display the angle dimension between axes in the graphics area, false to not
- `CreateNumOfInstancesDimInXDir`: True to display the number of instances in the x direction dimension in the graphics area, false to not
- `CreateNumOfInstancesDimInYDir`: True to display the number of instances in the y direction dimension in the graphics area, false to not

### Return Value

True if the linear sketch pattern is created, false if not

## VBA Syntax

See [SketchManager::CreateLinearSketchStepAndRepeat](ms-its:sldworksapivb6.chm::/Sldworks~SketchManager~CreateLinearSketchStepAndRepeat.html).

## Examples

[Create and Edit Linear Sketch Pattern (VB.NET)](Create_and_Edit_Linear_Sketch_Pattern_Example_VBNET.htm)
[Create and Edit Linear Sketch Patten (VBA)](Create_and_Edit_Linear_Sketch_Pattern_Example_VB.htm)
[Create and Edit Linear Sketch Pattern (C#)](Create_and_Edit_Linear_Sketch_Pattern_Example_CSharp.htm)

## Remarks

The spacing instances, angle, and number of instances dimensions displayed in the graphics area can be modified by interactive users.

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)
[ISketchManager::EditLinearSketchStepAndRepeat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~EditLinearSketchStepAndRepeat.html)
[ISketchManager::CreateCircularSketchStepAndRepeat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateCircularSketchStepAndRepeat.html)
[ISketchManager::EditCircularSketchStepAndRepeat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~EditCircularSketchStepAndRepeat.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
