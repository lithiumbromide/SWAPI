---
title: "swPropMgrPageSelectionBoxStyle_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swPropMgrPageSelectionBoxStyle_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPropMgrPageSelectionBoxStyle_e.html"
---

# swPropMgrPageSelectionBoxStyle_e Enumeration

PropertyManager page selection box styles. [Bitmask](sldworksapiprogguide.chm::/Overview/bitmasks.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swPropMgrPageSelectionBoxStyle_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swPropMgrPageSelectionBoxStyle_e
```

### C#

```csharp
public enum swPropMgrPageSelectionBoxStyle_e : System.Enum
```

### C++/CLI

```cpp
public enum class swPropMgrPageSelectionBoxStyle_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swPropMgrPageSelectionBoxStyle_HScroll | 1 or 0x1; Specifies that the selection box has a scroll bar so that interactive users can scroll through the list of items |
| swPropMgrPageSelectionBoxStyle_MultipleItemSelect | 4 or 0x4; Specifies that you can select multiple items in the selection box |
| swPropMgrPageSelectionBoxStyle_UpAndDownButtons | 2 or 0x2; Specifies that selection listbox has up and down arrows so that interactive users can move items in the list up or down |
| swPropMgrPageSelectionBoxStyle_WantListboxSelectionChanged | 8 or 0x8; Specifies that you want a notification sent when a user changes the selected item in a listbox or selection listbox |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
