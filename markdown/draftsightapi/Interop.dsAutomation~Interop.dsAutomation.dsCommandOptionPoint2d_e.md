---
title: "dsCommandOptionPoint2d_e Enumeration"
project: ""
interface: "dsCommandOptionPoint2d_e"
member: ""
kind: "enum"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.dsCommandOptionPoint2d_e.html"
---

# dsCommandOptionPoint2d_e Enumeration

Command options for 2D points.

## Syntax

### Visual Basic

```vb
Public Enum dsCommandOptionPoint2d_e
   Inherits System.Enum
```

### C#

```csharp
public enum dsCommandOptionPoint2d_e : System.Enum
```

### JScript

```
public enum dsCommandOptionPoint2d_e extends System.Enum
```

### Managed Extensions for C++

```
__value public enum dsCommandOptionPoint2d_e : public System.Enum
```

### C++/CLI

```cpp
public enum class dsCommandOptionPoint2d_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| dsCommandOptionPoint2d_Count | Not used |
| dsCommandOptionPoint2d_GetSzVP | 1 = Size of Viewport in pixels (x and y coordinates and read only) |
| dsCommandOptionPoint2d_GetXYLLBnds | 2 = x and y coordinates indicating the lower-left grid limits for the current workspace |
| dsCommandOptionPoint2d_GetXYURBnds | 3 = x and y coordinates indicating the upper-right grid limits for the current workspace |
| dsCommandOptionPoint2d_SetGridUnt | 4 = Tools > Options > User Preferences > Drafting Options > Display > Grid Settings > Spacing > Horizontal display spacing and Vertical Display spacing ; valid values for both settings 1-100 |
| dsCommandOptionPoint2d_SetSnpBase | 5 = x and y coordinates indicating the grid origin in the current Viewport relative to the current custom coordinate system (CCS) |
| dsCommandOptionPoint2d_SetSnpSpc | 6 = Tools > Options > User Preferences > Drafting Options > Pointer Control > Snap Settings > Spacing > Horizontal Snap spacing and Vertical Snap spacing ; valid values for both settings 1-100 |
| dsCommandOptionPoint2d_Undefined | 0 = Undefined |

## Remarks

The string **Lgcy** in a command option indicates that setting the command option has no effect in DraftSight; however, the value is stored in the DWG file.

In most instances, user-interface command option equivalents are the strings following **dsCommandOptionPoint2d_**; for example, typing **GetSzVP** in the command prompt is equivalent to using **dsCommandOptionPoint2d_GetSzVP** in code.

## See Also

[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IDocument::GetCommandOptionPoint2D Method](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetCommandOptionPoint2D.html)
[IDocument::SetCommandOptionPoint2D Method](Interop.dsAutomation~Interop.dsAutomation.IDocument~SetCommandOptionPoint2D.html)
