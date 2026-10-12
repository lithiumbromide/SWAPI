---
title: "IPropertyManagerPageWindowFromHandle Interface Members"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageWindowFromHandle_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageWindowFromHandle_members.html"
---

# IPropertyManagerPageWindowFromHandle Interface Members

The following tables list the members exposed by [IPropertyManagerPageWindowFromHandle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageWindowFromHandle.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | Height | Gets or sets the height of this .NET control. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | SetWindowHandle | Obsolete. Superseded by IPropertyManagerPageWindowFromHandle::SetWindowHandlex64 . This method is unsafe to use with 64-bit SOLIDWORKS, i.e. all versions since SOLIDWORKS 2016. The 32-bit integer returned may be to small to contain the 64-bit window handle/pointer, and will be truncated silently. A critical exception will occur sometime later, when the truncated handle/pointer is used. Sets the handle of this .NET control. |
| Method | SetWindowHandlex64 | Sets the handle of this .NET control on 64-bit machines. |

[Top](#topBookmark)

## See Also

[IPropertyManagerPageWindowFromHandle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageWindowFromHandle.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
