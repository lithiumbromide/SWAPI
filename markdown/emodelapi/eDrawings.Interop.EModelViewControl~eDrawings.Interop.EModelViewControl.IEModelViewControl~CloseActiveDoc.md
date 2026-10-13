---
title: "CloseActiveDoc Method (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "CloseActiveDoc"
kind: "method"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~CloseActiveDoc.html"
---

# CloseActiveDoc Method (IEModelViewControl)

Closes the active eDrawings document.

## Syntax

### Visual Basic (Declaration)

```vb
Sub CloseActiveDoc( _
   ByVal CommandString As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim CommandString As System.String

instance.CloseActiveDoc(CommandString)
```

### C#

```csharp
void CloseActiveDoc(
   System.string CommandString
)
```

### C++/CLI

```cpp
void CloseActiveDoc(
   System.String^ CommandString
)
```

### Parameters

- `CommandString`: Specify an empty string (""); do not specify Nothing, Empty, or vbNullString

## VBA Syntax

See [EModelViewControl::CloseActiveDoc](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~CloseActiveDoc.html).

## Examples

See [IEModelViewControl](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html) examples.

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)
[IEModelViewControl::OpenDoc Method](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~OpenDoc.html)
[IEModelViewControl::Save Method](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~Save.html)
[_IEModelViewControlEvents_OnFailedLoadingDocumentEventHandler Delegate](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl._IEModelViewControlEvents_OnFailedLoadingDocumentEventHandler.html)
[_IEModelViewControlEvents_OnFailedSavingDocumentEventHandler Delegate](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl._IEModelViewControlEvents_OnFailedSavingDocumentEventHandler.html)
[_IEModelViewControlEvents_OnFinishedPrintingDocumentEventHandler Delegate](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl._IEModelViewControlEvents_OnFinishedPrintingDocumentEventHandler.html)
[_IEModelViewControlEvents_OnFinishedSavingDocumentEventHandler Delegate](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl._IEModelViewControlEvents_OnFinishedSavingDocumentEventHandler.html)

## Availability

eDrawings API 2006 SP0
