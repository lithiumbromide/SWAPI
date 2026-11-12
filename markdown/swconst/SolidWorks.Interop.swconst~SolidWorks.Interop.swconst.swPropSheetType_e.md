---
title: "swPropSheetType_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swPropSheetType_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPropSheetType_e.html"
---

# swPropSheetType_e Enumeration

Property sheet types.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swPropSheetType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swPropSheetType_e
```

### C#

```csharp
public enum swPropSheetType_e : System.Enum
```

### C++/CLI

```cpp
public enum class swPropSheetType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swPropSheetAmbientLight | 3 = Property sheet ambient light |
| swPropSheetDirectionalLight | 4 = Property sheet directional light |
| swPropSheetLighting | 1 = Property sheet lighting |
| swPropSheetNotValid | 0 = Invalid property sheet |
| swPropSheetPositionLight | 5 = Property sheet position light |
| swPropSheetSpotLight | 6 = Property sheet spot light |
| swPropSheetToolsOptions | 2 = Property sheet tools options |

## Remarks

This enumerator specifies possible values for the types of [ISWPropertySheet](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISWPropertySheet.html)s exported by SOLIDWORKS when a SldWorks notification of type [swAppPropertySheetCreateNotify](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAppNotify_e.html) is sent.

An example of a property sheet is the dialog that is displayed when you click Tools, Options. This dialog consists of a base property sheet and property pages stacked on top of it. To display a specific property page, click its tab.

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
