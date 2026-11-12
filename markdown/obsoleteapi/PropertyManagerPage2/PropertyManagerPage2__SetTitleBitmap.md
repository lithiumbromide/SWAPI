---
title: "PropertyManagerPage2::SetTitleBitmap"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2/PropertyManagerPage2__SetTitleBitmap.htm"
---

# PropertyManagerPage2::SetTitleBitmap

This method is obsolete and has been superseded by [PropertyManagerPage2::SetTitleBitmap2](sldworksAPI.chm::/PropertyManagerPage2/PropertyManagerPage2__SetTitleBitmap2.htm).

Description

This method sets the bitmap in the title bar of this PropertyManager.

Syntax (OLE Automation)

retval = PropertyManagerPage2.SetTitleBitmap ( ModuleHandle, Identifier )

| Input: | (long) ModuleHandle | Module handle of the application instance that contains the bitmap resource |
| --- | --- | --- |
| Input: | (long) Identifier | Resource ID of the bitmap |
| Output: | (VARIANT_BOOL) retval | TRUE if successful, FALSE if not |

Syntax (COM)

status = PropertyManagerPage2->SetTitleBitmap ( ModuleHandle, Identifier, &retval )

| Input: | (long) ModuleHandle | Module handle of the application instance that contains the bitmap resource |
| --- | --- | --- |
| Input: | (long) Identifier | Resource ID of the bitmap |
| Output: | (VARIANT_BOOL) retval | TRUE if successful, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

You can only use this method to set properties on the PropertyManager page before it is displayed or while it is closed. See PropertyManagerPage2::Show and PropertyManagerPage2::Close for details.

Create the bitmap in the resources of your application. The bitmap must have less than 256 colors. It is accessed via the ModuleHandle and Identifier that is passed into this API. The recommended size for bitmaps is a square from 18- to 22-cells wide. However, the bitmap can be any size, as long as it fits on the title bar.

The bitmap appears transparent by mapping any white (RGB(255,255,255)) cells to the current Property Manager page title bar background color. Remember the special use of this color as you design your bitmap.

| If this method is... | Then the title bar contains... |
| --- | --- |
| Used | Specified bitmap starting at the left edge of the PropertyManager title bar, followed by the title bar text (see SldWorks::CreatePropertyManagerPage). |
| Not used | Only the text, centered on the title bar. |
