---
title: "_IEModelViewControlEvents_OnFinishedLoadingDocumentEventHandler Delegate (eDrawings.Interop.EModelViewControl)"
project: "eDrawings API Help"
interface: "_IEModelViewControlEvents_OnFinishedLoadingDocumentEventHandler"
member: ""
kind: "topic"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl._IEModelViewControlEvents_OnFinishedLoadingDocumentEventHandler.html"
---

# _IEModelViewControlEvents_OnFinishedLoadingDocumentEventHandler Delegate (eDrawings.Interop.EModelViewControl)

Fired when the eDrawings file has finished loading.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Sub _IEModelViewControlEvents_OnFinishedLoadingDocumentEventHandler( _
   ByVal FileName As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As New _IEModelViewControlEvents_OnFinishedLoadingDocumentEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate void _IEModelViewControlEvents_OnFinishedLoadingDocumentEventHandler(
   System.string FileName
)
```

### C++/CLI

```cpp
public delegate void _IEModelViewControlEvents_OnFinishedLoadingDocumentEventHandler(
   System.String^ FileName
)
```

### Parameters

- `FileName`: Name of document being opened

## VBA Syntax

See [OnFinishedLoadingDocument Event (EModelViewControl)](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~OnFinishedLoadingDocument_EV.html).

## Remarks

Because [IEModelViewControl::OpenDoc](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~OpenDoc.html) starts a new thread of execution and because eDrawings files are often loaded across the Internet or other potentially slow and unreliable networks, this API call can return before the document is finished loading.

Referencing a model that has not finished loading (for example, calling [IEModelViewControl::Animate](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~Animate.html)) can cause your application to hang, crash, or behave unpredictably. Therefore, listen for the OnFinishedLoadingDocument event after calling IEModelViewControl::OpenDoc so that your application knows when the eDrawings file is finished loading. Once your application receives notification that the eDrawings file has been loaded, it is safe to access the model.

## Availability

eDrawings API 2005 SP0
