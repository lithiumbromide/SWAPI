---
title: "SetHatchOrSolidData Method (IHatchPattern)"
project: ""
interface: "IHatchPattern"
member: "SetHatchOrSolidData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IHatchPattern~SetHatchOrSolidData.html"
---

# SetHatchOrSolidData Method (IHatchPattern)

Sets the specified Hatch pattern.

## Syntax

### Visual Basic

```vb
Sub SetHatchOrSolidData( _
   ByVal PatternName As System.String, _
   ByVal Angle As System.Double, _
   ByVal Scale As System.Double, _
   ByVal HatchPatternType As dsHatchPatternType_e, _
   ByVal Spacing As System.Double _
)
```

### C#

```csharp
void SetHatchOrSolidData(
   System.string PatternName,
   System.double Angle,
   System.double Scale,
   dsHatchPatternType_e HatchPatternType,
   System.double Spacing
)
```

### JScript

```
function SetHatchOrSolidData(
   PatternName : System.String,
   Angle : System.double,
   Scale : System.double,
   HatchPatternType : dsHatchPatternType_e,
   Spacing : System.double
);
```

### Managed Extensions for C++

```
void SetHatchOrSolidData(
   System.string* PatternName,
   System.double Angle,
   System.double Scale,
   dsHatchPatternType_e HatchPatternType,
   System.double Spacing
)
```

### C++/CLI

```cpp
void SetHatchOrSolidData(
   System.String^ PatternName,
   System.double Angle,
   System.double Scale,
   dsHatchPatternType_e HatchPatternType,
   System.double Spacing
)
```

### Parameters

- `PatternName`: Name of the Hatch pattern
- `Angle`: Angle of the Hatch pattern lines; values are between 0 and 360° in 15° increments; a positive angle rotates the pattern counter-clockwise
- `Scale`: Value by which to scale the Hatch pattern; values are between .25 and 2 in .25 unit increments; default is 1; for example, 2 doubles the distances in the pattern, and .25 reduces the original dimensions by 1/4; only valid if HatchPatternType not dsHatchPatternType_e.dsHatchPatternType_UserDefined; for user-defined Hatch patterns use Spacing to change hatch pattern line distances
- `HatchPatternType`: Hatch pattern type as defined in [dsHatchPatternType_e](Interop.dsAutomation~Interop.dsAutomation.dsHatchPatternType_e.html)
- `Spacing`: Distance between Hatch pattern lines in drawing units; default is 1; change the line spacing to customize the pattern proportions for specific graphics areas

## Examples

[Get or Set Hatch Pattern Data (C#)](Get_and_Set_Hatch_Pattern_Data_Example_CSharp.htm)
[Get or Set Hatch Pattern Data (VB.NET)](Get_and_Set_Hatch_Pattern_Data_Example_VBNET.htm)
[Get or Set Hatch Pattern Data (VBA)](Get_and_Set_Hatch_Pattern_Data_Example_VBA.htm)

## Remarks

This method is valid only when [IHatchPattern:GetFillType](Interop.dsAutomation~Interop.dsAutomation.IHatchPattern~GetFillType.html) is dsHatchFillType_e.dsHatchFillType_Hatch or dsHatchFillType_e.dsHatchFillType_Solid.

## See Also

[IHatchPattern Interface](Interop.dsAutomation~Interop.dsAutomation.IHatchPattern.html)
[IHatchPattern Members](Interop.dsAutomation~Interop.dsAutomation.IHatchPattern_members.html)
[IHatchPattern::GetHatchOrSolidData Method](Interop.dsAutomation~Interop.dsAutomation.IHatchPattern~GetHatchOrSolidData.html)

## Availability

DraftSight V1R1.3
