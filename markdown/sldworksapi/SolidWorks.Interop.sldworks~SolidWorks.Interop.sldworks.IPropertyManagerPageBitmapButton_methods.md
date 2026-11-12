---
title: "IPropertyManagerPageBitmapButton Interface Methods"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageBitmapButton_methods"
member: ""
kind: "methods"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmapButton_methods.html"
---

# IPropertyManagerPageBitmapButton Interface Methods

For a list of all members of this type, see [IPropertyManagerPageBitmapButton members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmapButton_members.html).

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | SetBitmaps | Obsolete. Superseded by IPropertyManagerPageBitmapButton::SetBitmapsx64 . This method is unsafe to use with 64-bit SOLIDWORKS, i.e. all versions since SOLIDWORKS 2016. The 32-bit integer returned may be to small to contain the 64-bit window handle/pointer, and will be truncated silently. A critical exception will occur sometime later, when the truncated handle/pointer is used. Sets the images for this button. |
| Method | SetBitmapsByName | Obsolete. Superseded by IPropertyManagerPageBitmapButton::SetBitmapsByName2 . |
| Method | SetBitmapsByName2 | Obsolete. Superseded by IPropertyManagerPageBitmapButton::SetBitmapsByName3 . |
| Method | SetBitmapsByName3 | Inserts the specified image for this button. |
| Method | SetBitmapsx64 | Sets the images for this button in 64-bit applications. |
| Method | SetStandardBitmaps | Sets the standard images for this button. |

[Top](#topBookmark)

## See Also

[IPropertyManagerPageBitmapButton Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmapButton.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
