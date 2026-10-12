---
title: "SldWorks::AddFileSaveAsItem"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__AddFileSaveAsItem.htm"
---

# SldWorks::AddFileSaveAsItem

This method is obsolete and has been superseded by [SldWorks::AddFileSaveAsItem2](sldworksAPI.chm::/SldWorks/SldWorks__AddFileSaveAsItem2.htm).

Description

This method adds a file type to the SolidWorks Save As dialog window. When a file of the type specified is selected in the dialog, then the application function specified is called to save the file. The file type will only be added.

NOTE: If your application is unloaded using the Add-In manager, then any file types added this way must be removed, see SldWorks::RemoveFileSaveAsItem.

Syntax (OLE Automation)

retval = SldWorks.AddFileSaveAsItem ( CallbackFcnAndModule, Description, Type)

| Input: | (BSTR) CallbackFcnAndModule | Name of application module and function used to save the file |
| --- | --- | --- |
| Input: | (BSTR) Description | File Extension and description |
| Input: | (long) Type | Type of document to save as defined in swDocumentTypes_e |
| Return: | (BOOL) retval | TRUE if successfully added to the menu, FALSE otherwise |

Syntax (COM)

status = SldWorks->AddFileSaveAsItem ( CallbackFcnAndModule, Description, Type, &retval )

| Input: | (BSTR) CallbackFcnAndModule | Name of application module and function used to save the file |
| --- | --- | --- |
| Input: | (BSTR) Description | File Extension and description |
| Input: | (long) Type | Type of document to save as defined in swDocumentTypes_e |
| Output: | (VARIANT_BOOL) retval | TRUE if successfully added, FALSE otherwise |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The Description argument specifies the filename extension and a description that is added to the Files of Type menu in the File Open dialog. The syntax is:

"<file extension>\n<description>"

where:

file extension is the extension for the required files.

description is the text that the user sees in the Files of Type menu.

For example, if you have a routine that loads bitmap files, your description might be:

"BMP\nBitmap File (*.bmp)"

NOTE: \n must separate these two fields.

The CallbackFcnAndModule argument specifies the application module and function that is called when a file is to be loaded. The syntax is as follows:

```vb
"dllname@function"
```

where function is the name of the function that gets called when the end-user chooses a file of the type specified. This function must also be declared as an export in your .def file.

The application function specified is called when a file of the specified type is selected by the end-user. Two arguments are passed to your callback function in Unicode format, for example:

```vb
#define DllExport __declspec( dllexport )
void DllExport MyOpenFile(LPTSTR FileName, LPSLDWORKS pSolidWorks)
{
 // Code to load the file
 }
```

The format of the FileName argument is:

"<FullPath > <FileName> <AccessType>"

where:

- FullPath is the file name with full path information,
- FileName is the file name and extension (without separator)
- AccessType is w or r
