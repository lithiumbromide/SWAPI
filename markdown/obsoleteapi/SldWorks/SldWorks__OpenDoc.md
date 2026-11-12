---
title: "SldWorks::OpenDoc"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__OpenDoc.htm"
---

# SldWorks::OpenDoc

This method is obsolete and has been superseded by [SldWorks::OpenDoc2](SldWorks__OpenDoc3.htm).

Description

This method opens an existing document of Name and Type and returns a pointer to the document object.

Syntax (OLE Automation)

retval = SldWorks.OpenDoc ( Name, Type)

| Input: | (BSTR) Name | Name of document or full path, if not current directory |
| --- | --- | --- |
| Input: | (long) Type | Type of document as defined in swDocumentTypes_e |
| Return: | (LPDISPATCH) retval | Pointer to dispatch object, the document or NULL if the operation fails |

Syntax (COM)

status = SldWorks->IOpenDoc ( Name, Type, &retval )

| Input: | (BSTR) Name | Name of document or full path, if not current directory |
| --- | --- | --- |
| Input: | (long) Type | Type of document as defined in swDocumentTypes_e |
| Output: | (LPMODELDOC) retval | Pointer to the document or NULL if the operation fails |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method doesnot cause a SldWorksEvents::FileOpenNotify event to be sent. However, SldWorksEvents::ActiveDocChangeNotify and SldWorksEvents::ActiveModelDocChangeNotify events are sent if the file being loaded is not already open as the active document.

NOTE: Calling an OpenDoc method does not change the current working directory to that of the opened file, whereas, interactively using the File Open dialog box does. This can affect documents with references.

When opening a parent document (assembly, drawing, and so on) SolidWorks also opens any additional documents that are referenced in the parent document (parts, subassemblies, and so on).

When opening these parent files, SolidWorks follows certain rules in trying to locate its referenced documents. If search folders have not been set using Tools, Options, System Options, External References, then the first place searched for the referenced documents is in the current working directory. If the referenced file are found in the current working directory, then it is loaded from that directory.

Interactively performing File, Open immediately sets the current working directory to that of the document being opened. However, the OpenDoc method does not set the current working directory. Because the end-user may have interactively opened files from some random directory, you cannot be certain that the current working directory is pointing to the desired location. This can affect the referenced documents that get loaded when using any of the OpenDoc method versus performing File, Open interactively. Because of this, you may want to set the current working directory before calling any of the OpenDoc methods. This can be done using the SldWorks::SetCurrentWorkingDirectory method. To imitate the File Open dialog, set the current working directory to that of the file being opened.

When opening files that contain references, consider the current search folder settings because they can affect the references that get loaded. This can be done programmatically using the SldWorks::GetSearchFolders and SldWorks::SetSearchFolders methods. If search folders are currently in use, references are searched for in the search folders before trying to locate references in the current working directory.

The OpenDoc methods do not activate and display the document if the file is already open in memory in an assembly or drawing. However, OpenDoc should return a valid ModelDoc2 pointer that is usable with methods that do not require a document to be displayed. SldWorks::ActivateDoc activates and displays the document. Because calling OpenDoc does not activate or display the file, calling the SldWorks::ActiveDoc property does not return a pointer to this document.

To open a library feature part, use swDocPART for the Type argument.

To open foreign files (IGES, STEP, and so on) use SldWorks::LoadFile2.
