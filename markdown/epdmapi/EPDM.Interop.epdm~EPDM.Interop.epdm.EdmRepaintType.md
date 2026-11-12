---
title: "EdmRepaintType Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmRepaintType"
member: ""
kind: "enum"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRepaintType.html"
---

# EdmRepaintType Enumeration

Types of flags passed into [IEdmImage::Reposition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmImage~Reposition.html) to control how to handle repainting of the background window.

## Syntax

### Visual Basic

```vb
Public Enum EdmRepaintType
   Inherits System.Enum
```

### C#

```csharp
public enum EdmRepaintType : System.Enum
```

### C++/CLI

```cpp
public enum class EdmRepaintType : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmRepaint_Erase | 2 = Trigger both paint and erase (WM_ERASEBKGND) message |
| EdmRepaint_Nothing | 0 = Do not refresh the window |
| EdmRepaint_Repaint | 1 = Trigger a repaint (WM_PAINT) message but not a background erase |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
