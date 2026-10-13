---
title: "OpenDoc Method (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "OpenDoc"
kind: "method"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~OpenDoc.html"
---

# OpenDoc Method (IEModelViewControl)

Opens the specified eDrawings file.

## Syntax

### Visual Basic (Declaration)

```vb
Sub OpenDoc( _
   ByVal FileName As System.String, _
   ByVal IsTemp As System.Boolean, _
   ByVal PromptToSave As System.Boolean, _
   ByVal ReadOnly As System.Boolean, _
   ByVal CommandString As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim FileName As System.String
Dim IsTemp As System.Boolean
Dim PromptToSave As System.Boolean
Dim ReadOnly As System.Boolean
Dim CommandString As System.String

instance.OpenDoc(FileName, IsTemp, PromptToSave, ReadOnly, CommandString)
```

### C#

```csharp
void OpenDoc(
   System.string FileName,
   System.bool IsTemp,
   System.bool PromptToSave,
   System.bool ReadOnly,
   System.string CommandString
)
```

### C++/CLI

```cpp
void OpenDoc(
   System.String^ FileName,
   System.bool IsTemp,
   System.bool PromptToSave,
   System.bool ReadOnly,
   System.String^ CommandString
)
```

### Parameters

- `FileName`: Fully qualified path and file name (see Remarks)
- `IsTemp`: True to delete the local copy of a remote non-eDrawings file when that file is closed, false to keep the local copy
- `PromptToSave`: True to show a dialog if the user exits without saving the file, false to not show a dialog
- `ReadOnly`: True if the file is read-only, false if not
- `CommandString`: Specify an empty string (""); do not specify Nothing, Empty, or vbNullString

## VBA Syntax

See [EModelViewControl::OpenDoc](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~OpenDoc.html).

## Examples

See [IEModelViewControl](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html) examples.

## Remarks

Syntax for specifying the file name:

| Access | Example |
| --- | --- |
| Windows local file | C:\temp\myAssembly.easm |
| Windows network path | //myServer//mySharedFolder//myDrawing.edrw (Assume that the folder is shared and note the use of the forward slashes) |
| URL | Supported: http://myHost/MyFolder/MyPart.eprt Not supported: file:///C:/temp\myDwg.dwg |

Because IEModelViewControl::OpenDoc starts a new thread of execution and because eDrawings files are often loaded across the Internet or other potentially slow and unreliable networks, this API call can return before the document is finished loading.

Referencing a model that has not finished loading (for example, calling [IEModelViewControl::Animate](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~Animate.html)) can cause your application to hang, crash, or behave unpredictably. Therefore, listen for the [OnFinishedLoadingDocument](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl._IEModelViewControlEvents_OnFinishedLoadingDocumentEventHandler.html) event after calling IEModelViewControl::OpenDoc so that your application knows when the eDrawings file is finished loading. Once your application receives notification that the eDrawings file has been loaded, it is safe to access the model.

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)
[IEModelViewControl::CloseActiveDoc Method](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~CloseActiveDoc.html)
[IEModelViewControl::Save Method](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~Save.html)
[_IEModelViewControlEvents_OnFailedLoadingDocumentEventHandler Delegate](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl._IEModelViewControlEvents_OnFailedLoadingDocumentEventHandler.html)
[_IEModelViewControlEvents_OnFailedSavingDocumentEventHandler Delegate](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl._IEModelViewControlEvents_OnFailedSavingDocumentEventHandler.html)
[_IEModelViewControlEvents_OnFinishedSavingDocumentEventHandler Delegate](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl._IEModelViewControlEvents_OnFinishedSavingDocumentEventHandler.html)
[IEModelViewControl::UserName Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~UserName.html)
[IEModelViewControl::Password Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~Password.html)
[IEmodelViewControl::AlwaysShowWarningWatermark Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~AlwaysShowWarningWatermark.html)

## Availability

eDrawings API 2005 SP0
