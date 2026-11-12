---
title: "PromptForPoint2 Method (ICommandMessage)"
project: ""
interface: "ICommandMessage"
member: "PromptForPoint2"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForPoint2.html"
---

# PromptForPoint2 Method (ICommandMessage)

Displays the specified prompt in the command window gets the x, y, and z coordinates specified by the user.

## Syntax

### Visual Basic

```vb
Function PromptForPoint2( _
   ByVal Prompt As System.String, _
   ByVal ShowRubberLine As System.Boolean, _
   ByVal BasePointX As System.Double, _
   ByVal BasePointY As System.Double, _
   ByVal BasePointZ As System.Double, _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double, _
   ByVal Plane As MathPlane _
) As System.Boolean
```

### C#

```csharp
System.bool PromptForPoint2(
   System.string Prompt,
   System.bool ShowRubberLine,
   System.double BasePointX,
   System.double BasePointY,
   System.double BasePointZ,
   out System.double X,
   out System.double Y,
   out System.double Z,
   MathPlane Plane
)
```

### JScript

```
function PromptForPoint2(
   Prompt : System.String,
   ShowRubberLine : System.boolean,
   BasePointX : System.double,
   BasePointY : System.double,
   BasePointZ : System.double,
   X : System.double,
   Y : System.double,
   Z : System.double,
   Plane : MathPlane
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool PromptForPoint2(
   System.string* Prompt,
   System.bool ShowRubberLine,
   System.double BasePointX,
   System.double BasePointY,
   System.double BasePointZ,
   [PARAMFLAG::Out] System.double X,
   [PARAMFLAG::Out] System.double Y,
   [PARAMFLAG::Out] System.double Z,
   MathPlane* Plane
)
```

### C++/CLI

```cpp
System.bool PromptForPoint2(
   System.String^ Prompt,
   System.bool ShowRubberLine,
   System.double BasePointX,
   System.double BasePointY,
   System.double BasePointZ,
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z,
   MathPlane^ Plane
)
```

### Parameters

- `Prompt`: Text of prompt
- `ShowRubberLine`: True to display a rubber line from the origin, or from the BasePointX, BasePointY, and BasePointZ coordinates, to the location of the cursor; false to not display the rubber line
- `BasePointX`: x coordinate for the point indicating where to start the rubber line (see **Remarks**)
- `BasePointY`: y coordinate for the point indicating where to start the rubber line (see **Remarks**)
- `BasePointZ`: z coordinate for the point indicating where to start the rubber line (see **Remarks**)
- `X`: x coordinate for a point
- `Y`: y coordinate for a point
- `Z`: z coordinate for a point
- `Plane`: Projection [plane](Interop.dsAutomation~Interop.dsAutomation.IMathPlane.html) cursor coordinates

### Return Value

True if the prompt is displayed in the command window, false if not

## Examples

[Insert Splines (C#)](Insert_Splines_Example_CSharp.htm)
[Insert Splines (VB.NET)](Insert_Splines_Example_VBNET.htm)
[Insert Splines (VBA)](Insert_Splines_Example_VBA.htm)

## Remarks

ShowRubberLine must be set to true for the values specified for BasePointX, BasePointY, or BasePointZ to have an effect. The rubber line extends to the location of the cursor in the drawing.

## See Also

[ICommandMessage Interface](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage.html)
[ICommandMessage Members](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage_members.html)
[ICommandMessage::PromptForPointOrKeyword Method ()](Interop.dsAutomation~Interop.dsAutomation.ICommandMessage~PromptForPointOrKeyword.html)

## Availability

DraftSight V1R2.0
