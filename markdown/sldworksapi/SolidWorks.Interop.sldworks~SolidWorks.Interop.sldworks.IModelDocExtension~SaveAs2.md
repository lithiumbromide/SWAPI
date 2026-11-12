---
title: "SaveAs2 Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "SaveAs2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveAs2.html"
---

# SaveAs2 Method (IModelDocExtension)

Obsolete. Superseded by [IModelDocExtension::SaveAs3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveAs3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SaveAs2( _
   ByVal Name As System.String, _
   ByVal Version As System.Integer, _
   ByVal Options As System.Integer, _
   ByVal ExportData As System.Object, _
   ByVal ReferencePrefixOrSuffixText As System.String, _
   ByVal AddTextAsPrefix As System.Boolean, _
   ByRef Errors As System.Integer, _
   ByRef Warnings As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Name As System.String
Dim Version As System.Integer
Dim Options As System.Integer
Dim ExportData As System.Object
Dim ReferencePrefixOrSuffixText As System.String
Dim AddTextAsPrefix As System.Boolean
Dim Errors As System.Integer
Dim Warnings As System.Integer
Dim value As System.Boolean

value = instance.SaveAs2(Name, Version, Options, ExportData, ReferencePrefixOrSuffixText, AddTextAsPrefix, Errors, Warnings)
```

### C#

```csharp
System.bool SaveAs2(
   System.string Name,
   System.int Version,
   System.int Options,
   System.object ExportData,
   System.string ReferencePrefixOrSuffixText,
   System.bool AddTextAsPrefix,
   out System.int Errors,
   out System.int Warnings
)
```

### C++/CLI

```cpp
System.bool SaveAs2(
   System.String^ Name,
   System.int Version,
   System.int Options,
   System.Object^ ExportData,
   System.String^ ReferencePrefixOrSuffixText,
   System.bool AddTextAsPrefix,
   [Out] System.int Errors,
   [Out] System.int Warnings
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`: Full pathname of the document to save; the file extension indicates any conversion that should be performed (for example, **Part1.igs** to save in IGES format) (see **Remarks**)
- `Version`: Format in which to save this document as defined in [swSaveAsVersion_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSaveAsVersion_e.html) (see **Remarks**)
- `Options`: Option indicating how to save the document as defined in [swSaveAsOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSaveAsOptions_e.html) (see **Remarks**)
- `ExportData`: [IExportPdfData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IExportPdfData.html) object for exporting drawing sheets to PDF (see **Remarks**)
- `ReferencePrefixOrSuffixText`: Text to prefix names of reference files (AddTextAsPrefix is true) or text to suffix them (AddTextAsPrefix is false); empty string to neither prefix nor suffix the names of reference files; valid only for assemblies (see **Remarks**)
- `AddTextAsPrefix`: True to prefix names of reference files with ReferencePrefixOrSuffixText, false to suffix names of reference files with ReferencePrefixOrSuffixText; valid only for assemblies and when ReferencePrefixOrSuffixText is a non-empty string (see **Remarks**)
- `Errors`: Errors that caused the save to fail as defined in [swFileSaveError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileSaveError_e.html) (see **Remarks**)
- `Warnings`: Warnings or extra information generated during the save operation as defined in [swFileSaveWarning_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileSaveWarning_e.html) (see **Remarks**)

### Return Value

True if the save is successful, false if not

## VBA Syntax

See [ModelDocExtension::SaveAs2](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~SaveAs2.html).

## Examples

'VBA

'Preconditions:

'1. Open **C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\tutorial\advdrawings\98food processor.sldasm**.

'2. Ensure **c:\temp** exists.

'Postconditions:

'1. Silently saves a copy of the assembly (**food_processor_Suff.sldasm**) and re-named reference files (***_Suff.sldprt**) to **c:\temp**.

'2. Opens the saved assembly.

'3. Observe the re-named components in the FeatureManager design tree.

' NOTE: Because the model is used elsewhere, do not save changes.

'=========================================

Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim boolstatus As Boolean
Dim FileName As String
Dim DIR As String
Dim EXT As String
Dim opt As Long
Dim lErrors As Long
Dim lWarnings As Long

Sub main()

DIR = "c:\temp\"

EXT = ".SLDASM"
Set swApp = Application.SldWorks
swApp.Visible = True

Set swModel = swApp.ActiveDoc
Set swModelDocExt = swModel.Extension

'1 = swSaveAsOptions_Silent
'4 = swSaveAsOptions_SaveReferenced
'512 = swSaveAsOptions_CopyAndOpen

opt = 512 + 4 + 1

FileName = DIR & "food_processor_Suff" & EXT

boolstatus = swModelDocExt.SaveAs2(FileName, 0, opt, Nothing, "_Suff", False, lErrors, lWarnings)

End Sub

## Remarks

The difference between this method and the now obsolete [IModelDocExtension::SaveAs](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveAs.html) is that when you save assemblies using this method, you can prefix or suffix reference file names by specifying AddTextAsPrefix and ReferencePrefixOrSuffixText. To save references in the assembly, specify Options by bitwise ANDing swSaveAsOptions_e:

- swSaveAsOptions_SaveReferenced
- swSaveAsOptions_Copy or swSaveAsOptions_CopyAndOpen
- swSaveAsOptions_Silent

To save as an IGES, STL, or STEP file, the document to convert must be the active document. Before calling this method:

1. Call [ISldWorks::ActivateDoc3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~ActivateDoc3.html) to make the document to convert the active document.
2. Call [ISldWorks::ActiveDoc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~ActiveDoc.html) to get the active document.

This method:

- Exports the entire model, unless faces or bodies are selected, in which case, it exports only those. Call [IModelDoc2::ClearSelection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ClearSelection2.html) before calling IModelDocExtension::SaveAs to clear the selection list and export the entire model.
- Overwrites existing files unless they are read only.
- Results in the FileSaveNotify event being sent to any application listening.
- Removes any configuration-specific bitmap previews, except the current configuration's.

Saving a document as PDF when the document is open as view only is not supported.

Do not use ModelDocExtension::SaveAs to copy assemblies, drawings, or parts with in-context references. Instead, use [ISldWorks::CopyDocument](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~CopyDocument.html) or [ISldWorks::ICopyDocument](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~ICopyDocument.html).

Use Name to specify the full pathname of the saved document. If you specify only the file name, then it is saved in the active document's directory. The filename extension indicates the conversion that should be performed (for example, **Part1.igs** to save to IGES). If the filename extension does not uniquely indicate how the file should be formatted, use Version to specify how to save the file. For example, to save:

- A standard drawing document as a detached drawing, specify swSaveAsDetachedDrawing for Version.
- A detached drawing as a standard drawing, specify swSaveAsStandardDrawing for Version.
- A standard or detached drawing document in the same format, specify swSaveAsCurrentVersion for Version.

Use ExportData to specify which drawings sheets to save to PDF. If ExportData is Nothing or null, then all sheets are saved to PDF. Saving a document as PDF when the document is open as view-only is not supported.

Use Options to specify save options. You can specify additional options using [ISldWorks::SetUserPreferenceIntegerValue](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~SetUserPreferenceIntegerValue.html). For example:

```vb
' Save assembly as multibody part and save exterior faces as surface bodies
swApp.SetUserPreferenceIntegerValue swSaveAssemblyAsPartOptions, _
swSaveAsmAsPart_ExteriorFaces
swModelDocExt.SaveAs "H:\Assem1.SLDPRT", swSaveAsCurrentVersion, _
swSaveAsOptions_Silent, Nothing, nErrors, nWarnings

- or -

' Save all drawing sheets in active drawing document as an eDrawings file
swApp.SetUserPreferenceIntegerValue swEdrawingsSaveAsSelectionOption, swEdrawingSaveAll
swModelDocExt.SaveAs "H:\Grid.edrw", swSaveAsCurrentVersion, _
swSaveAsOptions_Silent, Nothing, nErrors, nWarnings
```

If the file is saved successfully, then the returned value is true and Errors is 0. If the save is not successful, then the returned value is false and Errors contains a bitwise OR of the error codes that were generated in saving the document. Check the masks against the [swFileSaveError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileSaveError_e.html) enumeration. If you do not want SOLIDWORKS to return error information, set Errors to Nothing or null.

Even if the file is saved successfully, there might be warnings or information that occur during the save operation in which you might be interested. Warnings contains a bitwise OR of the warning codes that were generated when saving the document. Check the masks against the [swFileSaveWarning_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileSaveWarning_e.html) enumeration. If you do not want warning information returned, set Warnings to Nothing or null.

Use [IModelDoc2::Save3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~Save3.html) to save a file using its current name.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::SaveDeFeaturedFile Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveDeFeaturedFile.html)
[ISldWorks::ActivateDoc3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ActivateDoc3.html)
[ISldWorks::ActiveDoc Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ActiveDoc.html)
[ISldWorks::CheckpointConvertedDocument Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CheckpointConvertedDocument.html)
[ISldWorks::CloseAllDocuments Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseAllDocuments.html)
[ISldWorks::CloseDoc Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseDoc.html)
[ISldWorks::CopyDocument Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CopyDocument.html)
[ISldWorks::ExitApp Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ExitApp.html)
[ISldWorks::LoadFile4 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadFile4.html)
[ISldWorks::OpenDoc7 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc7.html)
[ISldWorks::QuitDoc Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~QuitDoc.html)

## Availability

SOLIDWORKS 2019 SP01, Revision Number 27.1
