---
title: "InsertHatchByEntities Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertHatchByEntities"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertHatchByEntities.html"
---

# InsertHatchByEntities Method (ISketchManager)

Inserts a Hatch with the specified pattern, scale, angle, and boundary defined by the specified entities.

## Syntax

### Visual Basic

```vb
Function InsertHatchByEntities( _
   ByVal EntitiesArray As System.Object, _
   ByVal PatternName As System.String, _
   ByVal PatternScale As System.Double, _
   ByVal PatternAngle As System.Double _
) As Hatch
```

### C#

```csharp
Hatch InsertHatchByEntities(
   System.object EntitiesArray,
   System.string PatternName,
   System.double PatternScale,
   System.double PatternAngle
)
```

### JScript

```
function InsertHatchByEntities(
   EntitiesArray : System.Object,
   PatternName : System.String,
   PatternScale : System.double,
   PatternAngle : System.double
) : Hatch;
```

### Managed Extensions for C++

```
Hatch* InsertHatchByEntities(
   System.Object* EntitiesArray,
   System.string* PatternName,
   System.double PatternScale,
   System.double PatternAngle
)
```

### C++/CLI

```cpp
Hatch^ InsertHatchByEntities(
   System.Object^ EntitiesArray,
   System.String^ PatternName,
   System.double PatternScale,
   System.double PatternAngle
)
```

### Parameters

- `EntitiesArray`: Array of entities that form the Hatch boundary
- `PatternName`: Name of the Hatch pattern
- `PatternScale`: Value by which to scale the Hatch pattern; values are between .25 and 2 in .25 unit increments; default is 1 (**see Remarks**)
- `PatternAngle`: Angle of the Hatch pattern lines; values are between 0 and 2*pi radians in .26 radian increments; a positive angle rotates the pattern counter-clockwise

### Return Value

[Hatch](Interop.dsAutomation~Interop.dsAutomation.IHatch.html)

## Examples

[Insert Hatch (JavaScript)](Insert_Hatch_Example_JS.htm)
[Insert Hatch by Entities or Internal Points (C#)](Insert_Hatch_by_Entities_or_Internal_Points_CSharp.htm)
[Insert Hatch by Entities or Internal Points (VB.NET)](Insert_Hatch_by_Entities_or_Internal_Points_Example_VBNET.htm)
[Insert Hatch by Entities or Internal Points (VBA)](Insert_Hatch_by_Entities_or_Internal_Points_Example_VBA.htm)

## Remarks

If PatternScale is equal to:

- 2.00, then the distance between pattern lines doubles.
- 0.25, then the distance between pattern lines is 1/4 the original distance.

PatternScale is valid only when the HatchPatternType parameter of [IHatchPattern::GetHatchOrSolidData](Interop.dsAutomation~Interop.dsAutomation.IHatchPattern~GetHatchOrSolidData.html) is not dsHatchPatternType_e.dsHatchPatternType_UserDefined.

To scale user-defined Hatch patterns, call [IHatchPattern::SetHatchOrSolidData](Interop.dsAutomation~Interop.dsAutomation.IHatchPattern~SetHatchOrSolidData.html) to change the line spacing of the Hatch pattern.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::InsertHatchByBoundary Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertHatchByBoundary.html)
[ISketchManager::InsertHatchByInternalPoints Method](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertHatchByInternalPoints.html)

## Availability

DraftSight V1R1.4
