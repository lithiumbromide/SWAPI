---
title: "SldWorks::AddToolbar3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__AddToolbar3.htm"
---

# SldWorks::AddToolbar3

This method is obsolete and has been superseded by [SldWorks::AddToolbar4](sldworksAPI.chm::/SldWorks/SldWorks__AddToolbar4.htm).

Description

This method creates a Windows-style dockable toolbar, containing a set of application defined buttons.

Syntax (OLE Automation)

NewToolBarID = SldWorks.AddToolbar3 ( Cookie, Title, SmallBitmapResourceID, LargeBitmapResourceID, MenuPositionForToolbar, DocumentType )

| Input: | (long) Cookie | Resource ID of the toolbar; this is the same cookie you specified in SwAddin::ConnectToSW |
| --- | --- | --- |
| Input: | (BSTR) Title | Toolbar title |
| Input: | (long) SmallBitmapResourceID | Resource ID of the small bitmap image |
| Input: | (long) LargeBitmapResourceID | Resource ID of the large bitmap image |
| Input: | (long) MenuPositionForToolbar | Unused; SolidWorks always puts toolbar names in alphabetical order |
| Input: | (long) DocumentType | Bitwise values indicating what frame window types should have this toolbar's name added to its View, Toolbars menu; values from swDocTemplateTypes_e |
| Output: | (long) NewToolBarID | Toolbar ID for use with other methods or –1 if not created |

Syntax (COM)

status = SldWorks->AddToolbar3 ( Cookie, Title, SmallBitmapResourceID, LargeBitmapResourceID, MenuPositionForToolbar, DocumentType, &NewToolBarID )

| Input: | (long) Cookie | Resource ID of the toolbar; this is the same cookie you specified in SwAddin::ConnectToSW |
| --- | --- | --- |
| Input: | (BSTR) Title | Toolbar title |
| Input: | (long) SmallBitmapResourceID | Resource ID of the small bitmap image |
| Input: | (long) LargeBitmapResourceID | Resource ID of the large bitmap image |
| Input: | (long) MenuPositionForToolbar | Unused; SolidWorks always puts toolbar names in alphabetical order |
| Input: | (long) DocumentType | Bitwise values indicating what frame window types should have this toolbar's name added to its View, Toolbars menu; values from swDocTemplateTypes_e |
| Output: | (long) NewToolBarID | Toolbar ID for use with other methods or –1 if not created |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

For information about using this method with the SwAddin object, see Using SwAddin to Create a SolidWorks Add-in.

This method:

- Only operates properly when the application is implemented as a DLL and not as an .exe.
- Adds the toolbar name to the View, Toolbars menu.
- Only creates the toolbar and passes the image for the buttons to SolidWorks. To add functionality, use SldWorks::AddToolbarCommand2.

The bitmap images should contain the bitmaps for each of the buttons (including separators) in the toolbar as a single bitmap. For a small bitmap, the image for each button must be 16x15; for a large bitmap, it must be 22x22. The bitmaps should use a 16-bit color palette. For a transparent bitmap, the color must be the standard Windows palette gray (RGB 192, 192, 192).

NOTES:

- When your add-in is unloaded, you must call SldWorks::RemoveToolbar2 to remove this toolbar.
- If you want the toolbar to show up in specific locations only, do not use SldWorks::ShowToolbar2. If your application uses that method, your application ignores the DocumentType argument of SldWorks::AddToolbar3.

  SldWorks::ShowToolbar2 assumes that the application is controlling the visibility state of the toolbar, and not the user. This means that the toolbar will be available in all locations.
