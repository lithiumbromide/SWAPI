---
title: "SldWorks::AddToolbar2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__AddToolbar2.htm"
---

# SldWorks::AddToolbar2

This method is obsolete and has been superseded by [SldWorks::AddToolbar3](SldWorks__AddToolbar3.htm).

Description

This method creates a Windows-style, dockable toolbar, containing a set of application-defined buttons. The toolbar name is entered into the View, Toolbars menu and the shortcut menu of the frame when the toolbar is added.

Syntax (OLE Automation)

retval = SldWorks.AddToolbar ( moduleName, title, smallBitmapHandle, largeBitmapHandle, menuPosition, docTemplateType )

| Input: | (BSTR) moduleName | Name of the module (for example, USERDLL) |
| --- | --- | --- |
| Input: | (BSTR) title | Name of the toolbar |
| Input: | (long) smallBitmapHandle | Handle of the small bitmap image |
| Input: | (long) largeBitmapHandle | Handle of the large bitmap image |
| Input: | (long) menuPosition | Unused; SolidWorks always puts toolbar names in alphabetical order |
| Input: | (long) docTemplateType | Bitwise values indicating what frame window types should have this toolbar name added to its View, Toolbars menu; values defined by swDocTemplateTypes_e |
| Return: | (long) retval | The toolbar ID for use with other methods or –1 if not created |

Syntax (COM)

status = SldWorks->AddToolbar2 ( moduleName, title, smallBitmapHandle, largeBitmapHandle, menuPosition, docTemplateType, &retval )

| Input: | (BSTR) moduleName | Name of the module (for example, USERDLL) |
| --- | --- | --- |
| Input: | (BSTR) title | Name of the toolbar |
| Input: | (long) smallBitmapHandle | Handle of the small bitmap image |
| Input: | (long) largeBitmapHandle | Handle of the large bitmap image |
| Input: | (long) menuPosition | Unused; SolidWorks always puts toolbar names in alphabetical order |
| Input: | (long) docTemplateType | Bitwise values indicating what frame window types should have this toolbar name added to its View, Toolbars menu; values defined by swDocTemplateTypes_e |
| Output: | (long) retval | Toolbar ID for use with other methods or –1 if not created |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method creates the toolbar and passes the image for the buttons to SolidWorks. To add functionality, use SldWorks::AddToolbarCommand.

The bitmap images should contain the bitmaps for each of the buttons (including separators) in the toolbar as a single bitmap. For the small bitmap the image for each button must be 16x15, for the large bitmap it must be 22x22.

One way of creating the bitmaps is to add a toolbar resource to your Visual C++ project and then load the bitmap for that toolbar into a CBitmap object

Example toolbar resource in Visual C++

```vb
SetResources();  // Local function to make sure we are using the Add-In resources
m_SmallToolbar.LoadMappedBitmap(IDR_TOOLBAR_SMALL);
HBITMAP hbmSmallImageWell = (HBITMAP)m_SmallToolbar.GetSafeHandle();
ResetResources();  // Local function to reset resources to SolidWorks
```

NOTES:

- If you load your toolbar image into a locally declared CBitmap object in a function, then as the function returns and the local CBitmap is destroyed, the handle passed to SolidWorks becomes invalid and, at best, the buttons are blank.
- When using resources specific to an add-in, it is necessary to allocate separate resource space to avoid resource clashes.
- When your add-in is unloaded, you must call SldWorks::RemoveToolbar to remove this toolbar.
