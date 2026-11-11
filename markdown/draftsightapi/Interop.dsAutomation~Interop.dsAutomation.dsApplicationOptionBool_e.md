---
title: "dsApplicationOptionBool_e Enumeration"
project: ""
interface: "dsApplicationOptionBool_e"
member: ""
kind: "enum"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.dsApplicationOptionBool_e.html"
---

# dsApplicationOptionBool_e Enumeration

Application options with Boolean values.

## Syntax

### Visual Basic

```vb
Public Enum dsApplicationOptionBool_e
   Inherits System.Enum
```

### C#

```csharp
public enum dsApplicationOptionBool_e : System.Enum
```

### JScript

```
public enum dsApplicationOptionBool_e extends System.Enum
```

### Managed Extensions for C++

```
__value public enum dsApplicationOptionBool_e : public System.Enum
```

### C++/CLI

```cpp
public enum class dsApplicationOptionBool_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| dsApplicationOptionBool_Count | 12 = Not used |
| dsApplicationOptionBool_EnblBAttDlgs | 1 = Sets whether attribute values are typed in a dialog or at the command prompt: False = Command prompt True = Dialog |
| dsApplicationOptionBool_EnblBAttVrfy | 2 = Sets whether to use default attribute values when inserting Blocks or to prompt the user for values: False = Defaults True = Command prompt or dialog |
| dsApplicationOptionBool_EnblBMPPrvw | 3 = Sets whether to save BMP preview images with the drawing: False = No True = Yes |
| dsApplicationOptionBool_EnblEntSelPreSel | 4 = Tools > Options > User Preferences > Drafting Options > Entity Selection > Selection Settings > Enable entity selection before commands: False = Select entities after issuing commands True = Select entities before issuing commands |
| dsApplicationOptionBool_EnblGBox | 5 = Tools > Options > User Preferences > Drafting Options > Display > Gravity Box > Enable ESnap gravity: False = Off True = On |
| dsApplicationOptionBool_EnblImgHlt | 6 = Sets whether to highlight the raster image or only its frame: False = Highlight only raster image frame True = Highlight raster image |
| dsApplicationOptionBool_EnblNavDlgs | 7 = Suppresses file navigation dialogs: False = Do not display dialogs True = Display dialogs |
| dsApplicationOptionBool_EnblPrxyWrng | 8 = Sets whether to display a notice when a proxy is created: False = No notice True = Notice |
| dsApplicationOptionBool_EnblRgnBndryDel | 9 = Sets whether geometry used to create 3D entities is deleted: False = Geometry not deleted True = Deletes geometry or displays a prompt to delete geometry |
| dsApplicationOptionBool_EnblRstrOleDsp | 10 = Sets whether to display both raster images and OLE content or display outlines when zooming and panning: False = Only display outlines True = Display raster images and OLE content |
| dsApplicationOptionBool_SetTxtPrnFill | 11 = Sets filling of TrueType fonts while printing: False = Off True = On |
| dsApplicationOptionBool_Undefined | 0 = Undefined |

## See Also

[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
