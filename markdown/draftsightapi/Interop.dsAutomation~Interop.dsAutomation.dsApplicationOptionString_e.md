---
title: "dsApplicationOptionString_e Enumeration"
project: ""
interface: "dsApplicationOptionString_e"
member: ""
kind: "enum"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.dsApplicationOptionString_e.html"
---

# dsApplicationOptionString_e Enumeration

Application options for strings.

## Syntax

### Visual Basic

```vb
Public Enum dsApplicationOptionString_e
   Inherits System.Enum
```

### C#

```csharp
public enum dsApplicationOptionString_e : System.Enum
```

### JScript

```
public enum dsApplicationOptionString_e extends System.Enum
```

### Managed Extensions for C++

```
__value public enum dsApplicationOptionString_e : public System.Enum
```

### C++/CLI

```cpp
public enum class dsApplicationOptionString_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| dsApplicationOptionString_Count | Not used |
| dsApplicationOptionString_GetActDict | 1 = Path and file name of current custom dictionary |
| dsApplicationOptionString_GetActUsr | 2 = Name of active Windows user (read only) |
| dsApplicationOptionString_GetInfOS | 3 = Code for current locale (read only) |
| dsApplicationOptionString_GetLstSvNm | 4 = Path and file name of most recently saved drawing (read only) |
| dsApplicationOptionString_GetNmActPrfl | 5 = Current profile name (read only) |
| dsApplicationOptionString_GetNmAutoSvFl | 6 = Current automatic save file name (read only) |
| dsApplicationOptionString_GetNmPrdct | 7 = Product name (read only) |
| dsApplicationOptionString_GetNmPrgm | 8 = Program name (read only) |
| dsApplicationOptionString_GetPlatform | 9 = Operating system and platform in use (read only) |
| dsApplicationOptionString_GetPthDS | 10 = Paths specified by environment variable, if it exists (read only) |
| dsApplicationOptionString_GetPthDWG | 11 = Drive and folder of active drawing (read only) |
| dsApplicationOptionString_Lgcy_PKSER | 12 = Product identification number (read only and see Remarks ) |
| dsApplicationOptionString_LgcySHPNAME | 13 = Default shape name (see Remarks ) |
| dsApplicationOptionString_SetActMnu | 14 = Tools > Options > File Locations > Interface > Customization File |
| dsApplicationOptionString_SetAltBgFnt | 26 = Tools > Options > File Locations > Drawing Support > Alternate Font File > Big font |
| dsApplicationOptionString_SetAltFnt | 15 = Tools > Options > File Locations > Drawing Support > Alternate Font File > SHX font |
| dsApplicationOptionString_SetAltShp | 25 = Tools > Options > File Locations > Drawing Support > Alternate Font File > Shape file |
| dsApplicationOptionString_SetAutoSvPth | 16 = Tools > Options > System Options > Auto-Save & Backup > Automatic save file location |
| dsApplicationOptionString_SetBrwsrUrl | 17 = Default web site for OpenWebPage |
| dsApplicationOptionString_SetDictFNm | 18 = Displays the file name of the current main spelling dictionary; the full path is not shown because this file is expected to reside in the Support directory |
| dsApplicationOptionString_SetFntMpFNm | 19 = Tools > Options > File Locations > Drawing Support > Font Mapping File |
| dsApplicationOptionString_SetLogPth | 20 = Tools > Options > File Locations > System > Log File Location |
| dsApplicationOptionString_SetPGdSpcAng | 21 = Tools > Options > User Preferences > Drafting Options > Display > Polar Guides > Incremental angles for Polar guide display |
| dsApplicationOptionString_SetPrmptTxt | 22 = Tools > Options > System Options > Display > Command window text > Command line text |
| dsApplicationOptionString_SetPSProLog | 23 = PostScript prolog section name |
| dsApplicationOptionString_SetPthTemp | 24 = Tools > Options > File Locations > System > Temporary File Location (read only) |
| dsApplicationOptionString_SetWSCURRENT | 27 = Current workspace |
| dsApplicationOptionString_Undefined | 0 = Undefined |

## Remarks

The string **Lgcy** in a command option indicates that setting the command option has no effect in DraftSight; however, the value is stored in the DWG file.

In most instances, user-interface command option equivalents are the strings following **dsCommandOptionString_**; for example, typing **SetPthTemp** in the command prompt is equivalent to using **dsCommandOptionString_SetPthTemp** in code.

## See Also

[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
