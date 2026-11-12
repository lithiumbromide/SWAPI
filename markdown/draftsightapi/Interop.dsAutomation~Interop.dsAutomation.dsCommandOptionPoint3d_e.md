---
title: "dsCommandOptionPoint3d_e Enumeration"
project: ""
interface: "dsCommandOptionPoint3d_e"
member: ""
kind: "enum"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.dsCommandOptionPoint3d_e.html"
---

# dsCommandOptionPoint3d_e Enumeration

Command options for 3D points.

## Syntax

### Visual Basic

```vb
Public Enum dsCommandOptionPoint3d_e
   Inherits System.Enum
```

### C#

```csharp
public enum dsCommandOptionPoint3d_e : System.Enum
```

### JScript

```
public enum dsCommandOptionPoint3d_e extends System.Enum
```

### Managed Extensions for C++

```
__value public enum dsCommandOptionPoint3d_e : public System.Enum
```

### C++/CLI

```cpp
public enum class dsCommandOptionPoint3d_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| dsCommandOptionPoint3d_Count | Not used |
| dsCommandOptionPoint3d_GetLstXY | 1 = x, y, and z coordinates of last point specified, relative to the current custom coordinate system (CCS), for the current space |
| dsCommandOptionPoint3d_GetOrgActCS | 2 = x, y, and z coordinates of the the world coordinate system (WCS), of the origin of the active CCS of the active Viewport (read only) |
| dsCommandOptionPoint3d_GetVwCtr | 3 = x, y, and z coordinates of the center of the view in the active Viewport (read only) |
| dsCommandOptionPoint3d_GetXDirActCS | 4 = x direction of the current USC of the active Viewport in the current space (read only); |
| dsCommandOptionPoint3d_GetXYLLFit | 5 = x, y, and z coordinates of the lower-left point of the drawing extents (read only) |
| dsCommandOptionPoint3d_GetXYURFit | 6 = x, y, and z coordinates of the upper-right point of the drawing extents (read only) |
| dsCommandOptionPoint3d_GetYDirActCS | 7 = y direction of the current CCS of the active Viewport (read only) |
| dsCommandOptionPoint3d_LgcyTARGET | 8 = x, y, and z CCS coordinates of the target point of the active Viewport (read only and see Remarks ) |
| dsCommandOptionPoint3d_LgcyVIEWDIR | 9 = x, y, and z CCS coordinates of the viewing direction of the active Viewport (read only and see Remarks ) |
| dsCommandOptionPoint3d_LgcyVSMAX | 10 = x, y, and z CCS coordinates of the upper-right corner of the active Viewport (read only and see Remarks ) |
| dsCommandOptionPoint3d_LgcyVSMIN | 11 = x, y, and z USC coordinates of the lower-left corner of the active Viewport (read only and see Remarks ) |
| dsCommandOptionPoint3d_SetBase | 12 = Base point (x, y, and z coordinates) when the drawing is to be used as a Block and inserted into another drawing |
| dsCommandOptionPoint3d_Undefined | 0 = Undefined |

## Remarks

The string **Lgcy** in a command option indicates that setting the command option has no effect in DraftSight; however, the value is stored in the DWG file.

In most instances, user-interface command option equivalents are the strings following **dsCommandOptionPoint3d_**; for example, typing **GetLstXY** in the command prompt is equivalent to using **dsCommandOptionPoint3d_GetLstXY** in code.

## See Also

[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IDocument::GetCommandOptionPoint3D Method](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetCommandOptionPoint3D.html)
[IDocument::SetCommandOptionPoint3D Method](Interop.dsAutomation~Interop.dsAutomation.IDocument~SetCommandOptionPoint3D.html)
