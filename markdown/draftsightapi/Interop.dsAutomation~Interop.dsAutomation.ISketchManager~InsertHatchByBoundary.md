---
title: "InsertHatchByBoundary Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertHatchByBoundary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertHatchByBoundary.html"
---

# InsertHatchByBoundary Method (ISketchManager)

Inserts a Hatch with the specified pattern, scale, angle, and boundary loop.

## Syntax

### Visual Basic

```vb
Function InsertHatchByBoundary( _
   ByVal BoundaryPointCountLongArray As System.Object, _
   ByVal BoundaryPointDblArray As System.Object, _
   ByVal PatternName As System.String, _
   ByVal PatternScale As System.Double, _
   ByVal PatternAngle As System.Double _
) As Hatch
```

### C#

```csharp
Hatch InsertHatchByBoundary(
   System.object BoundaryPointCountLongArray,
   System.object BoundaryPointDblArray,
   System.string PatternName,
   System.double PatternScale,
   System.double PatternAngle
)
```

### JScript

```
function InsertHatchByBoundary(
   BoundaryPointCountLongArray : System.Object,
   BoundaryPointDblArray : System.Object,
   PatternName : System.String,
   PatternScale : System.double,
   PatternAngle : System.double
) : Hatch;
```

### Managed Extensions for C++

```
Hatch* InsertHatchByBoundary(
   System.Object* BoundaryPointCountLongArray,
   System.Object* BoundaryPointDblArray,
   System.string* PatternName,
   System.double PatternScale,
   System.double PatternAngle
)
```

### C++/CLI

```cpp
Hatch^ InsertHatchByBoundary(
   System.Object^ BoundaryPointCountLongArray,
   System.Object^ BoundaryPointDblArray,
   System.String^ PatternName,
   System.double PatternScale,
   System.double PatternAngle
)
```

### Parameters

- `BoundaryPointCountLongArray`: Array containing a long that is the number of points in the Hatch boundary loop
- `BoundaryPointDblArray`: Array of x-y coordinates of the points in the Hatch boundary loop
- `PatternName`: Name of the Hatch pattern
- `PatternScale`: Value by which to scale the Hatch pattern; values are between .25 and 2 in .25 unit increments; default is 1 (**see Remarks**)
- `PatternAngle`: Angle of the Hatch pattern lines; values are between 0 and 2*pi radians in .26 radian increments; a positive angle rotates the pattern counter-clockwise

### Return Value

[Hatch](Interop.dsAutomation~Interop.dsAutomation.IHatch.html)

## Examples

[Insert Hatch (C#)](Insert_Hatch_Example_CSharp.htm)
[Insert Hatch (VB.NET)](Insert_Hatch_Example_VBNET.htm)
[Insert Hatch (VBA)](Insert_Hatch_Example_VBA.htm)
[Insert Hatch (JavaScript)](Insert_Hatch_Example_JS.htm)

## Remarks

If PatternScale is equal to:

- 2.00, then the distance between pattern lines doubles.
- 0.25, then the distance between pattern lines is 1/4 the original distance.

PatternScale is valid only when the HatchPatternType parameter of [IHatchPattern::GetHatchOrSolidData](Interop.dsAutomation~Interop.dsAutomation.IHatchPattern~GetHatchOrSolidData.html) is not dsHatchPatternType_e.dsHatchPatternType_UserDefined.

To scale user-defined Hatch patterns, call [IHatchPattern::SetHatchOrSolidData](Interop.dsAutomation~Interop.dsAutomation.IHatchPattern~SetHatchOrSolidData.html) to change the line spacing of the Hatch pattern.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::InsertHatchByEntities Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertHatchByEntities.html)
[ISketchManager::InsertHatchByInternalPoints Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertHatchByInternalPoints.html)

## Availability

DraftSight V1R1.3
