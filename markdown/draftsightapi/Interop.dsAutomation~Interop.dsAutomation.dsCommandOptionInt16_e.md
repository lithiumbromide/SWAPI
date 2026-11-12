---
title: "dsCommandOptionInt16_e Enumeration"
project: ""
interface: "dsCommandOptionInt16_e"
member: ""
kind: "enum"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.dsCommandOptionInt16_e.html"
---

# dsCommandOptionInt16_e Enumeration

Command options with Int16 values.

## Syntax

### Visual Basic

```vb
Public Enum dsCommandOptionInt16_e
   Inherits System.Enum
```

### C#

```csharp
public enum dsCommandOptionInt16_e : System.Enum
```

### JScript

```
public enum dsCommandOptionInt16_e extends System.Enum
```

### Managed Extensions for C++

```
__value public enum dsCommandOptionInt16_e : public System.Enum
```

### C++/CLI

```cpp
public enum class dsCommandOptionInt16_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| dsCommandOptionInt16_Count | Obsolete. Superseded by dsApplicationOptionInt16_e . |
| dsCommandOptionInt16_EnblBlkXpld | Obsolete. Superseded by dsApplicationOptionInt16_e . |
| dsCommandOptionInt16_EnblChmfAng | Obsolete. Superseded by dsApplicationOptionInt16_e . |
| dsCommandOptionInt16_EnblClpFrmDsp | 3 = Show xref clipping frame in the current drawing: 0 = Not visible and not printed 1 = Visible and printed 2 = Visible but not printed |
| dsCommandOptionInt16_EnblCmdDlgs | Obsolete. Superseded by dsApplicationOptionInt16_e . |
| dsCommandOptionInt16_EnblCmdEcho | 5 = Echo prompts and input for LISP command: 0 = Off 1 = On |
| dsCommandOptionInt16_EnblDrgDsp | 6 = Display outlines of dragged entities: 0 = Off 1 = Not implemented 2 = On |
| dsCommandOptionInt16_EnblEdgeExtd | Obsolete. Superseded by dsApplicationOptionInt16_e . |
| dsCommandOptionInt16_EnblEGripBlk | Obsolete. Superseded by dsApplicationOptionInt16_e . |
| dsCommandOptionInt16_EnblEGripTpDsp | Obsolete. Superseded by dsApplicationOptionInt16_e . |
| dsCommandOptionInt16_EnblEntSelHlt | Obsolete. Superseded by dsApplicationOptionInt16_e . |
| dsCommandOptionInt16_EnblETrkDsp | Obsolete. Superseded by dsApplicationOptionInt16_e . |
| dsCommandOptionInt16_EnblFltTrm | Obsolete. Superseded by dsApplicationOptionInt16_e . |
| dsCommandOptionInt16_EnblHtchBndTyp | 13 = Set the type of entity created by the BHATCH and BOUNDARY commands: 0 = Region 1 = PolyLine |
| dsCommandOptionInt16_EnblHtchDbl | 14 = Set hatch pattern doubling for user-defined patterns: 0 = Off 1 = On |
| dsCommandOptionInt16_EnblMMBPan | Obsolete. Superseded by dsApplicationOptionInt16_e . |
| dsCommandOptionInt16_EnblMutt | Obsolete. Superseded by dsApplicationOptionInt16_e . |
| dsCommandOptionInt16_EnblPEdtCnvrtWrng | Obsolete. Superseded by dsApplicationOptionInt16_e . |
| dsCommandOptionInt16_EnblRSnp | Obsolete. Superseded by dsApplicationOptionInt16_e . |
| dsCommandOptionInt16_EnblTlTps | Obsolete. Superseded by dsApplicationOptionInt16_e . |
| dsCommandOptionInt16_EnblUntSpcSupp | 20 = Set display format for units: 0 = Fractional, feet and inches, and surveyor's angles using spaces as delimiters 1 = Fractional, feet and inches, and surveyor's angles including spaces or sometimes dashes instead of spaces |
| dsCommandOptionInt16_GetActVP | 21 = Set the ID number of the active Viewport; valid IDs 1-4 |
| dsCommandOptionInt16_GetLstErr | 22 = Set the number of the error code when a LISP function call causes an error detected by DraftSight |
| dsCommandOptionInt16_GetNmCdePg | Obsolete. Superseded by dsApplicationOptionInt16_e . |
| dsCommandOptionInt16_GetStatActCmd | 24 = Show the type of active command (read-only bitcode): 0 = None 1 = Ordinary 2 = Transparent 4 = Script 8 = Dialog |
| dsCommandOptionInt16_GetStatCCS | 25 = Get whether custom coordinate system (CCS) is the same as world coordinate system (WCS) (read only): 0 = False 1 = True |
| dsCommandOptionInt16_GetStateUndo | 26 = Get the state of UNDO command options (read-only bitcode): 0 = UNDO Off 1 = UNDO on 2 = Only one command can be undone 4 = Auto on 8 = Group currently active 16 = Zoom and pan are grouped as single action 32 = Layer property operations are grouped as single action |
| dsCommandOptionInt16_GetStatLstDlg | 27 = Get how the most recently used dialog was closed (read only): 0 = Cancel 1 = OK |
| dsCommandOptionInt16_GetStatScreen | Obsolete. Superseded by dsApplicationOptionInt16_e . |
| dsCommandOptionInt16_LgcyACISOUTVER | Obsolete. Superseded by dsApplicationOptionInt16_e . |
| dsCommandOptionInt16_LgcyDBMOD | 30 = Show drawing modification status (bitcode and see Remarks ): 1 = Database modified 4 = Database variable modified 8 = Window modified 16 = View modified 32 = Field modified |
| dsCommandOptionInt16_LgcyDIMFIT | 31 = Obsolete |
| dsCommandOptionInt16_LgcyDIMUNIT | 32 = Set units for all dimension types (see Remarks ): 0 = Scientific 1 = Decimal 2 = Engineering 3 = Windows Desktop |
| dsCommandOptionInt16_LgcyDWGCODEPAGE | 33 = Store system code page (read only and see Remarks ) |
| dsCommandOptionInt16_LgcyHALOGAP | 34 = Display a gap where an entity is hidden by another entity in 2D views (see Remarks ) |
| dsCommandOptionInt16_LgcyHANDLES | 35 = Indicate if entity handles are accessible by applications (see Remarks ) |
| dsCommandOptionInt16_LgcyINDEXCTL | 36 = Set whether layer and spatial indexes are created and saved in drawings (see Remarks ): 0 = No indexes created 1 = Layer index created 2 = Spatial index created 3 = Layer and spatial indexes created |
| dsCommandOptionInt16_LgcyISOLINES | 37 = Set the number of contour lines per surface on entities; valid values 0 through 2047 (see Remarks ) |
| dsCommandOptionInt16_LgcyOBSCUREDCOLOR | 38 = Sets color of obscured lines, which are only visible in 2D views and when dsCommandOptionInt16_LgcyOBSCUREDLTYPE is a non-0 value (see Remarks ): 0 = ByBlock 1-255 = designated color 256 = By Layer |
| dsCommandOptionInt16_LgcyOBSCUREDLTYPE | 39 = Set LineType of obscured lines (see Remarks ): 0 = Off 1 = Solid 2 = Dashed 3 = Dotted 4 = Short dash 5 = Medium dash 6 = Long dash 7 = Double short dash 8 = Double medium dash 9 = Double long dash 10 = Medium long dash 11 = Sparse dash |
| dsCommandOptionInt16_LgcySHADEDGE | 40 = Set how to shade edges in rendering (see Remarks ): 0 = Faces shaded, edges not highlighted 1 = Faces shaded, edges in background color 2 = Faces not filled, edges in entity color 3 = Faces in entity color, edges in background color |
| dsCommandOptionInt16_LgcySHADEDIF | 41 = Set the diffuse reflective light to ambient light ratio, which is a percentage of diffuse reflective light when dsCommandOptionInt16_LgcySHADEDGE is set to 0 or 1 (see Remarks ) |
| dsCommandOptionInt16_LgcySORTENTS | 42 = Set entity sorting for draw; valid values 1-127 (see Remarks ) |
| dsCommandOptionInt16_LgcySTARTUP | Obsolete. Superseded by dsApplicationOptionInt16_e . |
| dsCommandOptionInt16_LgcyVIEWMODE | 44 = View mode for active Viewport (read-only bitcode and see Remarks ): 0 = Off 1 = Perspective view active 2 = Front clipping on 4 = Back clipping on 8 = CCS mode on 16 = Front clip not at eye. If on, front clip distance determines front clipping plane; if off, front clip distance is ignored, and front clipping plane is set to pass through the camera point; this option is ignored if the front-clipping bit (2) is off |
| dsCommandOptionInt16_LgcyWMFBKGND | Obsolete. Superseded by dsApplicationOptionInt16_e . |
| dsCommandOptionInt16_LgcyWMFFOREGND | Obsolete. Superseded by dsApplicationOptionInt16_e . |
| dsCommandOptionInt16_SetActBlkInsUnt | Obsolete. Superseded by dsApplicationOptionInt16_e . |
| dsCommandOptionInt16_SetActLClr | 48 = Tools > Options > Drafting Styles > Active Drafting Styles > Line Font > Line Color: 0 = ByBlock 1 = Red 2 = Yellow 3 = Green 4 = Cyan 5 = Blue 6 = Magenta 7 = White 8 − 256 = Specify Color |
| dsCommandOptionInt16_SetActLWt | 49 = Tools > Options > Drafting Styles > Active Drafting Styles > Line Font > Line Weight > Line Weight: -3 = Default -2 = ByBlock -1 = ByLayer 0 = 0.00 mm or inches 5 = 0.05 mm or 0.002 inches 9 = 0.09 mm or 0.004 inches 13 = 0.13 mm or 0.005 inches 15 = 0.15 mm or 0.006 inches 18 = 0.18 mm or 0.007 inches 20 = 0.20 mm or 0.008 inches 25 = 0.25 mm or 0.010 inches |
| dsCommandOptionInt16_SetActPntStyl | 50 = Format > Point Style > Points > Type: 0 = . 1 = space 2 = + 3 = X 4 = \| (pipe) 32 = . within a circle 33 = circle 34 = + within a circle 35 = X within a circle 36 = half-pipe within a circle 64 = . within a square |
| dsCommandOptionInt16_SetActVPLvl | 51 = Set the maximum number of Viewports active at the same time in a layout |
| dsCommandOptionInt16_SetAngDmPrc | 52 = Tools > Options > Drafting Styles > Dimension > Angular Dimension > Angular dimension settings > Precision: 0 = 0 1 = 0.0 2 = 0.00 3 = 0.000 4 = 0.0000 5 = 0.00000 6 = 0.000000 7 = 0.0000000 8 = 0.00000000 |
| dsCommandOptionInt16_SetAngDmUnt | 53 = Tools > Options > Drafting Styles > Dimension > Angular Dimension > Angular dimension settings > Format: 0 = Decimal Degrees 1 = Deg/Min/Sec 2 = Grads 3 = Radians |
| dsCommandOptionInt16_SetAngDmZroDsp | 54 = Tools > Options > Drafting Styles > Dimension > Angular Dimension > Angular dimension settings > Zeroes display: 0 = Show leading and trailing zeroes 1 = Hide leading zeroes 2 = Hide trailing zeroes 3 = Hide leading and trailing zeroes |
| dsCommandOptionInt16_SetAngPrc | 55 = Tools > Options > Drawing Settings > Unit System > Angle > Precision: 0 = 0 1 = 0.0 2 = 0.00 3 = 0.000 4 = 0.0000 5 = 0.00000 6 = 0.000000 7 = 0.0000000 8 = 0.00000000 |
| dsCommandOptionInt16_SetAngUnt | 56 = Tools > Options > Drawing Settings > Unit System > Angle > Type : 0 = Decimal Degrees 1 = Deg/Min/Sec 2 = Grads 3 = Radians 4 = Surveyor's UnitSystem |
| dsCommandOptionInt16_SetBAttDsp | 57 = Tools > Options > Drawing Settings > Display > Show block attributes: 0 = Normal 1 = On 2 = Off |
| dsCommandOptionInt16_SetBAttMode | Obsolete. Superseded by dsApplicationOptionInt16_e . |
| dsCommandOptionInt16_SetBlkInsUnt | 59 = Tools > Options > Drawing Settings > Unit System > Block units format: 0 = Unitless 1 = Inches 2 = Feet 3 = Miles 4 = Millimeters 5 = Centimeters 6 = Meters 7 = Kilometers 8 = Microinches 9 = Mils 10 = Yards 11 = Angstroms 12 = Nanometers 13 = Microns 14 = Decimeters 16 = Hectometers 17 = Gigameters 18 = Astronomical 19 = Light Years 20 = Parsecs |
| dsCommandOptionInt16_SetCCSAxisAng | Obsolete. Superseded by dsApplicationOptionInt16_e . |
| dsCommandOptionInt16_SetCOLORTHEME | Do not use. |
| dsCommandOptionInt16_SetCompEdFd | Obsolete. Superseded by dsApplicationOptionInt16_e . |
| dsCommandOptionInt16_SetCrdDsp | Obsolete. Superseded by dsApplicationOptionInt16_e . |
| dsCommandOptionInt16_SetCSIcnDsp | 63 = Tools > Options > Drawing Settings > Display > Coordinate System Icon > Display icon: 0 = Do not display icon 1 = Display icon 2 = Display icon at origin 3 = Display icon and Display icon at origin |
| dsCommandOptionInt16_SetDfltLWt | Obsolete. Superseded by dsApplicationOptionInt16_e . |
| dsCommandOptionInt16_SetDlDmPrc | 65 = Tools > Options > Drafting Styles > Dimension > Dual Dimension > Precision: 0 = 0 1 = 0.0 2 = 0.00 3 = 0.000 4 = 0.0000 5 = 0.00000 6 = 0.000000 7 = 0.0000000 8 = 0.00000000 |
| dsCommandOptionInt16_SetDlDmUnt | 66 = Tools > Options > Drafting Styles > Dimension > Dual Dimension > Format: 1 = Scientific 2 = Decimal 3 = Engineering 4 = Architectural Stacked 5 = Fractional Stacked 6 = Architectural 7 = Fractional 8 = Windows Desktop |
| dsCommandOptionInt16_SetDmDLClr | 67 = Tools > Options > Drafting Styles > Dimension > Line > Dimension line settings > Color: 0 = ByBlock 1 = Red 2 = Yellow 3 = Green 4 = Cyan 5 = Blue 6 = Magenta 7 = White 8 − 256 = Specify Color |
| dsCommandOptionInt16_SetDmDLWt | 68 = Tools > Options > Drafting Styles > Dimension > Line > Dimension line settings > Weight: -3 = Default -2 = ByBlock -1 = ByLayer 0 = 0.00 mm 5 = 0.05 mm 9 = 0.09 mm 13 = 0.13 mm 15 = 0.15 mm 18 = 0.18 mm 20 = 0.20 mm 25 = 0.25 mm 30 = 0.30 mm 35 = 0.35 mm 40 = 0.40 mm 50 = 0.50 mm 53 = 0.53 mm 60 = 0.60 mm 70 = 0.70 mm 80 = 0.80 mm 90 = 0.90 mm 100 = 1.00 mm 106 = 1.06 mm 120 = 1.20 mm 140 = 1.40 mm 158 = 1.58 mm 200 = 2.00 mm 211 = 2.11 mm |
| dsCommandOptionInt16_SetDmELClr | 69 = Tools > Options > Drafting Styles > Dimension > Line > Extension line settings > Styles > Color: 0 = ByBlock 1 = Red 2 = Yellow 3 = Green 4 = Cyan 5 = Blue 6 = Magenta 7 = White 8 − 256 = Specify Color |
| dsCommandOptionInt16_SetDmELWt | 70 = Tools > Options > Drafting Styles > Dimension > Line > Extension line settings > Styles > Weight: -3 = Default -2 = ByBlock -1 = ByLayer 0 = 0.00 mm 5 = 0.05 mm 9 = 0.09 mm 13 = 0.13 mm 15 = 0.15 mm 18 = 0.18 mm 20 = 0.20 mm 25 = 0.25 mm 30 = 0.30 mm 35 = 0.35 mm 40 = 0.40 mm 50 = 0.50 mm 53 = 0.53 mm 60 = 0.60 mm 70 = 0.70 mm 80 = 0.80 mm 90 = 0.90 mm 100 = 1.00 mm 106 = 1.06 mm 120 = 1.20 mm 140 = 1.40 mm 158 = 1.58 mm 200 = 2.00 mm 211 = 2.11 mm |
| dsCommandOptionInt16_SetDmFitMode | 71 = Sets how to move dimension text and arrows when there is insufficient space to place both within extension lines: 0 = Move text and arrows outside extension lines 1 = Move arrows, then text 2 = Move text, then arrows 3 = Move either text or arrows, whichever fits best NOTE : A leader is added to the dimension text that was moved when dsCommandOptionInt16_SetDmTxtMvMode is set to 1. |
| dsCommandOptionInt16_SetDmRltvMode | 72 = Associate dimension entities, e.g., lines, arcs, arrowheads, text, etc., and set whether to explode dimensions: 0 = Explode dimensions; no association among dimension entities 1 = Create dimension entities that are not associated 2 = Create dimension entities that are associated |
| dsCommandOptionInt16_SetDmTxtClr | 73 = Tools > Options > Drafting Styles > Dimension > Text > Text settings > Color: 0 = ByBlock 1 = Red 2 = Yellow 3 = Green 4 = Cyan 5 = Blue 6 = Magenta 7 = White 8 − 256 = Specify Color |
| dsCommandOptionInt16_SetDmTxtHPos | 74 = Tools > Options > Drafting Styles > Dimension > Text > Text position > Horizontal: 0 = Centered 1 = At Ext Line 1 2 = At Ext Line 2 3 = Over Ext Line 1 4 = Over Ext Line 2 |
| dsCommandOptionInt16_SetDmTxtMvMode | 75 = Set how to move dimension text: 0 = Move dimension line with dimension text 1 = Add a leader when dimension text is moved 2 = Allow text to be moved without a leader |
| dsCommandOptionInt16_SetDmTxtVPosFit | 76 = Tools > Options > Drafting Styles > Dimension > Text > Text position > Vertical: 0 = Centered 1 = Above 2 = Outside 3 = JIS |
| dsCommandOptionInt16_SetDmZroDsp | 77 = Set how to suppress zeros in the primary dimension value: 0 = Suppress zero feet and zero inches 1 = Include zero feet and zero inches 2 = Include zero feet and suppress zero inches 3 = Suppress zero feet and include zero inches 4 = Suppress leading zeros in decimal dimensions 8 = Suppress trailing zeros in decimal dimensions 12 = Suppress leading and trailing zeros |
| dsCommandOptionInt16_SetEGripActClr | Obsolete. Superseded by dsApplicationOptionInt16_e . |
| dsCommandOptionInt16_SetEGripDspLmt | Obsolete. Superseded by dsApplicationOptionInt16_e . |
| dsCommandOptionInt16_SetEGripDspMode | Obsolete. Superseded by dsApplicationOptionInt16_e . |
| dsCommandOptionInt16_SetEGripInActClr | 81 = Tools > Options > User Preferences > Drafting Options > Entity Selection > EGrips Colors > Inactive EGrips: 1 = Red 2 = Yellow 3 = Green 4 = Cyan 5 = Blue 6 = Magenta 7 = White 8 − 256 = Specify Color |
| dsCommandOptionInt16_SetEntSelMode | 82 = Tools > Options > User Preferences > Drafting Options > Entity Selection > Selection Settings > Enable EntityGroup selection sets: 0 = Disabled 1 = Enabled |
| dsCommandOptionInt16_SetESnpMode | Obsolete. Superseded by dsApplicationOptionInt16_e . |
| dsCommandOptionInt16_SetFLXPROXYGRAPHICS | 84 = Set whether images of proxy entities are saved in drawings: 0 = Do not save image with drawing 1 = Save image with drawing |
| dsCommandOptionInt16_SetFLXSPLINETYPE | 85 = Set the type of spline curve created when using PEDIT command: 5 = Quadratic b-spline 6 = Cubic b-spline |
| dsCommandOptionInt16_SetGBoxSz | Obsolete. Superseded by dsApplicationOptionInt16_e . |
| dsCommandOptionInt16_SetHtchPlcmnt | 87 = Set the order in which to draw hatches and fills: 0 = No order 1 = Hatch or fill is drawn behind all other entities 2 = Hatch or fill is drawn in front of all other entities 3 = Hatch or fill is drawn behind hatch boundary 4 = Hatch or fill is drawing in front of hatch boundary |
| dsCommandOptionInt16_SetHtchRltvMode | Obsolete. Superseded by dsApplicationOptionInt16_e .v |
| dsCommandOptionInt16_SetIsoPln | 89 = Set the active Viewport's isometric plane 0 = Left 1 = Top 2 = Right |
| dsCommandOptionInt16_SetLDmDecSym | 90 = Tools > Options > Drafting Styles > Dimension > Linear Dimension > Decimal separator: Period Comma Space |
| dsCommandOptionInt16_SetLDmFrmt | 91 = Set the fraction format when dsCommandOptionInt16_SetLWtUnt is set to architectural or fractional: 0 = Horizontal stacking 1 = Diagonal stacking 2 = Not stacked |
| dsCommandOptionInt16_SetLDmPrc | 92 = Tools > Options > Drafting Styles > Dimension > Linear Dimension > Precision: 0 = 0 1 = 0.0 2 = 0.00 3 = 0.000 4 = 0.0000 5 = 0.00000 6 = 0.000000 7 = 0.0000000 8 = 0.00000000 |
| dsCommandOptionInt16_SetLDmUnt | 93 = Tools > Options > Drafting Styles > Dimension > Linear Dimension > Format: 1 = Scientific 2 = Decimal 3 = Engineering 4 = Architectural 5 = Fractional 6 = Windows Desktop |
| dsCommandOptionInt16_SetLogMode | Obsolete. Superseded by dsApplicationOptionInt16_e . |
| dsCommandOptionInt16_SetLWtUnt | Obsolete. Superseded by dsApplicationOptionInt16_e . |
| dsCommandOptionInt16_SetMnuEcho | Obsolete. Superseded by dsApplicationOptionInt16_e . |
| dsCommandOptionInt16_SetNoteJst | 97 = Set multi-line justification: 0 = Top 1 = Middle 2 = Bottom |
| dsCommandOptionInt16_SetOfstGapMode | Obsolete. Superseded by dsApplicationOptionInt16_e . |
| dsCommandOptionInt16_SetOLEQlty | Obsolete. Superseded by dsApplicationOptionInt16_e . |
| dsCommandOptionInt16_SetPEdtSmthMode | 100 = Specifies the surface-fitting type for Smooth option of PEDIT: 5 = Quadratic b-spline surface 6 = Cubic b-spline surface 8 = Bezier surface |
| dsCommandOptionInt16_SetPEdtSplSegs | 101 = Specifies the number of line segments to generate for any spline-fit PolyLine created by the Spline option of PEDIT; valid values: -32768 − 32767, except 0; if a negative value, then segments are created using the absolute value of the setting and a fit-type curve is applied to those segments |
| dsCommandOptionInt16_SetPGonSides | Obsolete. Superseded by dsApplicationOptionInt16_e . |
| dsCommandOptionInt16_SetPntrSz | Obsolete. Superseded by dsApplicationOptionInt16_e . |
| dsCommandOptionInt16_SetPrnRot | Obsolete. Superseded by dsApplicationOptionInt16_e . |
| dsCommandOptionInt16_SetProjMode | Obsolete. Superseded by dsApplicationOptionInt16_e . |
| dsCommandOptionInt16_SetPrxyDspMode | Obsolete. Superseded by dsApplicationOptionInt16_e . |
| dsCommandOptionInt16_SetRefBindMode | 107 = Set how to handle xref names when binding or editing attaching reference files: 0 = Traditional binding behavior 1 = Insert-like behavior |
| dsCommandOptionInt16_SetSelBoxSz | Obsolete. Superseded by dsApplicationOptionInt16_e . |
| dsCommandOptionInt16_SetShrtCtMnuMode | Obsolete. Superseded by dsApplicationOptionInt16_e . |
| dsCommandOptionInt16_SetSrfMU | 110 = Set the surface density for PEDIT Smooth in M direction and the U isolines density on surface entities; valid values 0-200; meshes must be created with a minimum surface density of 2 |
| dsCommandOptionInt16_SetSrfTbs1 | 111 = Set the number of tabulated surfaces to generate for RULESURF and TABSURF; also set mesh density in M direction for REVSURF and EDGESURF; valid values 2-32766 |
| dsCommandOptionInt16_SetSrfTbs2 | 112 = Set mesh density in N direction for REVSURF and EDGESURF; valid values 2-32766 |
| dsCommandOptionInt16_SetSrgNV | 113 = Set the surface density for PEDIT Smooth in M direction and the V isolines density on surface entities; valid values 0-200; meshes must be created with a minimum surface density of 2 |
| dsCommandOptionInt16_SetStkFracTxtHt | 114 = Set the stacked text's fraction height relative to selected text's current height; valid values 25-125 percent |
| dsCommandOptionInt16_SetStkFracTyp | 115 = Set the vertical alignment of stacked text: 0 = Bottom 1 = Center 2 = Top |
| dsCommandOptionInt16_SetTDmDPrc | 116 = Tools > Options > Drafting Styles > Dimension > Dual Dimension > Dual dimension settings > Precision: 0 = 0 1 = 0.0 2 = 0.00 3 = 0.000 4 = 0.0000 5 = 0.00000 6 = 0.000000 7 = 0.0000000 8 = 0.00000000 |
| dsCommandOptionInt16_SetTDmPrc | 117 = Tools > Options > Drafting Styles > Dimension > Tolerance > Tolerance settings > Dual dimension: 0 = 0 1 = 0.0 2 = 0.00 3 = 0.000 4 = 0.0000 5 = 0.00000 6 = 0.000000 7 = 0.0000000 8 = 0.00000000 |
| dsCommandOptionInt16_SetTxtRes | 118 = Set the tessellation fineness resolution of text outlines; valid values 0-100 |
| dsCommandOptionInt16_SetUntMode | 119 = Tools > Options > Drawing Settings > Unit System > Length > Type: 1 = Scientific 2 = Decimal 3 = Engineering 4 = Architectural 5 = Fractional |
| dsCommandOptionInt16_SetUntPrc | 120 = Set the precision to display for units and coordinates: 0 = 0 1 = 0.0 2 = 0.00 3 = 0.000 4 = 0.0000 5 = 0.00000 6 = 0.000000 7 = 0.0000000 8 = 0.00000000 |
| dsCommandOptionInt16_SetUntTyp | 121 = Control whether hatch patterns and LineTypes display in imperial or metric units: 0 = Imperial 1 = Metric |
| dsCommandOptionInt16_SetUsrInt1 | 122 = User- or application-defined integer |
| dsCommandOptionInt16_SetUsrInt2 | 123 = User- or application-defined integer |
| dsCommandOptionInt16_SetUsrInt3 | 124 = User- or application-defined integer |
| dsCommandOptionInt16_SetUsrInt4 | 125 = User- or application-defined integer |
| dsCommandOptionInt16_SetUsrInt5 | 126 = User- or application-defined integer |
| dsCommandOptionInt16_Undefined | Obsolete. See dsApplicationOptionInt16_e . |

## Remarks

The string **Lgcy** in a command option indicates that setting the command option has no effect in DraftSight; however, the value is stored in the DWG file.

In most instances, user-interface command option equivalents are the strings following **dsCommandOptionInt16_**; for example, typing **SetUsrInt5** in the command prompt is equivalent to using **dsCommandOptionInt16_SetUsrInt5** in code.

## See Also

[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IDocument::GetCommandOptionInt16 Method](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetCommandOptionInt16.html)
[IDocument::SetCommandOptionInt16 Method](Interop.dsAutomation~Interop.dsAutomation.IDocument~SetCommandOptionInt16.html)
