---
title: "SldWorks::AddFileOpenItem"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__AddFileOpenItem.htm"
---

# SldWorks::AddFileOpenItem

This method is obsolete and has been superceded by [SldWorks::AddFileOpenItem2](SldWorks__AddFileOpenItem2.htm).

Description

This maethod adds a file type to the SolidWorks File Open dialog. When a file of the type specified is selected in the dialog, then the application function specified is called to load the file.

NOTE: If your application is unloaded using the Add-In manager, then any file types added this way must be removed. See SldWorks::RemoveFileOpenItem.

Syntax (OLE Automation)

retval = SldWorks.AddFileOpenItem ( CallbackFcnAndModule, Description)

| Input: | (BSTR) CallbackFcnAndModule | Name of application module and function used to open the file |
| --- | --- | --- |
| Input: | (BSTR) Description | File extension and description |
| Return: | (BOOL) retval | TRUE if successfully added, FALSE otherwise |

Syntax (COM)

status = SldWorks->AddFileOpenItem ( CallbackFcnAndModule, Description, &retval )

| Input: | (BSTR) CallbackFcnAndModule | Name of module and function used to open the file |
| --- | --- | --- |
| Input: | (BSTR) Description | File extension and description |
| Output: | (VARIANT_BOOL) retval | TRUE if successfully added, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

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
