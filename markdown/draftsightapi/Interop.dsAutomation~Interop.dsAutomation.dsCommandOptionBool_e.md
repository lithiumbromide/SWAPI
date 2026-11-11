---
title: "dsCommandOptionBool_e Enumeration"
project: ""
interface: "dsCommandOptionBool_e"
member: ""
kind: "enum"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.dsCommandOptionBool_e.html"
---

# dsCommandOptionBool_e Enumeration

Command options with Boolean values.

## Syntax

### Visual Basic

```vb
Public Enum dsCommandOptionBool_e
   Inherits System.Enum
```

### C#

```csharp
public enum dsCommandOptionBool_e : System.Enum
```

### JScript

```
public enum dsCommandOptionBool_e extends System.Enum
```

### Managed Extensions for C++

```
__value public enum dsCommandOptionBool_e : public System.Enum
```

### C++/CLI

```cpp
public enum class dsCommandOptionBool_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| dsCommandOptionBool_Count | Obsolete. Superseded by dsApplicationOptionBool_e . |
| dsCommandOptionBool_EnblBAttDlgs | Obsolete. Superseded by dsApplicationOptionBool_e . |
| dsCommandOptionBool_EnblBAttVrfy | Obsolete. Superseded by dsApplicationOptionBool_e . |
| dsCommandOptionBool_EnblBMPPrvw | Obsolete. Superseded by dsApplicationOptionBool_e . |
| dsCommandOptionBool_EnblBnds | 4 = Sets whether you can create entities outside the grid limits: False = No True = Yes |
| dsCommandOptionBool_EnblBoxTxt | 5 = Turns boxed text display and print mode on and off: False = Displays text True = Displays box |
| dsCommandOptionBool_EnblCCSVPMode | 6 = Tools > Options > Drawing Settings > Coordinate System > Options > Update view when coordinate system changes: False = Unlocked True = Locked |
| dsCommandOptionBool_EnblCSByVP | 7 = Tools > Options > Drawing Settings > Coordinate System > Options > Save coordinate system with view tile: False = Unchanged True = Changed to world coordinate system (WCS) for the command |
| dsCommandOptionBool_EnblDlDm | 8 = Tools > Options > Drafting Styles > Dimension > Dual Dimension > Show dual dimensions: False = Disabled True = Enabled |
| dsCommandOptionBool_EnblDmArwUsr | 9 = Sets the use of custom Blocks for dimension arrowheads on or off: False = Off True = On |
| dsCommandOptionBool_EnblDmDLBtwn | 10 = Tools > Options > Draft Styles > Fit > Dimension text > Additional options > Dimension lines between extension lines: False = Do not draw dimension lines between extension lines True = Draw dimension lines between extension lines |
| dsCommandOptionBool_EnblDmDLDsp1 | 11 = Tools > Options > Drafting Styles > Dimension > Line > Dimension line settings > Hide > Dimension Line 1: False = Not hidden True = Hidden |
| dsCommandOptionBool_EnblDmDLDsp2 | 12 = Tools > Options > Drafting Styles > Dimension > Line > Dimension line settings > Hide > Dimension Line 2: False = Not hidden True = Hidden |
| dsCommandOptionBool_EnblDmELDsp1 | 13 = Tools > Options > Drafting Styles > Dimension > Line > Extension line settings > Hide > Extension Line 1: False = Not hidden True = Hidden |
| dsCommandOptionBool_EnblDmELDsp2 | 14 = Tools > Options > Drafting Styles > Dimension > Line > Extension line settings > Hide > Extension Line 2: False = Not hidden True = Hidden |
| dsCommandOptionBool_EnblDmFitArwSup | 15 = Tools > Options > Drafting Styles > Dimension > Fit > Geometry > Hide arrows: False = Not hidden True = Hidden |
| dsCommandOptionBool_EnblDmTolAppnd | 16 = Tools > Options > Drafting Styles > Dimension > Tolerance > Tolerance settings > Calculation: False = Do not append True = Append |
| dsCommandOptionBool_EnblDmTxtAlgn | 17 = Dimension > Align Text: False = Align text with dimension line 1 = Draw text horizontally |
| dsCommandOptionBool_EnblDmTxtBtwn | 18 = Tools > Options > Drafting Styles > Dimension > Fit > Additional options > Specify text placement: False = Cursor controls dimension line location True = Cursor controls dimension line and text location |
| dsCommandOptionBool_EnblDmTxtBtwnExtLns | 19 = Tools > Options > Drafting Styles > Dimension > Fit > Geometry > When space is limited, move selected entity outside of extension lines > Keep text between extension lines: False = Placement of text varies True = Text placed between extension lines |
| dsCommandOptionBool_EnblEntSelPreSel | Obsolete. Superseded by dsApplicationOptionBool_e . |
| dsCommandOptionBool_EnblFills | 21 = Draw > Hatch/Fill > Fill: False = Not filled True = Filled |
| dsCommandOptionBool_EnblGBox | Obsolete. Superseded by dsApplicationOptionBool_e . |
| dsCommandOptionBool_EnblGrid | 23 = Tools > Options > User Preferences > Drafting Options > Display > Grid Settings > Enable Grid (F7): False = Turn grid off True = Turn grid on |
| dsCommandOptionBool_EnblImgHlt | Obsolete. Superseded by dsApplicationOptionBool_e . |
| dsCommandOptionBool_EnblLWtDsp | 25 = Tools > Options > Active Drafting Styles > Line Font > Line Weight > By Layer > Display weight in graphics area: False = Do not display True = Display |
| dsCommandOptionBool_EnblNavDlgs | Obsolete. Superseded by dsApplicationOptionBool_e . |
| dsCommandOptionBool_EnblOrtho | 27 = Sets whether cursor only moves in a perpendicular direction: False = Off True = On |
| dsCommandOptionBool_EnblPLineVert | 28 = Sets whether the LineStyle used around the vertices of a PolyLine are continuous or dashed: False = PolyLine starts and ends with a dash at each vertex True = Continuous pattern around the vertices of the PolyLine |
| dsCommandOptionBool_EnblPLnEllps | 29 = Sets whether to create a true Ellipse or a PolyLine representation of an Ellipse: False = Create true Ellipse True = Create PolyLine representation of an Ellipse |
| dsCommandOptionBool_EnblPrxyWrng | Obsolete. Superseded by dsApplicationOptionBool_e . |
| dsCommandOptionBool_EnblRbldAuto | 31 = Sets whether to automatically regenerate a drawing: False = Off True = On |
| dsCommandOptionBool_EnblRefEdt | 32 = Sets whether the current drawing can be edited in-place if referenced by another drawing: False = No True = Yes |
| dsCommandOptionBool_EnblRgnBndryDel | Obsolete. Superseded by dsApplicationOptionBool_e . |
| dsCommandOptionBool_EnblRstrOleDsp | Obsolete. See dsApplicationOptionBool_e . |
| dsCommandOptionBool_EnblSlhEdgDsp | 35 = Sets whether to display silhouette edges of 3D solid entities in 2D wireframe or 3D wireframe: False = Off True = On |
| dsCommandOptionBool_EnblSnp | 36 = Tools > Options > User Preferences > Drafting Options > Pointer Control > Snap Settings > Enable Snap (F9): False = Off True = On |
| dsCommandOptionBool_EnblSnpIso | 37 = Tools > Options > User Preferences > Drafting Options > Display > Grid Settings > Orientation > Isometric: False = Rectangular True = Isometric |
| dsCommandOptionBool_EnblSplnFrmDsp | 38 = Sets whether to display the control polygon for splines and spline-fit PolyLines: False = Do not display control polygon True = Display control polygon |
| dsCommandOptionBool_EnblSTBs | 39 = Sets the print style to be named tables or color-dependent tables (read only): False = Use color-dependent print-style tables True = Use named print-style tables |
| dsCommandOptionBool_EnblTDm | 40 = Tools > Options > Drafting Styles > Dimension > Tolerance > Tolerance settings > Calculation: False = Dimension limits not generated True = Dimension limits generated |
| dsCommandOptionBool_EnblTxtHide | 41 = Sets whether text is hidden: False = Not hidden True = Hidden |
| dsCommandOptionBool_EnblVP | 42 = Sets whether Model tab is active: False = Last active tab becomes active True = Model tab becomes active |
| dsCommandOptionBool_EnblVPLScl | 43 = Sets whether Viewport scaling overrides LineStyle scaling: False = No True = Yes |
| dsCommandOptionBool_GetStatDWGNm | 44 = Indicates whether the current drawing is named (read only): False = Not named True = Named |
| dsCommandOptionBool_LgcyDIMASO | 45 = Sets whether associative dimensions are on or off (see Remarks ) 0 = False 1 = True |
| dsCommandOptionBool_LgcyDIMSHO | 46 = Sets whether dimension measurements are updated when increasing or decreasing the size of a dimensioned entity (see Remarks ): 0 = False 1 = True |
| dsCommandOptionBool_LgcyEXTNAMES | 47 = Sets the parameters of named entities to specific AutoCAD versions (see Remarks ): False = AutoCAD Release 14 parameters True = AutoCAD 2000 and later parameters |
| dsCommandOptionBool_LgcyUCSFOLLOW | 48 = Creates a plan view whenever the custom coordinate system (CCS) changes (see Remarks ): False = CCS has no effect True = Changing CCS changes plan view |
| dsCommandOptionBool_LgcyVISRETAIN | 49 = Turns visibility of layers in external reference files on or off (see Remarks ): False = Off True = On |
| dsCommandOptionBool_SetAngDir | 50 = Tools > Options > Drawing Settings > Unit System > Base angle: False = Counterclockwise True = Clockwise |
| dsCommandOptionBool_SetDmTxtHPosBtwn | 51 = Tools > Options > Drafting Style > Dimension > Text > Text settings > Text alignment: False = Text aligned with dimension lines True = Text drawn horizontally |
| dsCommandOptionBool_SetFLXOLESTARTUP | 52 = Sets whether an embedded OLE object's source application loads when printing: False = Not loaded True = Loaded |
| dsCommandOptionBool_SetSktchMode | 53 = Sets whether the SKETCH command draws Lines or PolyLines: False = Draw Lines True = Draw PolyLines |
| dsCommandOptionBool_SetTxtMirrMode | 54 = Sets how the MIRROR command reflects text: False = Keep text direction True = Mirror the text |
| dsCommandOptionBool_SetTxtPrnFill | Obsolete. Superseded by dsApplicationOptionBool_e . |
| dsCommandOptionBool_Undefined | 0 = Undefined |

## Remarks

The string **Lgcy** in a command option indicates that setting the command option has no effect in DraftSight; however, the value is stored in the DWG file.

In most instances, user-interface command option equivalents are the strings following **dsCommandOptionBool_**; for example, typing **EnblCSByVP** in the command prompt is equivalent to using **dsCommandOptionBool_EnblCSByVP** in code.

## See Also

[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IDocument::GetCommandOptionBool Method](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetCommandOptionBool.html)
[IDocument::SetCommandOptionBool Method](Interop.dsAutomation~Interop.dsAutomation.IDocument~SetCommandOptionBool.html)
