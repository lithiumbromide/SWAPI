---
title: "EdmButtonState Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmButtonState"
member: ""
kind: "enum"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmButtonState.html"
---

# EdmButtonState Enumeration

States of a toolbar button; used in calls to [IEdmAddInDrawButton5:DrawToolbarButton](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddInDrawButton5~DrawToolbarButton.html), [IEdmCmdMgr5::AddToolbarImage](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCmdMgr5~AddToolbarImage.html), and [IEdmMenu5::GetButtonImages](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmMenu5~GetButtonImages.html).

## Syntax

### Visual Basic

```vb
Public Enum EdmButtonState
   Inherits System.Enum
```

### C#

```csharp
public enum EdmButtonState : System.Enum
```

### C++/CLI

```cpp
public enum class EdmButtonState : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| BState_Cold | 2 = Normal button display |
| BState_Disabled | 3 = Button is disabled |
| BState_Hot | 1 = Mouse cursor is hovering over the toolbar button; button should be highlighted |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
