---
title: "IFeatMgrView Interface Members"
project: "SOLIDWORKS API Help"
interface: "IFeatMgrView_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView_members.html"
---

# IFeatMgrView Interface Members

The following tables list the members exposed by [IFeatMgrView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView.html).

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | ActivateView | Activates this view in the FeatureManager design tree. |
| Method | DeActivateView | Deactivates this view in the FeatureManager design tree. |
| Method | DeleteView | Removes this view from the FeatureManager design tree. |
| Method | GetControl | Gets the control associated with this FeatureManager design tree view. |
| Method | GetFeatMgrViewWnd | Obsolete. Superseded by IFeatMgrView::GetFeatMgrViewWndx64 . This method is unsafe to use with 64-bit SOLIDWORKS, i.e. all versions since SOLIDWORKS 2016. The 32-bit integer returned may be to small to contain the 64-bit window handle/pointer, and will be truncated silently. A critical exception will occur sometime later, when the truncated handle/pointer is used. Gets the FeatureManager design tree view window handle as a CWnd object. |
| Method | GetFeatMgrViewWndx64 | Gets the FeatureManager design tree view window handle as a CWnd object in 64-bit applications. |
| Method | IGetControl | Gets the control associated with this FeatureManager design tree view. |

[Top](#topBookmark)

## See Also

[IFeatMgrView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
