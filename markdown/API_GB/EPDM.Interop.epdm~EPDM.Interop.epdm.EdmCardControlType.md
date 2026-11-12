---
title: "EdmCardControlType Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmCardControlType"
member: ""
kind: "enum"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCardControlType.html"
---

# EdmCardControlType Enumeration

File or folder data card control types; used in calls to [IEdmCardControl5::ControlType](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCardControl5~ControlType.html).

## Syntax

### Visual Basic

```vb
Public Enum EdmCardControlType
   Inherits System.Enum
```

### C#

```csharp
public enum EdmCardControlType : System.Enum
```

### C++/CLI

```cpp
public enum class EdmCardControlType : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmCtrl_Button | 5 = Push button |
| EdmCtrl_Checkbox | 13 = Check box |
| EdmCtrl_ComboboxDropdown | 8 = Combo box with a drop-down list and an edit box |
| EdmCtrl_ComboboxDroplist | 9 = Combo box with a drop-down list |
| EdmCtrl_ComboboxSimple | 7 = Combo box with a list that is always visible |
| EdmCtrl_CustomPropertySearch | 15 = Search tool control |
| EdmCtrl_CustomVariableTree | 16 = Search tool control |
| EdmCtrl_DatePicker | 14 = Date control |
| EdmCtrl_Editbox | 4 = Edit box |
| EdmCtrl_Frame | 3 = Static frame with optional text |
| EdmCtrl_Image | 1 = Static image |
| EdmCtrl_Invalid | 0 = Error |
| EdmCtrl_Listbox | 10 = List box |
| EdmCtrl_RadioColumn | 6 = Radio button |
| EdmCtrl_Tab | 11 = Tab control with one or more pages |
| EdmCtrl_Text | 2 = Static text |
| EdmCtrl_Viewer | DO NOT USE |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
