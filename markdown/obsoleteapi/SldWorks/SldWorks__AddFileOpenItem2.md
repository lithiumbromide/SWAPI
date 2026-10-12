---
title: "SldWorks::AddFileOpenItem2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__AddFileOpenItem2.htm"
---

# SldWorks::AddFileOpenItem2

This method is obsolete and has been superseded by [SldWorks::AddFileOpenItem3](sldworksAPI.chm::/SldWorks/SldWorks__AddFileOpenItem3.htm).

Description

This method adds a file type to the SolidWorks File Open dialog box.

Syntax (OLE Automation)

retval = SldWorks.AddFileOpenItem2 ( Cookie, MethodName, Description, Extension )

| Input: | (long) Cookie | Cookie specified in SwAddin::ConnectToSW |
| --- | --- | --- |
| Input: | (BSTR) MethodName | Name of the application function used to open the file |
| Input: | (BSTR) Description | File description displayed in the Files of Type menu |
| Input: | (BSTR) Extension | File extension |
| Output: | (VARIANT_BOOL) retval | TRUE if the item was added, FALSE if not |

Syntax (COM)

status = SldWorks->AddFileOpenItem2 ( Cookie, MethodName, Description, Extension, &retval )

| Input: | (long) Cookie | Cookie specified in SwAddin::ConnectToSW |
| --- | --- | --- |
| Input: | (BSTR) MethodName | Name of the application function used to open the file |
| Input: | (BSTR) Description | File description displayed in the Files of Type menu |
| Input: | (BSTR) Extension | File extension |
| Output: | (VARIANT_BOOL) retval | TRUE if the item was added, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If your application is unloaded using an add-in, then you must remove any file types added with this method. See SldWorks::RemoveFileOpenItem2.

#### Examples

```vb
Private Function SwAddin_ConnectToSW(ByVal ThisSW As Object, ByVal Cookie As Long) As Boolean
    ...
    bWasAdded = pSldWorks.AddFileSaveAsItem2(swCookie, "Test_Callback", "Save As file type", "xyz", 1)

    bWasAdded = pSldWorks.AddFileOpenItem2(swCookie, "Test_Callback", "Open File type", "xyz")
    ...
End Function
Private Function SwAddin_DisconnectFromSW() As Boolean
    ...

    bWasItemRemoved = pSldWorks.RemoveFileSaveAsItem2(swCookie, "Test_Callback", "Save As file type", "xyz", 1)
    bWasItemRemoved = pSldWorks.RemoveFileOpenItem2(swCookie, "Test_Callback", "Open File type", "xyz")
    ...
End Function

Public Sub Test_CallBack(Filename As String)
    pSldWorks.SendMsgToUser "Callback called with filename = " & Filename End Sub
```
