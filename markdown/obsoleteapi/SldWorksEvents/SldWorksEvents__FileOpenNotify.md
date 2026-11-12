---
title: "FileOpenNotify - SldWorks Event"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorksEvents/SldWorksEvents__FileOpenNotify.htm"
---

# FileOpenNotify - SldWorks Event

This event is obsolete and has been superseded by SldWorks event [FileOpenNotify2](sldworksAPI.chm::/SldWorksEvents/SldWorksEvents__FileOpenNotify2.htm).

Description

Post-notifies the user program when an existing file has been opened. SldWorks::GetOpenDocumentByName can then be used with FileName to get a pointer to the newly opened document.

status = FileOpenNotify ( FileName )

| Input: | (BSTR) FileName | Name of the opened file |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This event is not sent to any application when a file is opened programmatically using any SldWorks::OpenDoc* method. Your application can detect the newly opened document by watching the ActiveModelDocChangeNotify event.

SldWorks::OpenDoc2 and SldWorks::OpenDoc3 do send this event; however, to detect newly opened documents that are opened from within some other application that still uses an SldWorks::OpenDoc* method, you should still watch for the ActiveModelDocChangeNotify event. This event is not sent when the user opens a file in view-only mode. However, an ActiveModelDocChangeNotify event is sent.

With the exception of Parasolid files (that is, *.x_t, *.x_b), this event is not sent for the opening of non-native SolidWorks files (that is, *.igs, *.dxf, and so on). Non-native file open are typically handled with the creation of a new SolidWorks file (that is, *.sldprt, *.sldasm, *.slddrw) and the subsequent construction of the foreign geometry within that file.
