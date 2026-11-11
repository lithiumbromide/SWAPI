---
title: "CreateSolidBackground Method (IViewManager)"
project: ""
interface: "IViewManager"
member: "CreateSolidBackground"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IViewManager~CreateSolidBackground.html"
---

# CreateSolidBackground Method (IViewManager)

Creates a solid background.

## Syntax

### Visual Basic

```vb
Function CreateSolidBackground( _
   ByVal SolidColor As Color _
) As SolidBackground
```

### C#

```csharp
SolidBackground CreateSolidBackground(
   Color SolidColor
)
```

### JScript

```
function CreateSolidBackground(
   SolidColor : Color
) : SolidBackground;
```

### Managed Extensions for C++

```
SolidBackground* CreateSolidBackground(
   Color* SolidColor
)
```

### C++/CLI

```cpp
SolidBackground^ CreateSolidBackground(
   Color^ SolidColor
)
```

### Parameters

- `SolidColor`: [Color](Interop.dsAutomation~Interop.dsAutomation.IColor.html) for the solid background

### Return Value

[Solid background](Interop.dsAutomation~Interop.dsAutomation.ISolidBackground.html)

## Examples

[Create Model and Sheet Views (C#)](Create_Model_and_Sheet_Views_Example_CSharp.htm)
[Create Model and Sheet Views (VB.NET)](Create_Model_and_Sheet_Views_Example_VBNET.htm)
[Create Model and Sheet Views (VBA)](Create_Model_and_Sheet_Views_Example_VBA.htm)

## See Also

[IViewManager Interface](Interop.dsAutomation~Interop.dsAutomation.IViewManager.html)
[IViewManager Members](Interop.dsAutomation~Interop.dsAutomation.IViewManager_members.html)
[IModelNamedView::GetSolidBackground Method ()](Interop.dsAutomation~Interop.dsAutomation.IModelNamedView~GetSolidBackground.html)
[IModelNamedView::SetSolidBackground Method ()](Interop.dsAutomation~Interop.dsAutomation.IModelNamedView~SetSolidBackground.html)

## Availability

DraftSight V1R5.0
