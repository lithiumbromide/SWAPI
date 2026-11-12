---
title: "PropertyManagerPageBitmapButton::SetBitmapsByName"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPageBitmapButton/PropertyManagerPageBitmapButton__SetBitmapsByName.htm"
---

# PropertyManagerPageBitmapButton::SetBitmapsByName

This method is obsolete and has been superseded by [PropertyManagerPageBitmapButton::SetBitmapsByName2](sldworksAPI.chm::/PropertyManagerPageBitmapButton/PropertyManagerPageBitmapButton__SetBitmapsByName2.htm).

Description

This method sets the bitmaps for this button.

Syntax (OLE Automation)

retval = PropertyManagerPageBitmapButton.SetBitmapsByName ( bitmapUp, bitmapDown, bitmapDisabled)

| Input: | (BSTR) bitmapUp | Path to the not pressed-in (up) state bitmap image on disk |
| --- | --- | --- |
| Input: | (BSTR) bitmapDown | Path to the pressed-in (down) state bitmap image on disk |
| Input: | (BSTR) bitmapDisabled | Path to the disabled state bitmap image on disk |
| Output: | (VARIANT_BOOL*) retval | TRUE if the bitmap states are set, FALSE if not |

Syntax (COM)

status = PropertyManagerPageBitmapButton->SetBitmapsByName ( bitmapUp, bitmapDown, bitmapDisabled, &retval)

| Input: | (BSTR) bitmapUp | Path to the not pressed-in (up) state bitmap image on disk |
| --- | --- | --- |
| Input: | (BSTR) bitmapDown | Path to the pressed-in (down) state bitmap image on disk |
| Input: | (BSTR) bitmapDisabled | Path to the disabled state bitmap image on disk |
| Output: | (VARIANT_BOOL*) retval | TRUE if the bitmap states are set, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The bitmapUp, bitmapDown, and bitmapDisabled arguments must be fully qualified paths to .bmp files on the disk. Relative paths are not valid. The SolidWorks application loads the bitmaps from these .bmp files and uses them on this bitmap button control.

You must call this method after calling either of the following APIs to create the bitmap button control:

- PropertyManagerPage2::AddControl
- PropertyManagerPageGroup::AddControl
