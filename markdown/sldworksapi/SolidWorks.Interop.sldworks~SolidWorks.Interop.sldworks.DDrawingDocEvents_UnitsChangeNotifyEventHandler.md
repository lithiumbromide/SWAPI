---
title: "DDrawingDocEvents_UnitsChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DDrawingDocEvents_UnitsChangeNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_UnitsChangeNotifyEventHandler.html"
---

# DDrawingDocEvents_UnitsChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Raised when document units change.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DDrawingDocEvents_UnitsChangeNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DDrawingDocEvents_UnitsChangeNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DDrawingDocEvents_UnitsChangeNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DDrawingDocEvents_UnitsChangeNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [UnitsChangeNotify Event (DrawingDoc)](ms-its:sldworksapivb6.chm::/SldWorks~DrawingDoc~UnitsChangeNotify_EV.html).

## Remarks

If developing a C++ application, use [swDrawingUnitsChangeNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
