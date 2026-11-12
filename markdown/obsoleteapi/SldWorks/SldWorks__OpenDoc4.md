---
title: "SldWorks::OpenDoc4"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__OpenDoc4.htm"
---

# SldWorks::OpenDoc4

This method is obsolete and has been superseded by [SldWorks::OpenDoc6](sldworksAPI.chm::/SldWorks/SldWorks__OpenDoc6.htm).

Description

This method opens an existing document of Name and Type and returns a pointer to the document object. It also allows control over whether or not to suppress display of dialog boxes, opening the document read-only, opening the document view-only and converting a drawing to a RapidDraft drawing.

Syntax (OLE Automation)

retval = SldWorks.OpenDoc4 ( filename, type, options, configuration, &errors )

| Input: | (BSTR) filename | Document name or full path, if not in current directory, including extension |
| --- | --- | --- |
| Input: | (long) type | Document type as defined in swDocumentTypes_e |
| Input: | (long) options | Various BOOLEAN values affecting how a document is opened |
| Input: | (BSTR) configuration | Model configuration to open this document in |
| Output: | (long) errors | Load errors as defined in swFileLoadError_e |
| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the newly loaded ModelDoc, or NULL if failed to open |

Syntax (COM)

status = SldWorks->IOpenDoc4 ( filename, type, options, configuration, &errors, &retval )

| Input: | (BSTR) filename | Document name or full path, if not in current directory, including extension |
| --- | --- | --- |
| Input: | (long) type | Document type as defined in swDocumentTypes_e |
| Input: | (long) options | Various BOOLEAN values affecting how a document is opened |
| Input: | (BSTR) configuration | Model configuration to open this document in |
| Output: | (long) errors | Load errors as defined in swFileLoadError_e |
| Output: | (LPMODELDOC) retval | Pointer to the newly loaded ModelDoc or NULL if failed to open |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The options argument is a bitmask containing various BOOLEANs that affect the outcome of the document opening. Its value is a combination of the values in the swOpenDocOptions_e enumeration.

If the configuration argument is blank or names a configuration that is not present in the model being opened, the model is opened in the configuration it was last saved in (the current configuration). This argument applies only to parts and assemblies, not drawings. A document that is opened view-only can only be opened to the current configuration.

This method fires the SldWorksEvents::FileOpenNotify event. Also, SldWorksEvents::ActiveDocChangeNotify and SldWorksEvents::ActiveModelDocChangeNotify events is sent if the file being loaded is not already open as the active document.

NOTE: Calling this method does not change the current working directory to that of the opened file, whereas, interactively using the File Open dialog box does. This can affect documents with references.

When opening these parent files, certain rules are followed in trying to locate thier referenced documents. If search folders have not been set using Tools, Options,l ExternalReferences, then the first place for the referenced documents searched is in the current working directory. If the referenced file are found in the current working directory, then it is loaded from that directory.

Interactively performing File, Open immediately sets the current working directory to that of the document being opened. However, the OpenDoc methods do not set the current working directory. Because the end-user may have interactively opened files from some random directory, you cannot be certain that the current working directory is pointing to the desired location. This can affect the referenced documents that get loaded when using any of the OpenDoc methods versus performing File, Open interactively. Because of this, consider setting the current working directory before calling any of the OpenDoc methods. This can be done using the SldWorks::SetCurrentWorkingDirectory. To imitate the File, Open dialog, set the current working directory to that of the file being opened.

When opening files that contain references, consider the current search folder settings because this may affect the references that get loaded. This can be done programmatically using SldWorks::GetSearchFolders and SldWorks::SetSearchFolders. If search folders are currently in use, references are searched for in the search folders before trying to locate references in the current working directory.

This method does not activate and display the document if the file is already open in memory in an assembly or drawing. However, this method should return a valid ModelDoc pointer that is usable with functions that do not require a document to be displayed. If you wish, SldWorks::ActivateDoc2 activates and displays the document. Because calling this method does not activate nor display the file, calling the SldWorks::ActiveDoc property would not return a pointer to this document.

To open a library feature part, use swDocPART for the Type argument.

To open foreign files (IGES, STEP, and so on) use SldWorks::LoadFile2.
