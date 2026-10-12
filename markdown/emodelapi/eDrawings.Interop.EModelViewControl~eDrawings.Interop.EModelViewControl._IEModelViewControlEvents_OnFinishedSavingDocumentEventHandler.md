---
title: "_IEModelViewControlEvents_OnFinishedSavingDocumentEventHandler Delegate (eDrawings.Interop.EModelViewControl)"
project: "eDrawings API Help"
interface: "_IEModelViewControlEvents_OnFinishedSavingDocumentEventHandler"
member: ""
kind: "topic"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl._IEModelViewControlEvents_OnFinishedSavingDocumentEventHandler.html"
---

# _IEModelViewControlEvents_OnFinishedSavingDocumentEventHandler Delegate (eDrawings.Interop.EModelViewControl)

Fired when an eDrawings file finishes saving.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Sub _IEModelViewControlEvents_OnFinishedSavingDocumentEventHandler()
```

### Visual Basic (Usage)

```vb
Dim instance As New _IEModelViewControlEvents_OnFinishedSavingDocumentEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate void _IEModelViewControlEvents_OnFinishedSavingDocumentEventHandler()
```

### C++/CLI

```cpp
public delegate void _IEModelViewControlEvents_OnFinishedSavingDocumentEventHandler();
```

## VBA Syntax

See [OnFinishedSavingDocument Event (EModelViewControl)](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~OnFinishedSavingDocument_EV.html).

## Remarks

Because [IEModelViewControl::Save](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~Save.html) starts a new thread of execution and because eDrawings files are often saved across the internet or other potentially slow and unreliable networks, this call can return before the document is finished saving.

Referencing a model that has not finished saving can cause your application to hang, crash, or behave unpredictably. Therefore, listen for the IEModelViewControl::OnFinishedSavingDocument event after calling IEModelViewControl::Save so that your application knows when the eDrawings file is finished saving. Once your application receives notification that the eDrawings file has been saved, it is safe to exit your application or load another file in the same function.

## Availability

eDrawings API 2005 SP0
