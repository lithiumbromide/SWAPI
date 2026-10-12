---
title: "SldWorks::AddToolbar"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__AddToolbar.htm"
---

# SldWorks::AddToolbar

This method is obsolete and has been superseded by [SldWorks::AddToolbar2](SldWorks__AddToolbar2.htm).

Description

This method creates a Windows style, dockable toolbar, containing a set of application defined buttons.

Syntax (OLE Automation)

retval = SldWorks.AddToolbar ( moduleName, title, smallBitmapHandle, largeBitmapHandle )

| Input: | (BSTR) moduleName | Name of the module (for example, USERDLL) |
| --- | --- | --- |
| Input: | (BSTR) title | Name of the toolbar |
| Input: | (long) smallBitmapHandle | Handle of the small bitmap image |
| Input: | (long) largeBitmapHandle | Handle of the large bitmap image |
| Return: | (long) retval | The toolbar ID for use with other methods or -1 if not created |

Syntax (COM)

status = SldWorks->AddToolbar ( moduleName, title, smallBitmapHandle, largeBitmapHandle, &retval )

| Input: | (BSTR)moduleName | Name of the module (for example, USERDLL) |
| --- | --- | --- |
| Input: | (BSTR) title | Name of the toolbar |
| Input: | (long)smallBitmapHandle | Handle of the small bitmap image |
| Input: | (long)largeBitmapHandle | Handle of the large bitmap image |
| Output: | (long)retval | The toolbar ID for use with other methods or -1 if not created |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

This method creates the ToolBar and passes the image for the buttons to SolidWorks. To add functionality you must call SldWorks::AddToolbarCommand.

The bitmap images should contain the bitmaps for each of the buttons (including separators) in the Toolbar as a single bitmap. For the small bitmap the image for each button must be 16x15, for the large bitmap it must be 22x22.

One way of creating the bitmaps is to add a Toolbar resource to your Visual C++ project and then load the bitmap for that Toolbar into a Cbitmap object, for example:

Example ToolBar resource in Visual C++

```vb
 m_SmallToolbar.LoadMappedBitmap(IDR_TOOLBAR_SMALL);
 HBITMAP hbmSmallImageWell = (HBITMAP)m_SmallToolbar.GetSafeHandle();
```

If you load your Toolbar image into a locally declared CBitmap object in a function, then as the function returns and the local CBitmap is destroyed, the handle passed to SolidWorks becomes invalid and, at best, the buttons are blank.

NOTE: When your Add-In is unloaded, you must call SldWorks::RemoveToolbar to remove this toolbar.
