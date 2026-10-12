---
title: "Save Method (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "Save"
kind: "method"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~Save.html"
---

# Save Method (IEModelViewControl)

Saves the eDrawings file.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Save( _
   ByVal SaveName As System.String, _
   ByVal SaveAs As System.Boolean, _
   ByVal CommandString As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim SaveName As System.String
Dim SaveAs As System.Boolean
Dim CommandString As System.String

instance.Save(SaveName, SaveAs, CommandString)
```

### C#

```csharp
void Save(
   System.string SaveName,
   System.bool SaveAs,
   System.string CommandString
)
```

### C++/CLI

```cpp
void Save(
   System.String^ SaveName,
   System.bool SaveAs,
   System.String^ CommandString
)
```

### Parameters

- `SaveName`: Fully qualified path and file name to which to save the data (see Remarks)
- `SaveAs`:

  | If... | Then... |
  | --- | --- |
  | True | A dialog is displayed prompting the user to specify where to save the file. SaveName is ignored. |
  | False | If SaveName is specified, then the active document is saved to that location and file. If SaveName is empty, then the active document is saved to the location and file from which it was opened. |
- `CommandString`: Specify an empty string (""); do not specify Nothing, Empty, or vbNullString

## VBA Syntax

See [EModelViewControl::Save](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~Save.html).

## Examples

See [IEModelViewControl](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html) examples.

## Remarks

To save a document to a specific export format, you must include the filename extension of that format in the file name. Valid filename extensions for the supported export formats are .jpg, .tif, .bmp, .stl, .exe, .htm, .zip, .edrw, .eprt, and .easm.

NOTE: Certain export formats are only appropriate for certain document types. For example, you cannot save a .edrw file as an STL file using this method or in the user interface.

Because EModelViewControl::Save starts a new thread of execution and because eDrawings files are often saved across the Internet or other potentially slow and unreliable networks, this API call can return before the document is finished saving.

Referencing a model that has not finished saving can cause your application to hang, crash, or behave unpredictably. Therefore, listen for the [OnFinishedSavingDocument](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl._IEModelViewControlEvents_OnFinishedSavingDocumentEventHandler.html) event after calling EModelViewControl::Save so that your application knows when the eDrawings file is finished saving. Once your application receives notification that the eDrawings file has been saved, it is safe to exit your application or load another file in the same function.

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)
[IEModelViewControl::CloseActiveDoc Method](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~CloseActiveDoc.html)
[IEModelViewControl::OpenDoc Method](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~OpenDoc.html)
[_IEModelViewControlEvents_OnFailedLoadingDocumentEventHandler Delegate](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl._IEModelViewControlEvents_OnFailedLoadingDocumentEventHandler.html)
[_IEModelViewControlEvents_OnFailedSavingDocumentEventHandler Delegate](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl._IEModelViewControlEvents_OnFailedSavingDocumentEventHandler.html)
[_IEModelViewControlEvents_OnFinishedLoadingDocumentEventHandler Delegate](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl._IEModelViewControlEvents_OnFinishedLoadingDocumentEventHandler.html)

## Availability

eDrawings API 2005 SP0
