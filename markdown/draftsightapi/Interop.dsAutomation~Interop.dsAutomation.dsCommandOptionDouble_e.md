---
title: "dsCommandOptionDouble_e Enumeration"
project: ""
interface: "dsCommandOptionDouble_e"
member: ""
kind: "enum"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.dsCommandOptionDouble_e.html"
---

# dsCommandOptionDouble_e Enumeration

Command options with double values.

## Syntax

### Visual Basic

```vb
Public Enum dsCommandOptionDouble_e
   Inherits System.Enum
```

### C#

```csharp
public enum dsCommandOptionDouble_e : System.Enum
```

### JScript

```
public enum dsCommandOptionDouble_e extends System.Enum
```

### Managed Extensions for C++

```
__value public enum dsCommandOptionDouble_e : public System.Enum
```

### C++/CLI

```cpp
public enum class dsCommandOptionDouble_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| dsCommandOptionDouble_Count | Obsolete. Superseded by dsApplicationOptionDouble_e . |
| dsCommandOptionDouble_GetArea | 1 = Tools > Inquiry > Get Area |
| dsCommandOptionDouble_GetAreaPerim | 2 = Area perimeter (read only) |
| dsCommandOptionDouble_GetDst | 3 = Tools > Inquiry > Get Distance (read only) |
| dsCommandOptionDouble_GetDt | Obsolete. Superseded by dsApplicationOptionDouble_e . |
| dsCommandOptionDouble_GetDtCrt | 5 = Date and time drawing created in local time (read only) |
| dsCommandOptionDouble_GetDtJul | Obsolete. Superseded by dsApplicationOptionDouble_e . |
| dsCommandOptionDouble_GetDtLstSv | 7 = Date and time drawing last saved in local time (read only) |
| dsCommandOptionDouble_GetDtLstUSv | 8 = Local time and date drawing last updated or saved (read only) |
| dsCommandOptionDouble_GetLstAng | 9 = End angle of the last arc specified relative to the x,y plane of the active custom coordinate system (CCS) for the active space (read only) |
| dsCommandOptionDouble_GetTmLstEdt | 10 = Total editing time between saves of current drawing formatted as Number of days . Decimal fraction of a day (read only) |
| dsCommandOptionDouble_GetTmUsrEdit | 11 = User-elapsed timer (read only) |
| dsCommandOptionDouble_GetVwHt | 12 = Height of the view displayed in the active Viewport (read only) |
| dsCommandOptionDouble_LgcyBACKZ | 13 = Back clipping plane offset from the target plane for the active Viewport (read only and see Remarks ) |
| dsCommandOptionDouble_LgcyFACETRES | 14 = Smoothness of shaded and hidden-lines-removed entities; valid values 0.01 to 10.0 (see Remarks ) |
| dsCommandOptionDouble_LgcyFRONTZ | 15 = Front clipping plane offset from the target plane to the active Viewport (see Remarks ) |
| dsCommandOptionDouble_LgcyLENSLENGTH | 16 = Length of the lens (mm) used in perspective viewing (read only and see Remarks ) |
| dsCommandOptionDouble_LgcyVIEWTWIST | 17 = View rotation angle for the active Viewport relative to the world coordinate system (WCS) (read only and see Remarks ) |
| dsCommandOptionDouble_SetActLScl | 18 = Active LineType scaling factor |
| dsCommandOptionDouble_SetActPntSz | 19 = Tools > Options > Drawing Settings > Points > Size |
| dsCommandOptionDouble_SetActThk | 20 = Current 3D thickness |
| dsCommandOptionDouble_SetAngBase | 21 = Tools > Options > Drawing Settings > Unit System > Base angle |
| dsCommandOptionDouble_SetChmfAng | 22 = Modify > Chamfer > Angle |
| dsCommandOptionDouble_SetChmfDst1 | 23 = Modify > Chamfer > Specify first distance |
| dsCommandOptionDouble_SetChmfDst2 | 24 = Modify > Chamfer > Specify second distance |
| dsCommandOptionDouble_SetChmfLen | 25 = Modify > Chamfer > Angle |
| dsCommandOptionDouble_SetCirRad | 26 = Draw > Circle > Specify radius |
| dsCommandOptionDouble_SetDlDmMltpyScl | 27 = Tools > Options > Drafting Styles > Dimension > Dual Dimension > Multiplier for converting units |
| dsCommandOptionDouble_SetDlDmRnd | 28 = Tools > Options > Drafting Styles > Dimension > Dual Dimension > Round to the nearest |
| dsCommandOptionDouble_SetDmArwSz | 29 = Tools > Options > Drafting Styles > Dimension > Arrows > Size |
| dsCommandOptionDouble_SetDmDLDst | 30 = Tools > Options > Drafting Styles > Dimension > Line > Dimension line settings > Distance past start arrow |
| dsCommandOptionDouble_SetDmDLOfst | 31 = Tools > Options > Drafting Styles > Dimension > Line > Dimension line settings > Offset |
| dsCommandOptionDouble_SetDmELDst | 32 = Tools > Options > Drafting Styles > Dimension > Line > Extension line settings > Distance past dimension lines |
| dsCommandOptionDouble_SetDmELOfst | 33 = Tools > Options > Drafting Styles > Dimension > Line > Extension line settings > Offset |
| dsCommandOptionDouble_SetDmFrcScl | 34 = Tools > Options > Drafting Styles > Dimension > Text > Text settings > Fractional scale |
| dsCommandOptionDouble_SetDmGlblScl | 35 = Tools > Options > Drafting Styles > Dimension > Linear Dimension > Measurement scale > Scale factor |
| dsCommandOptionDouble_SetDmTolTxtMax | 36 = Tools > Options > Drafting Styles > Dimension > Tolerance > Tolerance settings > Maximum value |
| dsCommandOptionDouble_SetDmTxtHt | 37 = Tools > Options > Drafting Styles > Dimension > Text > Text settings > Height |
| dsCommandOptionDouble_SetDmTxtOfst | 38 = Tools > Options > Drafting Styles > Dimension > Text > Text position > Offset from dimension lines |
| dsCommandOptionDouble_SetDmTxtVPos | 39 = Tools > Options > Drafting Styles > Dimension > Text > Text position > Vertical |
| dsCommandOptionDouble_SetFltRad | 40 = Modify > Fillet > Radius |
| dsCommandOptionDouble_SetGblLScl | 41 = Tools > Options > Drawing Settings > Behavior > LineStyle Parameters > Global line scale |
| dsCommandOptionDouble_SetHtchPtrnAng | 42 = Draw > Hatch/Fill > Angle |
| dsCommandOptionDouble_SetHtchPtrnScl | 43 = Draw > Hatch/Fill > Scale |
| dsCommandOptionDouble_SetHtchSpc | 44 = Draw > Hatch/Fill > Spacing |
| dsCommandOptionDouble_SetLDmRnd | 45 = Tools > Options > Drafting Styles > Dimension > Linear Dimension > Round to the nearest |
| dsCommandOptionDouble_SetLDmSclFac | 46 = Tools > Options > Drafting Styles > Dimension > Linear Dimension > Measurement scale > Scale factor |
| dsCommandOptionDouble_SetNoteScl | 47 = Scale factor for multi-line width: 2.0 creates a multi-line 2X wider than the style definition 0 changes the multi-line into a single line <0 flips the order of the offset lines |
| dsCommandOptionDouble_SetOfstDst | 48 = Offset distance: <0 offsets an entity through a point >=0 sets default offset distance |
| dsCommandOptionDouble_SetPGdAng | Obsolete. Superseded by dsApplicationOptionDouble_e . |
| dsCommandOptionDouble_SetPLineWdth | 50 = PolyLine width for new entities |
| dsCommandOptionDouble_SetRDmCM | 51 = Tools > Options > Drafting Styles > Dimension > Radial/Diameter Dimension > Center mark display |
| dsCommandOptionDouble_SetRDmCMSz | 52 = Tools > Options > Drafting Styles > Dimension > Radial/Diameter Dimension > Center mark display > Size |
| dsCommandOptionDouble_SetRingID | 53 = Ring > Specify inside diameter |
| dsCommandOptionDouble_SetRingOD | 54 = Ring > Specify outside diameter |
| dsCommandOptionDouble_SetRSnpSpc | Obsolete. Superseded by dsApplicationOptionDouble_e . |
| dsCommandOptionDouble_SetSktchInc | 56 = Line segment increment for the SKETCH command |
| dsCommandOptionDouble_SetSnpAng | 57 = Rotation angle for snap and grid for the active Viewport relative to the current CCS |
| dsCommandOptionDouble_SetTDmMin | 58 = Tools > Options > Drafting Styles > Dimension > Tolerance > Tolerance settings > Precision |
| dsCommandOptionDouble_SetTrcWdth | 59 = Trace width |
| dsCommandOptionDouble_SetTxtHt | 60 = Tools > Options > Drafting Styles > Text > Height |
| dsCommandOptionDouble_SetUsrRl1 | 61 = User- or application-defined real number |
| dsCommandOptionDouble_SetUsrRl2 | 62 = User- or application-defined real number |
| dsCommandOptionDouble_SetUsrRl3 | 63 = User- or application-defined real number |
| dsCommandOptionDouble_SetUsrRl4 | 64 = User- or application-defined real number |
| dsCommandOptionDouble_SetUsrRl5 | 65 = User- or application-defined real number |
| dsCommandOptionDouble_SetVPScl | 66 = View scale factor for newly created Viewports; 0 = scaled to fit |
| dsCommandOptionDouble_SetZElv | 67 = Elevation of new entities relative to the current CCS |
| dsCommandOptionDouble_Undefined | Obsolete. Superseded by dsApplicationOptionDouble_e . |

## Remarks

The string **Lgcy** in a command option indicates that setting the command option has no effect in DraftSight; however, the value is stored in the DWG file.

In most instances, user-interface command option equivalents are the strings following **dsCommandOptionDouble_**; for example, typing **GetAreaPerim** in the command prompt is equivalent to using **dsCommandOptionDouble_GetAreaPerim** in code.

## See Also

[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IDocument::GetCommandOptionDouble Method](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetCommandOptionDouble.html)
[IDocument::SetCommandOptionDouble Method](Interop.dsAutomation~Interop.dsAutomation.IDocument~SetCommandOptionDouble.html)
