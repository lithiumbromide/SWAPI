---
title: "OpenDoc6 Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "OpenDoc6"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc6.html"
---

# OpenDoc6 Method (ISldWorks)

Opens an existing document and returns a pointer to the document object.

## Syntax

### Visual Basic (Declaration)

```vb
Function OpenDoc6( _
   ByVal FileName As System.String, _
   ByVal Type As System.Integer, _
   ByVal Options As System.Integer, _
   ByVal Configuration As System.String, _
   ByRef Errors As System.Integer, _
   ByRef Warnings As System.Integer _
) As ModelDoc2
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim FileName As System.String
Dim Type As System.Integer
Dim Options As System.Integer
Dim Configuration As System.String
Dim Errors As System.Integer
Dim Warnings As System.Integer
Dim value As ModelDoc2

value = instance.OpenDoc6(FileName, Type, Options, Configuration, Errors, Warnings)
```

### C#

```csharp
ModelDoc2 OpenDoc6(
   System.string FileName,
   System.int Type,
   System.int Options,
   System.string Configuration,
   out System.int Errors,
   out System.int Warnings
)
```

### C++/CLI

```cpp
ModelDoc2^ OpenDoc6(
   System.String^ FileName,
   System.int Type,
   System.int Options,
   System.String^ Configuration,
   [Out] System.int Errors,
   [Out] System.int Warnings
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Document name or full path if not in current directory, including extension
- `Type`: Document type as defined in [swDocumentTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)
- `Options`: Mode in which to open the document as defined in [swOpenDocOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swOpenDocOptions_e.html)
- `Configuration`: Model configuration in which to open this document

  - Applies to parts and assemblies, not drawings
  - If this argument is empty or the specified configuration is not present in the model, the model is opened in the last-used configuration
- `Errors`: Load errors as defined in [swFileLoadError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileLoadError_e.html) (**See Remarks**)
- `Warnings`: Warnings or extra information generated during the open operation as defined in [swFileLoadWarning_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileLoadWarning_e.html)

### Return Value

Newly loaded [model document](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) or NULL if document failed to open

## VBA Syntax

See [SldWorks::OpenDoc6](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~OpenDoc6.html).

## Examples

[Add Component and Mate (C++)](Add_Component_and_Mate_Example_CPlusPlus_COM.htm)
[Open Document (VBA)](Open_Document_Example_VB.htm)
[Open Document Silently (VBA)](Open_Document_Silently_Example_VB.htm)
[Open Assembly in Large Design Review Mode (VBA)](Open_Assembly_in_Large_Design_Review_Mode_Example_VB.htm)
[Open Assembly in Large Design Review Mode (VB.NET)](Open_Assembly_in_Large_Design_Review_Mode_Example_VBNET.htm)
[Open Assembly in Large Design Review Mode (C#)](Open_Assembly_in_Large_Design_Review_Mode_Example_CSharp.htm)
[Switch Documents (C#)](Switch_Documents_Example_CSharp.htm)
[Switch Documents (VB.NET)](Switch_Documents_Example_VBNET.htm)
[Switch Documents (VBA)](Switch_Documents_Example_VB.htm)

## Remarks

As of SOLIDWORKS 2020 SP03.1, SOLIDWORKS Design works on the **3D**EXPERIENCE platform as [SOLIDWORKS Design connected to the 3DEXPERIENCE platform](ms-its:sldworksapiprogguide.chm:://Overview/SOLIDWORKS_Connected.htm). Use [ISldWorks::OpenDoc7](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~OpenDoc7.html) to open documents with SOLIDWORKS Design connected to the 3DEXPERIENCE platform.

As of SOLIDWORKS 2012 SP5, loading future file versions is supported, and ISldWorks::OpenDoc6 no longer throws a [swFileLoadError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileLoadError_e.html).swFutureVersion error. Use [IModelDocExtension::IsFutureVersion](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~IsFutureVersion.html) to determine whether a component is for a future version of SOLIDWORKS.

As of SOLIDWORKS 2008, [ISldWorks::OpenDoc7](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~OpenDoc7.html) performs the same work as this method, but also:

- Allows you to open a document with a specified display state.
- Uses [IDocumentSpecification](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification.html) to specify input parameters.

This method also allows control over whether to:

- Suppress displaying dialog boxes
- Open the document read-only
- Open the document in Large Design Review mode
- Convert a drawing to a detached drawing

When opening a parent document (assembly, drawing, and so on):

- SOLIDWORKS Design also opens any additional documents that are referenced in the parent document (parts, subassemblies, and so on).
- SOLIDWORKS Design follows certain rules in trying to locate its referenced documents. If explicit Search Folders have not been set using Tools, Options, System Options, ExternalReferences, then the first place SOLIDWORKS Design looks for the referenced documents is in the current working directory. If SOLIDWORKS Design finds the referenced file in the current working directory, then it is loaded from that directory.

Calling ISldWorks::OpenDoc6 does not change the current working directory to that of the opened file, whereas, interactively using the File Open dialog box does. This may affect documents with references.

Because the user may have interactively opened files from some random directory, you cannot be certain that the current working directory is pointing to the desired location. This may affect the referenced documents that ultimately get loaded when using ISldWorks::OpenDoc6 versus performing File Open interactively. You may want to set the current working directory before calling ISldWorks::OpenDoc6. This can be done using the [ISldWorks::SetCurrentWorkingDirectory](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~SetCurrentWorkingDirectory.html) method. To mimic the behavior of the File Open dialog, you set the current working directory to that of the file being opened.

When opening files that contain references, you may also want to consider the current Search Folder settings because they may affect the references that ultimately get loaded. This can be done using [ISldWorks::GetSearchFolders](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetSearchFolders.html) and [ISldWorks::SetSearchFolders](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~SetSearchFolders.html). If Search Folders are currently in use, SOLIDWORKS Design looks for references in the Search Folders before trying to locate references in the current working directory.

If this method successfully opens an assembly, it still returns swFileLoadError_e.swFileNotFoundError in Errors if a referenced component file cannot be located.

ISldWorks::OpenDoc6 does not activate and display the document if the file is already open in memory in an assembly or drawing. However, ISldWorks::OpenDoc6 should return a valid [IModelDoc2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) pointer that is usable with functions that do not require a document to be displayed. If you want, [ISldWorks::ActivateDoc2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~ActivateDoc2.html) or [ISldWorks::IActivateDoc3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~IActivateDoc3.html) will activate and display the document. Because calling ISldWorks::OpenDoc6 does not activate nor display the file, calling the [ISldWorks::ActiveDoc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~ActiveDoc.html) or [ISldWorks::IActiveDoc2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~IActiveDoc2.html) property will not return a pointer to this document.

This method fires the the SOLIDWORKS event [FileOpenNotify2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldWorksEvents_FileOpenNotify2EventHandler.html) event. Also, the SOLIDWORKS event [ActiveDocChangeNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldWorksEvents_ActiveDocChangeNotifyEventHandler.html) and [ActiveModelDocChangeNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldWorksEvents_ActiveModelDocChangeNotifyEventHandler.html) events are sent if the file being loaded is not already open as the active document.

TIPS

| To... | Then... |
| --- | --- |
| Open an assembly in Large Design Review mode | Set the Options argument to swOpenDocOptions_LDR_EditAssembly. This option opens large assemblies in edit mode without actually loading them. This is useful for conducting a quick walk-through of a large assembly. Call IAssemblyDoc::SelectiveOpen to open selected components after an assembly has been opened in Large Design Review mode. |
| Avoid warnings when opening the document | Set the Options argument to swOpenDocOptions_Silent. The software uses the last-displayed configuration if it discovers missing configurations or component references. |
| Open a library feature part | Set the Type argument to swDocPART. |
| Open foreign files (IGES, STEP, and so on) | Use ISldWorks::LoadFile4 . |
| Avoid a warning when opening shaded models in views | Set the Options argument to swOpenDocOptions_LoadModel. This option loads the model so that the view comes in shaded automatically. |
| Avoid large increases in memory usage caused when adding parts to assemblies | Opening a model causes SceneGraph to display the model. SceneGraph uses maps with defaults sizes of 2MB - 3MB for even the simplest model. And, assemblies and parts do not share the same SceneGraph buffer. To avoid large increases in your memory usage: Set the document to invisible. Open the parts. Set the document to visible. Add the part to the assembly. See ISldWorks::DocumentVisible for details. |
| Open a document with a specified display state | Use ISldWorks::OpenDoc7. |

A warning is displayed if you [open a Detached drawing](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~IsRapidDraft.html) without loading the model, and the model was saved since the drawing was last saved.

This method honors:

- [ISldWorks::GetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserPreferenceToggle.html) swLargeAsmModeEnabled

- and -

- [ISldWorks::SetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.html) swLargeAsmModeEnabled, true/false (NOTE: if this toggle is set to true, then the file opens in lightweight mode)

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
[ISldWorks::GetOpenedFileInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenedFileInfo.html)
[ISldWorks::GetOpenFileName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenFileName.html)
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
[ISldWorks::EnableBackgroundProcessing Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~EnableBackgroundProcessing.html)
[ISldWorks::IsBackgroundProcessingCompleted Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IsBackgroundProcessingCompleted.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
