---
title: "dsApplicationOptionInt16_e Enumeration"
project: ""
interface: "dsApplicationOptionInt16_e"
member: ""
kind: "enum"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.dsApplicationOptionInt16_e.html"
---

# dsApplicationOptionInt16_e Enumeration

Application options with Int16 values.

## Syntax

### Visual Basic

```vb
Public Enum dsApplicationOptionInt16_e
   Inherits System.Enum
```

### C#

```csharp
public enum dsApplicationOptionInt16_e : System.Enum
```

### JScript

```
public enum dsApplicationOptionInt16_e extends System.Enum
```

### Managed Extensions for C++

```
__value public enum dsApplicationOptionInt16_e : public System.Enum
```

### C++/CLI

```cpp
public enum class dsApplicationOptionInt16_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| dsApplicationOptionInt16_Count | Not used |
| dsApplicationOptionInt16_EnblBlkXpld | 1 = Explode non-uniformly scaled (NUS) blocks (only affects explode command): 0 = False 1 = True |
| dsApplicationOptionInt16_EnblChmfAng | 2 = Set chamfer input method: 0 = Two chamfer distances 1 = One chamfer length and one angle |
| dsApplicationOptionInt16_EnblCmdDlgs | 3 = Show in-place text editor for the LEADER and QLEADER commands: 0 = Off 1 = On |
| dsApplicationOptionInt16_EnblDrgDsp | 4 = Display outlines of dragged entities: 0 = Off 1 = Not implemented 2 = On |
| dsApplicationOptionInt16_EnblEdgeExtd | 5 = Set TRIM and EXTEND commands for cutting and boundary edges: 0 = Use the selected edge without an extension 1 = Extend or trim the selected entity to an imaginary extension of the cutting or boundary edge |
| dsApplicationOptionInt16_EnblEGripBlk | 6 = Tools > Options > User Preferences > Drafting Options > Entity Selection > EGrips Options > Enable EGrips in Blocks: 0 = Enable EntityGrips (EGrips) 1 = Enable EGrips in Blocks |
| dsApplicationOptionInt16_EnblEGripTpDsp | 7 = Tools > Options > User Preferences > Drafting Options > Entity Selection > EGrips Options > Enable EGrips tips: 0 = Enable EGrips tips off 1 = Enable EGrips tips on |
| dsApplicationOptionInt16_EnblEntSelHlt | 8 = Tools > Options > User Preferences > Drafting Options > Entity Selection > Pre-selected highlighting > When prompted to specify entities: 0 = Off 1 = On |
| dsApplicationOptionInt16_EnblETrkDsp | 9 = Tools > Options > User Preferences > Drafting Options > Display > ETrack > Display ETrack guides across screen: 0 = Off 1 = On |
| dsApplicationOptionInt16_EnblFltTrm | 10 = Trim selected chamfer and fillet edges: 0 = Off 1 = On |
| dsApplicationOptionInt16_EnblMMBPan | 11 = Set the behavior of the third button or wheel on the mouse: 0 = Supports the action defined in the customization file 1 = Supports panning |
| dsApplicationOptionInt16_EnblMutt | 12 = Set whether to suppress displaying a message when it typically would not be suppressed: 0 = Off 1 = On |
| dsApplicationOptionInt16_EnblPEdtCnvrtWrng | 13 = Set whether to suppress the error message in PEDIT when the selected entity is not a PolyLine: 0 = Off 1 = On |
| dsApplicationOptionInt16_EnblRSnp | 14 = Tools > Options > User Preferences > Drafting Options > Pointer Control > Snap Settings > Radial (RSnap): 0 = Off 1 = On |
| dsApplicationOptionInt16_EnblTlTps | 15 = Tools > Options > System Options > Graphics Area > Display ESnap tooltips: 0 = Off 1 = On |
| dsApplicationOptionInt16_GetNmCdePg | 16 = Show the system code page, which is determined by the operating system (read only) |
| dsApplicationOptionInt16_GetStatScreen | 17 = Get screen state (read only): 1 = Text screen is displayed 2 = Drawing area is displayed 3 = Both screens are displayed |
| dsApplicationOptionInt16_LgcyACISOUTVER | 18 = Set ACIS version of SAT files created using ACISOUT command; valid values 15-18, 20, 21, 30, 31, 40, 50, 60, and 70 (see Remarks ) |
| dsApplicationOptionInt16_LgcySTARTUP | 19 = Specify 0 or 1 to display the Specify Template dialog when NEW is typed at the command prompt, or to create a new drawing document when QNEW command is typed in the command prompt (see Remarks ) |
| dsApplicationOptionInt16_LgcyWMFBKGND | 20 = Set the background display when entities are inserted in Windows metafile format (WMF) (see Remarks ): 0 = background is transparent; foreground color is dsCommandOptionInt16_LgcyWMFFOREGND 1 = background color same as drawing's current background color; foreground color unchanged |
| dsApplicationOptionInt16_LgcyWMFFOREGND | 21 = Set the foreground color when entities are inserted in WMF (see Remarks ): 0 = If needed, foreground and background colors are swapped so that the foreground color is darker than the background color 1 = If needed, foreground and background colors are swapped so that the foreground color is lighter than the background color |
| dsApplicationOptionInt16_SetActBlkInsUnt | 22 = Tools > Options > System Options > Drawing File Defaults > Block insertion units > Units for inserting entities: 0 = Unitless 1 = Inches 2 = Feet 3 = Miles 4 = Millimeters 5 = Centimeters 6 = Meters 7 = Kilometers 8 = Microinches 9 = Mils 10 = Yards 11 = Angstroms 12 = Nanometers 13 = Microns 14 = Decimeters 16 = Hectometers 17 = Gigameters 18 = Astronomical 19 = Light Years 20 = Parsecs |
| dsApplicationOptionInt16_SetBAttMode | 23 = Sets BlockAttribute options (bitcode): 0 = None 1 = Invisible 2 = Constant 4 = Verify 8 = Preset 16 = Lock position in Block |
| dsApplicationOptionInt16_SetCCSAxisAng | 24 = Set the default angle, in degrees, when rotating the CCS around one of its axes using the x, y, or z option of the CCS command: 5 10 15 18 22.5 30 45 90 180 |
| dsApplicationOptionInt16_SetCOLORTHEME | Do not use. |
| dsApplicationOptionInt16_SetCompEdFd | 25 = Set the fading intensity for references being edited in-place; valid values 0-90 |
| dsApplicationOptionInt16_SetCrdDsp | 26 = Set how often to update and the format of the coordinates on the status line: 0 = Only when points are specified 1 = Continuously 2 = Continuously except when a point, distance, or angle is requested; then relative polar coordinates are displayed for x and y; z is always displayed as an absolute coordinate 3 = Continuously with latitude and longitude coordinate values of geographic location |
| dsApplicationOptionInt16_SetDfltLWt | 27 = Tools > Options > Drafting Styles > Active Drafting Styles > Line Font > Line Weight > Default Weight: -3 = Default -2 = ByBlock -1 = ByLayer 0 = 0.00 mm or inches 5 = 0.05 mm or 0.002 inches 9 = 0.09 mm or 0.004 inches 13 = 0.13 mm or 0.005 inches 15 = 0.15 mm or 0.006 inches 18 = 0.18 mm or 0.007 inches 20 = 0.20 mm or 0.008 inches 25 = 0.25 mm or 0.010 inches 30 = 0.30 mm or 0.012 inches 35 = 0.35 mm or 0.014 inches 40 = 0.40 mm or 0.016 inches 50 = 0.50 mm or 0.020 inches 53 = 0.53 mm or 0.021 inches 60 = 0.60 mm or 0.024 inches 70 = 0.70 mm or 0.028 inches 80 = 0.80 mm or 0.031 inches 90 = 0.90 mm or 0.035 inches 100 = 1.00 mm or 0.039 inches 106 = 1.06 mm or 0.042 inches 120 = 1.20 mm or 0.047 inches 140 = 1.40 mm or 0.055 inches 158 = 1.58 mm or 0.062 inches 200 = 2.00 mm or 0.079 inches 211 = 2.11 mm or 0.083 inches |
| dsApplicationOptionInt16_SetEGripActClr | 28 = Tools > Options > User Preferences > Drafting Options > Entity Selection > EGrips Colors > Active EGrips: 1 = Red 2 = Yellow 3 = Green 4 = Cyan 5 = Blue 6 = Magenta 7 = White 8 − 256 = Specify Color |
| dsApplicationOptionInt16_SetEGripDspLmt | 29 = Tools > Options > User Preferences > Drafting Options > Entity Selection > EGrips Options > EGrip display limit ; valid values 0-32767 |
| dsApplicationOptionInt16_SetEGripDspMode | 30 = Tools > Options > User Preferences > Drafting Options > Entity Selection > EGrips Options > Enable EntityGrips (EGrips): 0 = Disabled 1 = Enabled |
| dsApplicationOptionInt16_SetEGripInActClr | 31 = Tools > Options > User Preferences > Drafting Options > Entity Selection > EGrips Colors > Inactive EGrips: 1 = Red 2 = Yellow 3 = Green 4 = Cyan 5 = Blue 6 = Magenta 7 = White 8 − 256 = Specify Color |
| dsApplicationOptionInt16_SetEntSelMode | 32 = Tools > Options > User Preferences > Drafting Options > Entity Selection > Selection Settings > Enable EntityGroup selection sets: 0 = Disabled 1 = Enabled |
| dsApplicationOptionInt16_SetESnpMode | 33 = Tools > Options > User Preferences > Drafting Options > Pointer Control > Entity Snaps (bitcode): 0 = Clear entity snaps 1 = End 2 = Midpoint 4 = Center 8 = Node 16 = Quadrant 32 = Intersection 64 = Insert 128 = Perpendicular 256 = Tangent 512 = Nearest 2048 = Visual Intersection 4096 = Extension |
| dsApplicationOptionInt16_SetGBoxSz | 34 = Tools > Options > User Preferences > Drafting Options > Display > Gravity Box > GravityBox size ; valid values 1-20 |
| dsApplicationOptionInt16_SetHtchRltvMode | 35 = Set whether hatch patterns and gradient fills are associated with their boundaries: No Yes; updated when their boundaries change |
| dsApplicationOptionInt16_SetLogMode | 36 = Set whether to write the contents of the text window to a log file: 0 = No 1 = Yes |
| dsApplicationOptionInt16_SetLWtUnt | 37 = Tools > Options > Drafting Styles > Active Drafting Styles > Line Font > Line Weight > Inches or Millimeters: 0 = Inches 1 = Millimeters |
| dsApplicationOptionInt16_SetMnuEcho | 38 = Specify menu echo behavior: 1 = Suppress echo of menu items 2 = Suppress display of system prompts during menu 4 = Disable menu echo ^P toggle 8 = Display input/output strings |
| dsApplicationOptionInt16_SetOfstGapMode | 39 = Specify how to handle gaps between segments for closed PolyLines that are offset: 0 = Fill gaps by extending PolyLine segments 1 = Fill gaps with filleted arc segments, where the radius of each arc segment is equal to the offset distance 2 = Fill gaps with chamfered line segments, where the perpendicular distance to each chamfer is equal to the offset distance |
| dsApplicationOptionInt16_SetOLEQlty | 40 = Control the default print quality for OLE objects: 0 = Monochrome 1 = Low graphics 2 = High graphics 3 = Automatically select |
| dsApplicationOptionInt16_SetPGonSides | 41 = Specifies the default number for POLYGON; valid values: 3-1024 |
| dsApplicationOptionInt16_SetPntrSz | 42 = Tools > Options > System Options > Graphics Area > Pointer size ; valid values: 1-100 percent |
| dsApplicationOptionInt16_SetPrnRot | 43 = Sets print orientation: 0 = Rotate the printing area so that the corner with the Rotation icon aligns with the paper at the lower left for 0, top left for 90, top right for 180, and lower right for 270; x and y origin offsets are calculated relative to the lower-left corner 1 = Align the lower-left corner of the printing area with the lower-left corner of the paper 2 = Behave like 0 value, except that x and Y origin offsets are calculated relative to the rotated origin position |
| dsApplicationOptionInt16_SetProjMode | 44 = Specify the projection mode used with TRIM and EXTEND: 0 = No projection 1 = Project x,y plane of the current CCS 2 = Project to current view plane |
| dsApplicationOptionInt16_SetPrxyDspMode | 45 = Specify how to show proxy objects in drawings: 0 = Not displayed 1 = Images displayed for all proxy objects 2 = Only bounding box displayed for all proxy objects |
| dsApplicationOptionInt16_SetSelBoxSz | 46 = Tools > Options > User Preferences > Drafting Options > Entity Selection > Selection Settings > SelectionBox size ; valid values 0-50 |
| dsApplicationOptionInt16_SetShrtCtMnuMode | 47 = Tools > Options > User Preferences > Mouse Options > Options > Display shortcut menus by right-clicking ; valid values 0-20 |
| dsApplicationOptionInt16_Undefined | 48 = Undefined |

## Remarks

The string **Lgcy** in a command option indicates that setting the command option has no effect in DraftSight; however, the value is stored in the DWG file.

In most instances, user-interface command option equivalents are the strings following **dsApplicationOptionInt16_**; for example, typing **EnblBlkXpld** in the command prompt is equivalent to using **dsApplicationOptionInt16_EnblBlkXpld** in code.

## See Also

[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
