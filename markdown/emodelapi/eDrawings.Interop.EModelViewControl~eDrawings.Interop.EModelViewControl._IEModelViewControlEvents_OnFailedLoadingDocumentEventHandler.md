---
title: "_IEModelViewControlEvents_OnFailedLoadingDocumentEventHandler Delegate (eDrawings.Interop.EModelViewControl)"
project: "eDrawings API Help"
interface: "_IEModelViewControlEvents_OnFailedLoadingDocumentEventHandler"
member: ""
kind: "topic"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl._IEModelViewControlEvents_OnFailedLoadingDocumentEventHandler.html"
---

# _IEModelViewControlEvents_OnFailedLoadingDocumentEventHandler Delegate (eDrawings.Interop.EModelViewControl)

Fired when the specified eDrawings document fails to load.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Sub _IEModelViewControlEvents_OnFailedLoadingDocumentEventHandler( _
   ByVal FileName As System.String, _
   ByVal ErrorCode As System.Integer, _
   ByVal ErrorString As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As New _IEModelViewControlEvents_OnFailedLoadingDocumentEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate void _IEModelViewControlEvents_OnFailedLoadingDocumentEventHandler(
   System.string FileName,
   System.int ErrorCode,
   System.string ErrorString
)
```

### C++/CLI

```cpp
public delegate void _IEModelViewControlEvents_OnFailedLoadingDocumentEventHandler(
   System.String^ FileName,
   System.int ErrorCode,
   System.String^ ErrorString
)
```

### Parameters

- `FileName`: File name
- `ErrorCode`: Not used
- `ErrorString`: Not used

## VBA Syntax

See [OnFailedLoadingDocument Event (EModelViewControl)](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~OnFailedLoadingDocument_EV.html).

## Availability

eDrawings API 2006 SP0
