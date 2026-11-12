---
title: "_IEModelViewControlEvents_OnFailedSavingDocumentEventHandler Delegate (eDrawings.Interop.EModelViewControl)"
project: "eDrawings API Help"
interface: "_IEModelViewControlEvents_OnFailedSavingDocumentEventHandler"
member: ""
kind: "topic"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl._IEModelViewControlEvents_OnFailedSavingDocumentEventHandler.html"
---

# _IEModelViewControlEvents_OnFailedSavingDocumentEventHandler Delegate (eDrawings.Interop.EModelViewControl)

Fired when saving an eDrawings document fails.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Sub _IEModelViewControlEvents_OnFailedSavingDocumentEventHandler( _
   ByVal FileName As System.String, _
   ByVal ErrorCode As System.Integer, _
   ByVal ErrorString As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As New _IEModelViewControlEvents_OnFailedSavingDocumentEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate void _IEModelViewControlEvents_OnFailedSavingDocumentEventHandler(
   System.string FileName,
   System.int ErrorCode,
   System.string ErrorString
)
```

### C++/CLI

```cpp
public delegate void _IEModelViewControlEvents_OnFailedSavingDocumentEventHandler(
   System.String^ FileName,
   System.int ErrorCode,
   System.String^ ErrorString
)
```

### Parameters

- `FileName`: Name of file to save
- `ErrorCode`: Not used
- `ErrorString`: Not used

## VBA Syntax

See [OnFailedSavingDocument Event (EModelViewControl)](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~OnFailedSavingDocument_EV.html).

## Availability

eDrawings API 2006 SP0
