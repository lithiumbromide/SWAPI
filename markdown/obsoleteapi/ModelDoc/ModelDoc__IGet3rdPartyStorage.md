---
title: "ModelDoc::IGet3rdPartyStorage"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__IGet3rdPartyStorage.htm"
---

# ModelDoc::IGet3rdPartyStorage

This method is obsolete and has been superseded by [ModelDoc2::IGet3rdPartyStorage](sldworksAPI.chm::/ModelDoc2/ModelDoc2__IGet3rdPartyStorage.htm).

Description

This method gets an IStream interface for storage inside the SolidWorks document.

Syntax (OLE Automation)

Not Available.

Syntax (COM)

status = ModelDoc->IGet3rdPartyStorage ( stringIn, isStoring, &retval )

| Input: | (BSTR) stringIn | Name for the storage stream; the name should be less than 30 characters and must be unique and qualified among all parties choosing to store within the current session |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) isStoring | TRUE if you are storing data, FALSE if you are reading data |
| Output: | (LPUNKNOWN) retval | Pointer to an unknown type, the IStream storage |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Call this interface when a SaveToStorageNotify or LoadFromStorageNotify notification is received. Do not call this method to save or load from storage in reaction to the FileSaveNotify or FileOpenNotify events.

During a File, Open operation, your application receives a LoadFromStorageNotify event if you have registered for document notifications. After you receive this event, it is safe to open your Stream for reading using this method. After a file is fully loaded, SolidWorks allows you to call this method for reading your data at any time. This provides you with access to read your storage node whenever needed. However, it is not a good idea to attempt this while SolidWorks is in the middle of a FileSaveNotify or FileOpenNotify as unforeseen conflicts may occur.

If your application is loaded in the middle of a SolidWorks session, then you can traverse all open documents using SldWorks::EnumDocuments or SldWorks::GetFirstDocument or SldWorks::GetNext and read the storage from all existing open documents. From that point on, your application can use the LoadFromStorageNotify event to recognize when new documents have been opened and may need reading.

For storage writing, the IGet3rdPartyStorage interface is locked unless the SaveToStorageNotify event has been sent. Therefore, you can only write to your storage when the file is actually being saved by SolidWorks and your application has received the SaveToStorageNotify event.

A call to IGet3rdPartyStorage must be followed by a call to ModelDoc::IRelease3rdPartyStorage. This must be done even when you fail to obtain a Stream and the return value from ModelDoc::IGet3rdPartyStorage is NULL. If you fail to call ModelDoc::IRelease3rdPartyStorage, the 3rdParty node may remain locked and prevent future access. You are not required to call ModelDoc::IRelease3rdPartyStorage, under any circumstance, if you have called ModelDoc::IGet3rdPartyStorage in reaction to one of the SaveToStorageNotify or LoadFromStorageNotify events. However, it will not cause problems if you call ModelDoc::IRelease3rdPartyStorage excessively.

As work progresses during an active session and you have information that needs to be stored, you may want to flag the document as dirty using ModelDoc::SetSaveFlag. This will cause a Save Changes? prompt to appear if the user tries to close the file without saving. If the user chooses Yes to this prompt, then your application will receive the SaveToStorageNotify event.

NOTE: The name to give to the storage stream should be registered with SolidWorks so that no conflicts occur. Once registered, SolidWorks reserves the stream name exclusively for your application.

Passing the unique name string and a flag to determine if data is being stored or being loaded returns an IUnknown pointer. You must then use QueryInterface() to get the IStream interface. The stream is to be used for serialization and then released in the third-party code.

SwRootStorage --|

|

|-- ThirdPty --|

|

|-- <SW Assigned IStream name 1>

|-- <SW Assigned IStream name 2>

|-- <SW Assigned IStream name 3>

: : :

|-- <SW Assigned IStream name n>

The IStream object used by the third party is written to IStream objects under an IStorage object called ThirdPty in the SolidWorks compound document. Each third party writes to a single IStream object whose name is assigned by SolidWorks.

NOTE If you are using serialization, then you should be careful with the standard MFC macros; otherwise, you may get messages like Unexpected File Format after your application is unloaded.

One way of using IMPLEMENT_SERIAL is:

IMPLEMENT_SERIAL( CCustomAttr, CObject, VERSIONABLE_SCHEMA|0 )
