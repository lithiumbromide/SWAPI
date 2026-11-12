---
title: "_IEModelViewControlEvents_OnFinishedPrintingDocumentEventHandler Delegate (eDrawings.Interop.EModelViewControl)"
project: "eDrawings API Help"
interface: "_IEModelViewControlEvents_OnFinishedPrintingDocumentEventHandler"
member: ""
kind: "topic"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl._IEModelViewControlEvents_OnFinishedPrintingDocumentEventHandler.html"
---

# _IEModelViewControlEvents_OnFinishedPrintingDocumentEventHandler Delegate (eDrawings.Interop.EModelViewControl)

Fired when an eDrawings document finishes printing.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Sub _IEModelViewControlEvents_OnFinishedPrintingDocumentEventHandler( _
   ByVal PrintJobName As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As New _IEModelViewControlEvents_OnFinishedPrintingDocumentEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate void _IEModelViewControlEvents_OnFinishedPrintingDocumentEventHandler(
   System.string PrintJobName
)
```

### C++/CLI

```cpp
public delegate void _IEModelViewControlEvents_OnFinishedPrintingDocumentEventHandler(
   System.String^ PrintJobName
)
```

### Parameters

- `PrintJobName`: String specified for the FileNameInPrintQueue argument in [IEModelViewControl::Print5](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~Print5.html) or an empty string if the ShowDialog argument of IEModelViewControl::Print5 was set to true and the user prints from the user interface

## VBA Syntax

See [OnFinishedPrintingDocument Event (EModelViewControl)](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~OnFinishedPrintingDocument_EV.html).

## Remarks

When this event is fired, eDrawings has sent all of the eDrawings data in the active document to the printer queue, and it is safe to close the active document or open another one.

This event does not guarantee that printing of the eDrawings document was successful. For example, if the printer is out of paper, eDrawings still fires this event and not [OnFailedPrintingDocument](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl._IEModelViewControlEvents_OnFailedPrintingDocumentEventHandler.html).

## Availability

eDrawings API 2006 SP0
