---
title: "dsCommandOptionString_e Enumeration"
project: ""
interface: "dsCommandOptionString_e"
member: ""
kind: "enum"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.dsCommandOptionString_e.html"
---

# dsCommandOptionString_e Enumeration

Command options for strings.

## Syntax

### Visual Basic

```vb
Public Enum dsCommandOptionString_e
   Inherits System.Enum
```

### C#

```csharp
public enum dsCommandOptionString_e : System.Enum
```

### JScript

```
public enum dsCommandOptionString_e extends System.Enum
```

### Managed Extensions for C++

```
__value public enum dsCommandOptionString_e : public System.Enum
```

### C++/CLI

```cpp
public enum class dsCommandOptionString_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| dsCommandOptionString_Count | Obsolete. Superseded by dsApplicationOptionString_e . |
| dsCommandOptionString_GetActCmd | 1 = Names of commands in use, both active and transparent (read only) |
| dsCommandOptionString_GetActComp | 2 = Name of reference being edited (read only) |
| dsCommandOptionString_GetActDict | Obsolete. Superseded by dsApplicationOptionString_e . |
| dsCommandOptionString_GetActDimStyl | 4 = Name of current dimension style (read only) |
| dsCommandOptionString_GetActTab | 5 = Name of current tab |
| dsCommandOptionString_GetActUsr | Obsolete. Superseded by dsApplicationOptionString_e . |
| dsCommandOptionString_GetInfOS | Obsolete. Superseded by dsApplicationOptionString_e . |
| dsCommandOptionString_GetLstPrmpt | 8 = Last string echoed at the command prompt (read only) |
| dsCommandOptionString_GetLstSvNm | Obsolete. Superseded by dsApplicationOptionString_e . |
| dsCommandOptionString_GetNmActCS | 10 = Name of current coordinate system for the active Viewport in the current space; empty string is returned if custom coordinate system (CCS) is not named (read only) |
| dsCommandOptionString_GetNmActPrfl | Obsolete. Superseded by dsApplicationOptionString_e . |
| dsCommandOptionString_GetNmAutoSvFl | Obsolete. Superseded by dsApplicationOptionString_e . |
| dsCommandOptionString_GetNmPrdct | Obsolete. Superseded by dsApplicationOptionString_e . |
| dsCommandOptionString_GetNmPrgm | Obsolete. Superseded by dsApplicationOptionString_e . |
| dsCommandOptionString_GetNmPrnStyl | 15 = PrintStyle table types (read only): STB, then default is ByLayer CTB, then default is ByColor |
| dsCommandOptionString_GetPlatform | Obsolete. Superseded by dsApplicationOptionString_e . |
| dsCommandOptionString_GetPthDS | Obsolete. Superseded by dsApplicationOptionString_e . |
| dsCommandOptionString_GetPthDWG | 18 = Drive and folder of active drawing (read only) |
| dsCommandOptionString_GetUsrStrn1 | 19 = User- or application-defined string |
| dsCommandOptionString_GetUsrStrn2 | 20 = User- or application-defined string |
| dsCommandOptionString_GetUsrStrn3 | 21 = User- or application-defined string |
| dsCommandOptionString_GetUsrStrn4 | 22 = User- or application-defined string |
| dsCommandOptionString_GetUsrStrn5 | 23 = User- or application-defined string |
| dsCommandOptionString_Lgcy_PKSER | Obsolete. Superseded by dsApplicationOptionString_e . |
| dsCommandOptionString_LgcyCANNOSCALE | 25 = Current annotation scale; only named scales in the drawing's named scales can be specified (see Remarks ) |
| dsCommandOptionString_LgcyPROJECTNAME | 26 = Project name for current drawing (see Remarks ) |
| dsCommandOptionString_LgcySHPNAME | Obsolete. Superseded by dsApplicationOptionString_e . |
| dsCommandOptionString_SetActBlkNm | 28 = Default Block name for INSERT |
| dsCommandOptionString_SetActLay | 29 = Tools > Options > Drafting Styles > Active Drafting Styles > Layer |
| dsCommandOptionString_SetActLStyl | 30 = Tools > Options > Drafting Styles > Active Drafting Styles > Line Font > Line Style |
| dsCommandOptionString_SetActMnu | Obsolete. Superseded by dsApplicationOptionString_e . |
| dsCommandOptionString_SetActTblStyl | 32 = Tools > Options > Drafting Styles > Active Drafting Styles > Table |
| dsCommandOptionString_SetActTxtStyl | 33 = Tools > Options > Drafting Styles > Active Drafting Styles > Text > Style |
| dsCommandOptionString_SetAltBgFnt | Obsolete. Superseded by dsApplicationOptionString_e . |
| dsCommandOptionString_SetAltFnt | Obsolete. Superseded by dsApplicationOptionString_e . |
| dsCommandOptionString_SetAltShp | Obsolete. Superseded by dsApplicationOptionString_e . |
| dsCommandOptionString_SetAutoSvPth | Obsolete. Superseded by dsApplicationOptionString_e . |
| dsCommandOptionString_SetBrwsrURL | Obsolete. Superseded by dsApplicationOptionString_e . |
| dsCommandOptionString_SetCCSBase | 37 = Active named CCS |
| dsCommandOptionString_SetDictFNm | Obsolete. Superseded by dsApplicationOptionString_e . |
| dsCommandOptionString_SetDmArwBlk | 39 = Tools > Options > Drafting Styles > Dimension > Arrows > Start arrow and End arrow: _ARCHTICK = Architectural tick _BOXBLANK = Box _BOXFILLED = Box filled _CLOSED = Closed _CLOSEDBLANK = Closed blank _DATUMBLANK = Datum triangle _DATUMFILLED = Datum triangle filled _DOT = Dot _DOTBLANK = Dot blank _DOTSMALL = Dot small empty string = Closed filled _INTEGRAL = Integral _NONE = None _OBLIQUE = Oblique _OPEN = Open _OPEN30 = Open 30 _OPEN90 = Right angle _ORIGIN = Origin indicator _ORIGIN2 = Origin indicator 2 _SMALL = Dot small blank |
| dsCommandOptionString_SetDmArwBlk1 | 40 = Tools > Options > Drafting Styles > Dimension > Arrows > Start arrow: _ARCHTICK = Architectural tick _BOXBLANK = Box _BOXFILLED = Box filled _CLOSED = Closed _CLOSEDBLANK = Closed blank _DATUMBLANK = Datum triangle _DATUMFILLED = Datum triangle filled _DOT = Dot _DOTBLANK = Dot blank _DOTSMALL = Dot small empty string = Closed filled _INTEGRAL = Integral _NONE = None _OBLIQUE = Oblique _OPEN = Open _OPEN30 = Open 30 _OPEN90 = Right angle _ORIGIN = Origin indicator _ORIGIN2 = Origin indicator 2 _SMALL = Dot small blank |
| dsCommandOptionString_SetDmArwBlk2 | 41 = Tools > Options > Drafting Styles > Dimension > Arrows > End arrow: _ARCHTICK = Architectural tick _BOXBLANK = Box _BOXFILLED = Box filled _CLOSED = Closed _CLOSEDBLANK = Closed blank _DATUMBLANK = Datum triangle _DATUMFILLED = Datum triangle filled _DOT = Dot _DOTBLANK = Dot blank _DOTSMALL = Dot small empty string = Closed filled _INTEGRAL = Integral _NONE = None _OBLIQUE = Oblique _OPEN = Open _OPEN30 = Open 30 _OPEN90 = Right angle _ORIGIN = Origin indicator _ORIGIN2 = Origin indicator 2 _SMALL = Dot small blank |
| dsCommandOptionString_SetDmLdrBlk | 42 = Tools > Options > Drafting Styles > Dimension > Arrows > Leader arrow: _ARCHTICK = Architectural tick _BOXBLANK = Box _BOXFILLED = Box filled _CLOSED = Closed _CLOSEDBLANK = Closed blank _DATUMBLANK = Datum triangle _DATUMFILLED = Datum triangle filled _DOT = Dot _DOTBLANK = Dot blank _DOTSMALL = Dot small empty string = Closed filled _INTEGRAL = Integral _NONE = None _OBLIQUE = Oblique _OPEN = Open _OPEN30 = Open 30 _OPEN90 = Right angle _ORIGIN = Origin indicator _ORIGIN2 = Origin indicator 2 _SMALL = Dot small blank |
| dsCommandOptionString_SetDmTxtStyl | 43 = Tools > Options > Drafting Styles > Dimension > Text > Text settings > Style |
| dsCommandOptionString_SetFntMpFNm | Obsolete. Superseded by dsApplicationOptionString_e . |
| dsCommandOptionString_SetHistFNm | 45 = Log file name (read only) |
| dsCommandOptionString_SetHtchPtrn | 46 = Draw > Hatch/Fill > Pattern > Pattern |
| dsCommandOptionString_SetHyprLnkBase | 47 = Path for all relative hyperlinks in a drawing |
| dsCommandOptionString_SetLDmPrfxSfx | 48 = Tools > Options > Drafting Styles > Dimension > Linear Dimension > Prefix and Suffix |
| dsCommandOptionString_SetLogPth | Obsolete. Superseded by dsApplicationOptionString_e . |
| dsCommandOptionString_SetNoteStyl | 50 = Tools > Options > Drafting Styles > Text > Style |
| dsCommandOptionString_SetPGdSpcAng | Obsolete. Superseded by dsApplicationOptionString_e . |
| dsCommandOptionString_SetPrmptTxt | Obsolete. Superseded by dsApplicationOptionString_e . |
| dsCommandOptionString_SetPSProLog | Obsolete. Superseded by dsApplicationOptionString_e . |
| dsCommandOptionString_SetPthTemp | Obsolete. Superseded by dsApplicationOptionString_e . |
| dsCommandOptionString_SetShtCSNm | 55 = Name of the CCS that defines the orthographic CCS settings in sheet space |
| dsCommandOptionString_SetTDmPrfxSfx | 56 = Tools > Options > Drafting Styles > Dimension > Dual Dimension > Prefix and Suffix |
| dsCommandOptionString_Undefined | 0 = Undefined |

## Remarks

The string **Lgcy** in a command option indicates that setting the command option has no effect in DraftSight; however, the value is stored in the DWG file.

In most instances, user-interface command option equivalents are the strings following **dsCommandOptionString_**; for example, typing **GetActCmd** in the command prompt is equivalent to using **dsCommandOptionString_GetActCmd** in code.

## See Also

[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IDocument::GetCommandOptionString Method](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetCommandOptionString.html)
[IDocument::SetCommandOptionString Method](Interop.dsAutomation~Interop.dsAutomation.IDocument~SetCommandOptionString.html)
