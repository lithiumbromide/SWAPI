---
title: "ISWPropertySheet Interface Methods"
project: "SOLIDWORKS API Help"
interface: "ISWPropertySheet_methods"
member: ""
kind: "methods"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISWPropertySheet_methods.html"
---

# ISWPropertySheet Interface Methods

For a list of all members of this type, see [ISWPropertySheet members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISWPropertySheet_members.html).

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AddActivePage | Adds a third-party CPropertyPage to ISWPropertySheet and adds an ActiveX control on top of the page. |
| Method | AddPage | Obsolete. Superseded by ISWPropertySheet::AddPagex64 . This method is unsafe to use with 64-bit SOLIDWORKS, i.e. all versions since SOLIDWORKS 2016. The 32-bit integer returned may be to small to contain the 64-bit window handle/pointer, and will be truncated silently. A critical exception will occur sometime later, when the truncated handle/pointer is used. Adds a CPropertyPage-derived page to an ISWPropertySheet . |
| Method | AddPagex64 | Adds a CPropertyPage-derived page to an ISWPropertySheet in 64-bit applications. |
| Method | GetControl | Gets the ActiveX control on the property sheet. |
| Method | RemovePage | Removes a CPropertyPage derived page from an ISWPropertySheet . |

[Top](#topBookmark)

## See Also

[ISWPropertySheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISWPropertySheet.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
