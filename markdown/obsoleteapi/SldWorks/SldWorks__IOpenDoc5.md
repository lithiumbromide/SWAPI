---
title: "SldWorks::IOpenDoc5"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__IOpenDoc5.htm"
---

# SldWorks::IOpenDoc5

This method is obsolete and has been superseded by [SldWorks::OpenDoc6](sldworksAPI.chm::/SldWorks/SldWorks__OpenDoc6.htm).

Description

This method opens an existing document of Name and Type and returns a pointer to the document object. It also allows control over whether or not to suppress display of dialog boxes, opening the document read-only, opening the document view-only and converting a drawing to a RapidDraft drawing.

Syntax (OLE Automation)

Not available.

Syntax (COM)

status = SldWorks->IOpenDoc5 ( filename, type, options, configuration, &errors, &retval )

| Input: | (BSTR) filename | Document name (or full path, if not in current directory), including extension |
| --- | --- | --- |
| Input: | (long) type | Document type as defined in swDocumentTypes_e enum |
| Input: | (long) options | Various BOOLEAN values affecting how a document is opened |
| Input: | (BSTR) configuration | Model configuration with which to open this document |
| Output: | (long) errors | Load errors as defined in swFileLoadError_e |
| Output: | (LPMODELDOC2) retval | Pointer to the newly loaded ModelDoc or NULL if failed to open |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The options argument is a bitmask containing various BOOLEANs that affect the outcome of the document opening. Its value is a combination of the values in the swOpenDocOptions_e enumeration.

If the configuration argument is blank or names a configuration that is not present in the model being opened, the model is opened in the configuration it was last saved in (the current configuration). This argument applies only to parts and assemblies, not drawings. A document that is being opened view-only can only be opened to the current configuration.

This method fires SldWorksEvents::FileOpenNotify event. Also, SldWorks::ActiveDocChangeNotify and SldWorks::ActiveModelDocChangeNotify events are sent if the file being loaded is not already open as the active document.

When opening a parent document, any additional documents that are referenced in the parent document are also opened.

When opening these parent files, certain rules are followed to locate referenced documents. If explicit search folders have not been set using Tools, Options, ExternalReferences, then the first place searched for the referenced documents)is in the current working directory. The referenced file are found in the current working directory, then it is loaded from that directory.

Interactively performing File, Open immediately sets the current working directory to that of the document being opened. However, the OpenDoc methods do not set the current working directory. Because the end-user may have interactively opened files from some random directory, you cannot be certain that the current working directory"is pointing to the desired location. This can affect the referenced documents that ultimately get loaded when using any of the OpenDoc methods versus performing File, Open interactively. Because of this, you might want to consider setting the current working directory before calling any of the OpenDoc methods. This can be done using SldWorks::SetCurrentWorkingDirectory. To imitate the behavior of the File Open dialog, set the current working directory to that of the file being opened.

When opening files that contain references, you might also want to consider the current search folder settings because this can affect the references that get loaded. This can be done programmatically using SldWorks::GetSearchFolders and SldWorks::SetSearchFolders. If search folders are currently in use, references in the search folders are searched before trying to locate references in the current working directory.

The OpenDoc methods do not activate and display the document if the file is already open in memory in an assembly or drawing. However, these methods should return a valid ModelDoc pointer that is usable with functions that do not require a document to be displayed. If you want, SldWorks::ActivateDoc2 activates and displays the document. Because calling OpenDoc methods do not activate nor display the file, calling the ASldWorks::ActiveDoc property does not return a pointer to this document.

To open a library feature part, use swDocPART for the Type argument.

To open foreign files (IGES, STEP, etc.) use SldWorks::LoadFile2.

For a document that is being opened view-only, you must pass an empty string in the configuration argument.
