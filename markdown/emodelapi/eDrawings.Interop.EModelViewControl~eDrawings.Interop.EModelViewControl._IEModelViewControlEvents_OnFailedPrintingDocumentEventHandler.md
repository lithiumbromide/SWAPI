---
title: "_IEModelViewControlEvents_OnFailedPrintingDocumentEventHandler Delegate (eDrawings.Interop.EModelViewControl)"
project: "eDrawings API Help"
interface: "_IEModelViewControlEvents_OnFailedPrintingDocumentEventHandler"
member: ""
kind: "topic"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl._IEModelViewControlEvents_OnFailedPrintingDocumentEventHandler.html"
---

# _IEModelViewControlEvents_OnFailedPrintingDocumentEventHandler Delegate (eDrawings.Interop.EModelViewControl)

Fired if the printer name specified in the [IEModelViewControl::SetPageSetupOptions](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~SetPageSetupOptions.html) was invalid or if an eDrawings-related error exists that prevents data from being sent to a printer queue.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Sub _IEModelViewControlEvents_OnFailedPrintingDocumentEventHandler( _
   ByVal PrintJobName As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As New _IEModelViewControlEvents_OnFailedPrintingDocumentEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate void _IEModelViewControlEvents_OnFailedPrintingDocumentEventHandler(
   System.string PrintJobName
)
```

### C++/CLI

```cpp
public delegate void _IEModelViewControlEvents_OnFailedPrintingDocumentEventHandler(
   System.String^ PrintJobName
)
```

### Parameters

- `PrintJobName`: String specified for the FileNameInPrintQueue argument in [IEModelViewControl::Print5](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~Print5.html) or an empty string if the ShowDialog argument of IEModelViewControl::Print5 was set to true and the user prints from the user interface

## VBA Syntax

See [OnFailedPrintingDocument Event (EModelViewControl)](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~OnFailedPrintingDocument_EV.html).

## Remarks

When this event is fired, eDrawings has sent all of the eDrawings data in the active document to the printer queue, and it is safe to close the active document or open another one.

## Availability

eDrawings API 2006 SP0
