---
title: "CreateGradientBackground Method (IViewManager)"
project: ""
interface: "IViewManager"
member: "CreateGradientBackground"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IViewManager~CreateGradientBackground.html"
---

# CreateGradientBackground Method (IViewManager)

Creates a gradient background.

## Syntax

### Visual Basic

```vb
Function CreateGradientBackground( _
   ByVal TopColor As Color, _
   ByVal MiddleColor As Color, _
   ByVal BottomColor As Color, _
   ByVal UseTwoColors As System.Boolean, _
   ByVal Angle As System.Double _
) As GradientBackground
```

### C#

```csharp
GradientBackground CreateGradientBackground(
   Color TopColor,
   Color MiddleColor,
   Color BottomColor,
   System.bool UseTwoColors,
   System.double Angle
)
```

### JScript

```
function CreateGradientBackground(
   TopColor : Color,
   MiddleColor : Color,
   BottomColor : Color,
   UseTwoColors : System.boolean,
   Angle : System.double
) : GradientBackground;
```

### Managed Extensions for C++

```
GradientBackground* CreateGradientBackground(
   Color* TopColor,
   Color* MiddleColor,
   Color* BottomColor,
   System.bool UseTwoColors,
   System.double Angle
)
```

### C++/CLI

```cpp
GradientBackground^ CreateGradientBackground(
   Color^ TopColor,
   Color^ MiddleColor,
   Color^ BottomColor,
   System.bool UseTwoColors,
   System.double Angle
)
```

### Parameters

- `TopColor`: [Color](Interop.dsAutomation~Interop.dsAutomation.IColor.html) for the top of the gradient background
- `MiddleColor`: [Color](Interop.dsAutomation~Interop.dsAutomation.IColor.html) for the middle of the gradient background
- `BottomColor`: [Color](Interop.dsAutomation~Interop.dsAutomation.IColor.html) for the bottom of the gradient background
- `UseTwoColors`: True to use TopColor and BottomColor and ignore MiddleColor, false to use TopColor, MiddleColor, and BottomColor
- `Angle`: Angle by which to rotate the gradient background

### Return Value

[Gradient background](Interop.dsAutomation~Interop.dsAutomation.IGradientBackground.html)

## Examples

[Create Model and Sheet Views (C#)](Create_Model_and_Sheet_Views_Example_CSharp.htm)
[Create Model and Sheet Views (VB.NET)](Create_Model_and_Sheet_Views_Example_VBNET.htm)
[Create Model and Sheet Views (VBA)](Create_Model_and_Sheet_Views_Example_VBA.htm)

## See Also

[IViewManager Interface](Interop.dsAutomation~Interop.dsAutomation.IViewManager.html)
[IViewManager Members](Interop.dsAutomation~Interop.dsAutomation.IViewManager_members.html)
[IModelNamedView::GetGradientBackground Method ()](Interop.dsAutomation~Interop.dsAutomation.IModelNamedView~GetGradientBackground.html)
[IModelNamedView::SetGradientBackground Method ()](Interop.dsAutomation~Interop.dsAutomation.IModelNamedView~SetGradientBackground.html)

## Availability

DraftSight V1R5.0
