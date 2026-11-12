---
title: "CreateEquationSpline Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "CreateEquationSpline"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateEquationSpline.html"
---

# CreateEquationSpline Method (ISketchManager)

Obsolete. Superseded by [ISketchManager::CreateEquationSpline2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~CreateEquationSpline2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateEquationSpline( _
   ByVal YExpression As System.String, _
   ByVal RangeStart As System.Double, _
   ByVal RangeEnd As System.Double, _
   ByVal IsAngleRange As System.Boolean, _
   ByVal RotationAngle As System.Double, _
   ByVal XOffset As System.Double, _
   ByVal YOffset As System.Double, _
   ByVal LockStart As System.Boolean, _
   ByVal LockEnd As System.Boolean _
) As SketchSpline
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim YExpression As System.String
Dim RangeStart As System.Double
Dim RangeEnd As System.Double
Dim IsAngleRange As System.Boolean
Dim RotationAngle As System.Double
Dim XOffset As System.Double
Dim YOffset As System.Double
Dim LockStart As System.Boolean
Dim LockEnd As System.Boolean
Dim value As SketchSpline

value = instance.CreateEquationSpline(YExpression, RangeStart, RangeEnd, IsAngleRange, RotationAngle, XOffset, YOffset, LockStart, LockEnd)
```

### C#

```csharp
SketchSpline CreateEquationSpline(
   System.string YExpression,
   System.double RangeStart,
   System.double RangeEnd,
   System.bool IsAngleRange,
   System.double RotationAngle,
   System.double XOffset,
   System.double YOffset,
   System.bool LockStart,
   System.bool LockEnd
)
```

### C++/CLI

```cpp
SketchSpline^ CreateEquationSpline(
   System.String^ YExpression,
   System.double RangeStart,
   System.double RangeEnd,
   System.bool IsAngleRange,
   System.double RotationAngle,
   System.double XOffset,
   System.double YOffset,
   System.bool LockStart,
   System.bool LockEnd
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `YExpression`: Equation for y (see **Remarks**)
- `RangeStart`: Start value of x (see **Remarks**)
- `RangeEnd`: End value of x (see **Remarks**)
- `IsAngleRange`: True if the range and x value represent an angle (in radians), false if not
- `RotationAngle`: Rotation angle (in radians) for the curve
- `XOffset`: Offset in x for f(x), where x = 0 (see **Remarks**)
- `YOffset`: Offset in y for f(x), where x = 0 (see **Remarks**)
- `LockStart`: True to lock the start point (RangeStart) of the curve, false to not
- `LockEnd`: True to lock the end point (RangeEnd) of the curve, false to not

### Return Value

[Equation-driven curve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSpline.html)

## VBA Syntax

See [SketchManager::CreateEquationSpline](ms-its:sldworksapivb6.chm::/sldworks~SketchManager~CreateEquationSpline.html).

## Examples

[Create Equation-driven Curve (C#)](Create_Equation-driven_Curve_Example_CSharp.htm)
[Create Equation-driven Curve (VB.NET)](Create_Equation-driven_Curve_Example_VBNET.htm)
[Create Equation-driven Curve (VBA)](Create_Equation-driven_Curve_Example_VB.htm)

## Remarks

**YExpression:**

Any function that you can define as a 2D function in the following form:

y-in-the-sketch = f(x-in-the-sketch)

will appear as a curve in the sketch. For example:

y = sin(x)

**RangeStart** and **RangeEnd**

You cannot specify string values for RangeStart and RangeEnd; you must specify double values.

**XOffset:**

In the equation:

y = sin(x) [x=0 to 2Pi]

the start point (0,0) is moved by XOffset in the x direction.

**YOffset:**

In the equation:

y = sin(x) [x=0 to 2Pi]

the start point (0,0) is moved by YOffset in the y direction.

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)
[ISketchSpline::GetEquationParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetEquationParameters.html)
[ISketchSpline::SetEquationParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~SetEquationParameters.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
