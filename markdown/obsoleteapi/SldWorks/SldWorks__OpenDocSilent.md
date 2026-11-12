---
title: "SldWorks::OpenDocSilent"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__OpenDocSilent.htm"
---

# SldWorks::OpenDocSilent

This method is obsolete and has been superseded by [SldWorks::OpenDoc2](SldWorks__OpenDoc3.htm).

Description

This method opens an existing document and returns a pointer to the document object. The display of dialog boxes is suppressed.

Syntax (OLE Automation)

retval = SldWorks.OpenDocSilent ( Name, Type, &Errors )

| Input: | (BSTR) Name | Name of document or full path, if not current directory |
| --- | --- | --- |
| Input: | (long) Type | Type of document as defined by swDocumentTypes_e |
| Output: | (long) Errors | Error code as defined by swFileLoadError_e |
| Return: | (LPDISPATCH) retval | Pointer to dispatch object, the document, or NULL if the operation fails |

Syntax (COM)

status = SldWorks->IOpenDocSilent ( Name, Type, &Errors, &retval )

| Input: | (BSTR) Name | Name of document or full path, if not current directory |
| --- | --- | --- |
| Input: | (long) Type | Type of document as defined by swDocumentTypes_e |
| Output: | (long) Errors | Error code as defined by swFileLoadError_e |
| Output: | (LPMODELDOC) retval | Pointer to the document or NULL if the operation fails |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

This method is identical to SldWorks::OpenDoc except that dialog boxes are suppressed. The error code returned is a bitwise OR of the error codes that were generated in opening the document. The masks to check against are the values of the enumerator swFileLoadError_e.

Calling SldWorks::OpenDoc or SldWorks::OpenDocSilent does not change the current working directory to that of the opened file; whereas, interactively using the File Open dialog box does. This may affect documents with references.

When opening a parent document (assembly, drawing, and so on.), SolidWorks also opens any additional documents that are referenced in the parent document (parts, subassemblies, and so on). SolidWorks follows certain rules in trying to locate its referenced documents. If explicit Search Folders have not been set using Tools, Options, System Options, External References, then the first place SolidWorks looks for the referenced documents is in the current working directory. If SolidWorks finds the referenced file in the current working directory, then it loads it from that directory.

Interactively performing File Open immediately sets the current working directory to that of the document being opened. However, SldWorks::OpenDoc and SldWorks::OpenDocSilent do not set the current working directory for SolidWorks. Because the user may have interactively opened files from some random directory, you cannot be certain that the current working directory is pointing to the desired location. This may affect the referenced documents that get loaded when using any of the SldWorks::OpenDocn methods versus performing File Open interactively. Because of this, you may want to consider setting the current working directory before calling any of the SldWorks::OpenDocn methods. This can be done using SldWorks::SetCurrentWorkingDirectory. To mimic the behavior of the File Open dialog, set the current working directory to that of the file being opened.

When opening files that contain references, you may also want to consider the current Search Folder settings because this may affect the references that get loaded. This can be done programmatically using SldWorks::GetSearchFolders and SldWorks::SetSearchFolders. If Search Folders are currently in use, SolidWorks looks for references in the Search Folders before trying to locate references in the current working directory.

SldWorks::OpenDocSilent will not activate and display the document if the file is already open in memory in an assembly or drawing. However, SldWorks::OpenDocSilent should return a valid ModelDoc pointer that is usable with functions that do not require a document to be displayed. If you want, SldWorks::ActivateDoc will activate and display the document. Because calling SldWorks::OpenDocSilent will not activate nor display the file, calling SldWorks::ActiveDoc will not return a pointer to this document.

To open a library feature part, use swDocPART for the Type argument.

To open foreign files (IGES, STEP, and so on) use SldWorks::LoadFile2.
