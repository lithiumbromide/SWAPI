---
title: "GetHatchOrSolidData Method (IHatchPattern)"
project: ""
interface: "IHatchPattern"
member: "GetHatchOrSolidData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IHatchPattern~GetHatchOrSolidData.html"
---

# GetHatchOrSolidData Method (IHatchPattern)

Gets the specified Hatch pattern data.

## Syntax

### Visual Basic

```vb
Sub GetHatchOrSolidData( _
   ByRef PatternName As System.String, _
   ByRef Angle As System.Double, _
   ByRef Scale As System.Double, _
   ByRef HatchPatternType As dsHatchPatternType_e, _
   ByRef Spacing As System.Double _
)
```

### C#

```csharp
void GetHatchOrSolidData(
   out System.string PatternName,
   out System.double Angle,
   out System.double Scale,
   out dsHatchPatternType_e HatchPatternType,
   out System.double Spacing
)
```

### JScript

```
function GetHatchOrSolidData(
   PatternName : System.String,
   Angle : System.double,
   Scale : System.double,
   HatchPatternType : dsHatchPatternType_e,
   Spacing : System.double
);
```

### Managed Extensions for C++

```
void GetHatchOrSolidData(
   [PARAMFLAG::Out] System.string* PatternName,
   [PARAMFLAG::Out] System.double Angle,
   [PARAMFLAG::Out] System.double Scale,
   [PARAMFLAG::Out] dsHatchPatternType_e HatchPatternType,
   [PARAMFLAG::Out] System.double Spacing
)
```

### C++/CLI

```cpp
void GetHatchOrSolidData(
   [Out] System.String^ PatternName,
   [Out] System.double Angle,
   [Out] System.double Scale,
   [Out] dsHatchPatternType_e HatchPatternType,
   [Out] System.double Spacing
)
```

### Parameters

- `PatternName`: Name of the Hatch pattern
- `Angle`: Angle of the Hatch pattern lines; values are between 0 and 360° in 15° increments; a positive angle rotates the pattern counter-clockwise
- `Scale`: Value by which to scale the Hatch pattern; values are between .25 and 2 in .25 unit increments; default is 1; for example, 2 doubles the distances in the pattern, and .25 reduces the original dimensions by 1/4; only valid if HatchPatternType not dsHatchPatternType_e.dsHatchPatternType_UserDefined; for user-defined Hatch patterns use Spacing to change Hatch pattern line distances
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
[IHatchPattern::SetHatchOrSolidData Method](Interop.dsAutomation~Interop.dsAutomation.IHatchPattern~SetHatchOrSolidData.html)

## Availability

DraftSight V1R1.3
