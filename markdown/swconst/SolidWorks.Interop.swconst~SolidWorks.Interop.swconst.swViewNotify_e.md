---
title: "swViewNotify_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swViewNotify_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swViewNotify_e.html"
---

# swViewNotify_e Enumeration

Model view notifications.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swViewNotify_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swViewNotify_e
```

### C#

```csharp
public enum swViewNotify_e : System.Enum
```

### C++/CLI

```cpp
public enum class swViewNotify_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swViewBufferSwapNotify | 5 = BufferSwapNotify |
| swViewChangeNotify | 2 = ViewChangeNotify |
| swViewDestroyNotify | Obsolete |
| swViewDestroyNotify2 | 6 = DestroyNotify2 |
| swViewDisplayModeChangePostNotify | 13 = DisplayModeChangePostNotify |
| swViewDisplayModeChangePreNotify | 12 = DisplayModeChangePreNotify |
| swViewGraphicsRenderPostNotify | 11 = GraphicsRenderPostNotify |
| swViewPerspectiveViewNotify | 7 = PerspectiveViewNotify |
| swViewPrintNotify | Obsolete |
| swViewPrintNotify2 | 14 = PrintNotify2 |
| swViewRenderLayer0Notify | 8 = RenderLayerNotify |
| swViewRepaintNotify | 1 = RepaintNotify |
| swViewRepaintPostNotify | 4 = RepaintPostNotify |
| swViewUserClearSelectionsNotify | 9 = UserClearSelectionsNotify |

## Remarks

To receive notifications, a DLL application must register for the notifications by object type. This registration must be done for each instance of a particular object.

For example, in the file in the Visual C++ 6.0 wizard-generated add-in that supports model view events (e.g., DocView.h), include:

```vb
BEGIN_SINK_MAP(CDocView)
SINK_ENTRY_EX(ID_MODELVIEW_EVENTS, DIID_DModelViewEvents, swViewDestroyNotify, DestroyNotify)
SINK_ENTRY_EX(ID_MODELVIEW_EVENTS, DIID_DModelViewEvents, swViewRepaintNotify, RepaintNotify)
END_SINK_MAP()
```

If developing a C++ application, use these enumerators to [register for notifications](sldworksapiprogguide.chm::/Overview/events.htm) for the [IModelView](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView.html) events.

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
