---
title: "SetEquationParameters2 Method (ISketchSpline)"
project: "SOLIDWORKS API Help"
interface: "ISketchSpline"
member: "SetEquationParameters2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~SetEquationParameters2.html"
---

# SetEquationParameters2 Method (ISketchSpline)

Sets an equation-driven curve's parameters.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetEquationParameters2( _
   ByVal XExpression As System.String, _
   ByVal YExpression As System.String, _
   ByVal ZExpression As System.String, _
   ByVal RangeStart As System.Double, _
   ByVal RangeEnd As System.Double, _
   ByVal IsAngleRange As System.Boolean, _
   ByVal RotationAngle As System.Double, _
   ByVal XOffset As System.Double, _
   ByVal YOffset As System.Double, _
   ByVal LockStart As System.Boolean, _
   ByVal LockEnd As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSpline
Dim XExpression As System.String
Dim YExpression As System.String
Dim ZExpression As System.String
Dim RangeStart As System.Double
Dim RangeEnd As System.Double
Dim IsAngleRange As System.Boolean
Dim RotationAngle As System.Double
Dim XOffset As System.Double
Dim YOffset As System.Double
Dim LockStart As System.Boolean
Dim LockEnd As System.Boolean
Dim value As System.Boolean

value = instance.SetEquationParameters2(XExpression, YExpression, ZExpression, RangeStart, RangeEnd, IsAngleRange, RotationAngle, XOffset, YOffset, LockStart, LockEnd)
```

### C#

```csharp
System.bool SetEquationParameters2(
   System.string XExpression,
   System.string YExpression,
   System.string ZExpression,
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
System.bool SetEquationParameters2(
   System.String^ XExpression,
   System.String^ YExpression,
   System.String^ ZExpression,
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

- `XExpression`: Equation for x
- `YExpression`: Equation for y
- `ZExpression`: Equation for z
- `RangeStart`: Start value of x
- `RangeEnd`: End value of x
- `IsAngleRange`: True if the range and x value represent an angle (in radians), false if not
- `RotationAngle`: Rotation angle (in radians) for the curve
- `XOffset`: Offset in x for f(x), where x = 0
- `YOffset`: Offset in y for f(x), where x = 0
- `LockStart`: True to lock the start point (RangeStart) of the curve, false to not
- `LockEnd`: True to lock the end point (RangeEnd) of the curve, false to not

### Return Value

True if the equation-driven curve's parameters are set, false if not

## VBA Syntax

See [SketchSpline::SetEquationParameters2](ms-its:sldworksapivb6.chm::/sldworks~SketchSpline~SetEquationParameters2.html).

## See Also

[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.html)
[ISketchSpline Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_members.html)
[ISketchSpline::GetEquationParameters2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~GetEquationParameters2.html)
[ISketchManager::CreateEquationSpline2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateEquationSpline2.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
