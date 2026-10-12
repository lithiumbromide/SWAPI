---
title: "swPropMgrPageNumberBoxStyle_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swPropMgrPageNumberBoxStyle_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPropMgrPageNumberBoxStyle_e.html"
---

# swPropMgrPageNumberBoxStyle_e Enumeration

PropertyManager page number box styles. [Bitmask](sldworksapiprogguide.chm::/Overview/bitmasks.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swPropMgrPageNumberBoxStyle_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swPropMgrPageNumberBoxStyle_e
```

### C#

```csharp
public enum swPropMgrPageNumberBoxStyle_e : System.Enum
```

### C++/CLI

```cpp
public enum class swPropMgrPageNumberBoxStyle_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swPropMgrPageNumberBoxStyle_AvoidSelectionText | 4 or 0x4; The item the user selects in the attached drop-down list does not appear in the number box. Instead, the user's selection causes the add-in to get a callback via IPropertyManagerPage2Handler9::OnComboboxSelectionChanged ; the Id argument will be the number box; the add-in is expected to respond by setting the value for the number box using IPropertyManagerPageNumberbox::Value . |
| swPropMgrPageNumberBoxStyle_ComboEditBox | 1 or 0x1; Enables the attached drop-down list for the number box; user can type a value or select a value from the attached drop-down list for the number box |
| swPropMgrPageNumberBoxStyle_EditBoxReadOnly | 2 or 0x2; User can only select a value from the attached drop-down list for the number box NOTE: You can set swPropMgrPageNumberBoxStyle_EditBoxReadOnly either before or after the PropertyManager page is displayed. If set after the PropertyManager page is displayed and the number box contains editable text, then that text cannot be edited by the user |
| swPropMgrPageNumberBoxStyle_NoScrollArrows | 8 or 0x8; Do not show the up and down arrows in the number box, thus, disallowing incrementing or decrementing the value in the number box |
| swPropMgrPageNumberBoxStyle_Slider | 16 or 0x10; Slider |
| swPropMgrPageNumberBoxStyle_SuppressNotifyWhileTracking | 64 or 0x40; Suppress sending multiple notifications when a user is dragging or spinning the slider of a number box on a PropertyManager page; instead, send only one notification; see IPropertyManagerPage2Handler9::OnNumberboxChanged for details |
| swPropMgrPageNumberBoxStyle_Thumbwheel | 32 or 0x20; Thumbwheel |

## Remarks

When the user selects an item in the attached drop-down list, SOLIDWORKS attempts to use that item as a value in the number box. Thus, the items in the attached drop-down list should be numeric values and optionally include their units. The add-in then gets a callback via IPropertyManagerPage2Handler9::OnNumberboxChanged as if the user had typed a value in the number box or clicked the up-arrow or down-arrow buttons to increment or decrement the value.

If you do not want your add-in to directly use items in the attached drop-down list in the number box, but instead want it to react to the user selecting a computed or linked value in the number box, then use swPropMgrPageNumberBoxStyle_AvoidSelectionText.

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
