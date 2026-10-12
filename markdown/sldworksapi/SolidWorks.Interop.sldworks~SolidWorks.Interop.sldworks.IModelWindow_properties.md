---
title: "IModelWindow Interface Properties"
project: "SOLIDWORKS API Help"
interface: "IModelWindow_properties"
member: ""
kind: "properties"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelWindow_properties.html"
---

# IModelWindow Interface Properties

For a list of all members of this type, see [IModelWindow members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelWindow_members.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | HWnd | Obsolete. Superseded by IModelWindow::HWndx64 . This method is unsafe to use with 64-bit SOLIDWORKS, i.e. all versions since SOLIDWORKS 2016. The 32-bit integer returned may be to small to contain the 64-bit window handle/pointer, and will be truncated silently. A critical exception will occur sometime later, when the truncated handle/pointer is used. Gets the handle to this model window. |
| Property | HWndx64 | Gets the handle to this model window in 64-bit applications. |
| Property | ModelDoc | Gets the model document in this model window. |
| Property | Title | Gets the title of this model window. |

[Top](#topBookmark)

## See Also

[IModelWindow Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelWindow.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IFrame::ShowModelWindow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~ShowModelWindow.html)
[IFrame::GetModelWindowCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetModelWindowCount.html)
