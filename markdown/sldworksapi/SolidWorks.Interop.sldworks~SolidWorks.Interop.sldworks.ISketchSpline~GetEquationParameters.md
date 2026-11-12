---
title: "GetEquationParameters Method (ISketchSpline)"
project: "SOLIDWORKS API Help"
interface: "ISketchSpline"
member: "GetEquationParameters"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetEquationParameters.html"
---

# GetEquationParameters Method (ISketchSpline)

Obsolete. Superseded by [ISketchSpline::GetEquationParameters2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSpline~GetEquationParameters2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEquationParameters( _
   ByRef YExpression As System.String, _
   ByRef RangeStart As System.Double, _
   ByRef RangeEnd As System.Double, _
   ByRef IsAngleRange As System.Boolean, _
   ByRef RotationAngle As System.Double, _
   ByRef XOffset As System.Double, _
   ByRef YOffset As System.Double, _
   ByRef LockStart As System.Boolean, _
   ByRef LockEnd As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSpline
Dim YExpression As System.String
Dim RangeStart As System.Double
Dim RangeEnd As System.Double
Dim IsAngleRange As System.Boolean
Dim RotationAngle As System.Double
Dim XOffset As System.Double
Dim YOffset As System.Double
Dim LockStart As System.Boolean
Dim LockEnd As System.Boolean
Dim value As System.Boolean

value = instance.GetEquationParameters(YExpression, RangeStart, RangeEnd, IsAngleRange, RotationAngle, XOffset, YOffset, LockStart, LockEnd)
```

### C#

```csharp
System.bool GetEquationParameters(
   out System.string YExpression,
   out System.double RangeStart,
   out System.double RangeEnd,
   out System.bool IsAngleRange,
   out System.double RotationAngle,
   out System.double XOffset,
   out System.double YOffset,
   out System.bool LockStart,
   out System.bool LockEnd
)
```

### C++/CLI

```cpp
System.bool GetEquationParameters(
   [Out] System.String^ YExpression,
   [Out] System.double RangeStart,
   [Out] System.double RangeEnd,
   [Out] System.bool IsAngleRange,
   [Out] System.double RotationAngle,
   [Out] System.double XOffset,
   [Out] System.double YOffset,
   [Out] System.bool LockStart,
   [Out] System.bool LockEnd
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

True if the equation-driven curve's parameters are returned, false if not

## VBA Syntax

See [SketchSpline::GetEquationParameters](ms-its:sldworksapivb6.chm::/sldworks~SketchSpline~GetEquationParameters.html).

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

[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.html)
[ISketchSpline Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_members.html)
[ISketchSpline::SetEquationParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~SetEquationParameters.html)
[ISketchManager::CreateEquationSpline Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateEquationSpline.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
