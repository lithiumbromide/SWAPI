---
title: "swMouseNotify_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swMouseNotify_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMouseNotify_e.html"
---

# swMouseNotify_e Enumeration

Mouse notifications.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swMouseNotify_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swMouseNotify_e
```

### C#

```csharp
public enum swMouseNotify_e : System.Enum
```

### C++/CLI

```cpp
public enum class swMouseNotify_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swMouseLBtnDblClkNotify | 9 = MouseLBtnDblClkNotify |
| swMouseLBtnDownNotify | 3 = MouseLBtnDownNotify |
| swMouseLBtnUpNotify | 4 = MouseLBtnUpNotify |
| swMouseMBtnDblClkNotify | 11 = MouseMBtnDblClkNotify |
| swMouseMBtnDownNotify | 7 = MouseMBtnDownNotify |
| swMouseMBtnUpNotify | 8 = MouseMBtnUpNotify |
| swMouseMoveNotify | 2 = MouseMoveNotify |
| swMouseNotify | 1 = MouseNotify |
| swMouseRBtnDblClkNotify | 10 = MouseRBtnDblClkNotify |
| swMouseRBtnDownNotify | 5 = MouseRBtnDownNotify |
| swMouseRBtnUpNotify | 6 = MouseRBtnUpNotify |
| swMouseSelectNotify | 12 = MouseSelectNotify |

## Remarks

To receive notifications, a DLL application must register for the notifications by object type. This registration must be done for each instance of a particular object.

For example, in the file in the Visual C++ 6.0 wizard-generated add-in that supports mouse events (e.g., Mouse.h), include:

```vb
DECLARE_REGISTRY_RESOURCEID(IDR_MOUSE)
BEGIN_SINK_MAP(CMouse)
SINK_ENTRY_EX(ID_MOUSE_EVENTS, DIID_DMouseEvents, swMouseMoveNotify, MouseMoveNotify)
SINK_ENTRY_EX(ID_MOUSE_EVENTS, DIID_DMouseEvents, swMouseSelectNotify, MouseSelectNotify)
SINK_ENTRY_EX(ID_MOUSE_EVENTS, DIID_DMouseEvents, swMouseLBtnDownNotify, MouseLBtnDownNotify)
END_SINK_MAP()
```

If developing a C++ application, use these enumerators to [register for notifications](sldworksapiprogguide.chm::/Overview/events.htm) for the [IMouse](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMouse.html) events.

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
