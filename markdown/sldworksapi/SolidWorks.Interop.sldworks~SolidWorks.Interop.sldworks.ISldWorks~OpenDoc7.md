---
title: "OpenDoc7 Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "OpenDoc7"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc7.html"
---

# OpenDoc7 Method (ISldWorks)

Opens an existing document and returns a pointer to the document object.

## Syntax

### Visual Basic (Declaration)

```vb
Function OpenDoc7( _
   ByVal Specification As System.Object _
) As ModelDoc2
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Specification As System.Object
Dim value As ModelDoc2

value = instance.OpenDoc7(Specification)
```

### C#

```csharp
ModelDoc2 OpenDoc7(
   System.object Specification
)
```

### C++/CLI

```cpp
ModelDoc2^ OpenDoc7(
   System.Object^ Specification
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Specification`: [Document specification](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDocumentSpecification.html)

### Return Value

[Document](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html)

## VBA Syntax

See [SldWorks::OpenDoc7](ms-its:sldworksapivb6.chm::/Sldworks~SldWorks~OpenDoc7.html).

## Examples

[Hide All Edges in Drawing (VBA)](Hide_All_Edges_in_Drawing_View_Example_VB.htm)
[Open Drawing Document Read-only (VBA)](Open_Drawing_Document_Read-only_Example_VB.htm)
[Get Whether Components Are Loaded (C#)](Get_Whether_Components_Are_Loaded_Example_CSharp.htm)
[Get Whether Components Are Loaded (VB.NET)](Get_Whether_Components_Are_Loaded_Example_VBNET.htm)
[Get Whether Components Are Loaded (VBA)](Get_Whether_Components_Are_Loaded_Example_VB.htm)
[Open Assembly Document (C#)](Open_Assembly_Document_Example_CSharp.htm)
[Open Assembly Document (VB.NET)](Open_Assembly_Document_Example_VBNET.htm)
[Open Assembly Document (VBA)](Open_Assembly_Document_Example_VB.htm)

## Remarks

As of SOLIDWORKS 2020 SP03.1, SOLIDWORKS Design can run on the **3D**EXPERIENCE platform as [SOLIDWORKS Design connected to the 3DEXPERIENCE platform](ms-its:sldworksapiprogguide.chm:://Overview/SOLIDWORKS_Connected.htm). While running SOLIDWORKS Design connected to the 3DEXPERIENCE platform, this method can be called to either import local SOLIDWORKS documents or open **3D**EXPERIENCE documents. Inspect the Remarks section on each property of IDocumentSpecification to see whether it can be used to open a **3D**EXPERIENCE platform document. Also see [IDocumentSpecifiation::PLMObjectSpecification](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~PLMObjectSpecification.html).

The following remarks apply primarily to SOLIDWORKS Design.

When opening a parent document (assembly, drawing, and so on):

- SOLIDWORKS Design also opens any additional documents that are referenced in the parent document (parts, subassemblies, and so on).
- SOLIDWORKS Design follows certain rules in trying to locate its referenced documents. If explicit Search Folders have not been set using Tools, Options, System Options, ExternalReferences, then the first place SOLIDWORKS Design looks for the referenced documents is in the current working directory. If SOLIDWORKS Design finds the referenced file in the current working directory, then it is loaded from that directory.

Calling ISldWorks::OpenDoc7 does not change the current working directory to that of the opened file, whereas, interactively using the File Open dialog box does. This may affect documents with references.

Because the user may have interactively opened files from some random directory, you cannot be certain that the current working directory is pointing to the desired location. This may affect the referenced documents that ultimately get loaded when using ISldWorks::OpenDoc7 versus performing File Open interactively. You may want to set the current working directory before calling ISldWorks::OpenDoc7. This can be done using the [ISldWorks::SetCurrentWorkingDirectory](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~SetCurrentWorkingDirectory.html) method. To mimic the behavior of the File Open dialog, you set the current working directory to that of the file being opened.

When opening files that contain references, you may also want to consider the current Search Folder settings because they may affect the references that ultimately get loaded. This can be done using [ISldWorks::GetSearchFolders](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetSearchFolders.html) and [ISldWorks::SetSearchFolders](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~SetSearchFolders.html). If Search Folders are currently in use, SOLIDWORKS looks for references in the Search Folders before trying to locate references in the current working directory.

ISldWorks::OpenDoc7 does not activate and display the document if the file is already open in memory in an assembly or drawing. However, ISldWorks::OpenDoc7 should return a valid [IModelDoc2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) pointer that is usable with functions that do not require a document to be displayed. If you want, [ISldWorks::ActivateDoc2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~ActivateDoc2.html) or [ISldWorks::IActivateDoc3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~IActivateDoc3.html) will activate and display the document. Because calling ISldWorks::OpenDoc7 does not activate nor display the file, calling the [ISldWorks::ActiveDoc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~ActiveDoc.html) or [ISldWorks::IActiveDoc2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~IActiveDoc2.html) property will not return a pointer to this document.

This method fires the SOLIDWORKS event [FileOpenNotify2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldWorksEvents_FileOpenNotify2EventHandler.html) event. Also, the SOLIDWORKS event [ActiveDocChangeNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldWorksEvents_ActiveDocChangeNotifyEventHandler.html) and [ActiveModelDocChangeNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldWorksEvents_ActiveModelDocChangeNotifyEventHandler.html) events are sent if the file being loaded is not already open as the active document.

TIPS

| To... | Then... |
| --- | --- |
| Open an assembly in Large Design Review mode | Set IDocumentSpecification::ViewOnly to true. This option displays large assemblies without actually loading them. This is useful for conducting a quick walk-through of a large assembly. Call IAssemblyDoc::SelectiveOpen to open selected components after an assembly has been opened in Large Design Review mode. |
| Avoid warnings when opening the document | Set IDocumentSpecification::Silent to true. The software uses the last-displayed configuration if it discovers missing configurations or component references. |
| Open a library feature part | Set IDocumentSpecification::DocumentType to swDocumentTypes_e .swDocPART. |
| Open foreign files (IGES, STEP, and so on) | Use ISldWorks::LoadFile4 . |
| Avoid a warning when opening shaded models in views | Set IDocumentSpecification::LoadModel to true. This option loads the model so that the view comes in shaded automatically. |
| Avoid large increases in memory usage caused when adding parts to assemblies | Opening a model causes SceneGraph to display the model. SceneGraph uses maps with defaults sizes of 2MB - 3MB for even the simplest model. And, assemblies and parts do not share the same SceneGraph buffer. To avoid large increases in your memory usage: Set the document to invisible. Open the parts. Set the document to visible. Add the part to the assembly. See ISldWorks::DocumentVisible for details. |
| To open a document without a specified display state | Use ISldWorks::OpenDoc6 . |

A warning is displayed if you [open a Detached drawing](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~IsRapidDraft.html) without loading the model, and the model was saved since the drawing was last saved.

This method honors:

- [ISldWorks::GetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserPreferenceToggle.html) swLargeAsmModeEnabled

- and -

- [ISldWorks::SetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.html) swLargeAsmModeEnabled, true/false (NOTE: if this toggle is set to true, then the document opens in lightweight mode)

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::CloseAllDocuments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseAllDocuments.html)
[ISldWorks::CloseDoc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseDoc.html)
[ISldWorks::CopyDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CopyDocument.html)
[ISldWorks::EnumDocuments2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~EnumDocuments2.html)
[ISldWorks::GetCurrentWorkingDirectory Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentWorkingDirectory.html)
[ISldWorks::GetDataFolder Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDataFolder.html)
[ISldWorks::GetDocumentDependencies2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDocumentDependencies2.html)
[ISldWorks::GetFirstDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetFirstDocument.html)
[ISldWorks::GetOpenDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenDocument.html)
[ISldWorks::GetOpenDocumentByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenDocumentByName.html)
[ISldWorks::GetRecentFiles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetRecentFiles.html)
[ISldWorks::ICopyDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ICopyDocument.html)
[ISldWorks::IGetDocumentDependencies2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetDocumentDependencies2.html)
[ISldWorks::IGetFirstDocument2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetFirstDocument2.html)
[ISldWorks::IGetOpenDocumentByName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetOpenDocumentByName2.html)
[ISldWorks::IMoveDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IMoveDocument.html)
[ISldWorks::PreviewDoc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~PreviewDoc.html)
[ISldWorks::PreviewDocx64 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~PreviewDocx64.html)
[ISldWorks::QuitDoc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~QuitDoc.html)
[ISldWorks::SetPromptFilename Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetPromptFilename.html)
[ISldWorks::IsBackgroundProcessingCompleted Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IsBackgroundProcessingCompleted.html)
[ISldWorks::EnableBackgroundProcessing Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~EnableBackgroundProcessing.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
