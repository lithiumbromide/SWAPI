---
title: "DDrawingDocEvents_ActivateSheetPostNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DDrawingDocEvents_ActivateSheetPostNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_ActivateSheetPostNotifyEventHandler.html"
---

# DDrawingDocEvents_ActivateSheetPostNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Notifies the user program after activating the drawing sheet.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DDrawingDocEvents_ActivateSheetPostNotifyEventHandler( _
   ByVal SheetName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DDrawingDocEvents_ActivateSheetPostNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DDrawingDocEvents_ActivateSheetPostNotifyEventHandler(
   System.string SheetName
)
```

### C++/CLI

```cpp
public delegate System.int DDrawingDocEvents_ActivateSheetPostNotifyEventHandler(
   System.String^ SheetName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SheetName`: Name of the drawing sheet

## VBA Syntax

See [ActivateSheetPostNotify Event (DrawingDoc)](ms-its:sldworksapivb6.chm::/SldWorks~DrawingDoc~ActivateSheetPostNotify_EV.html).

## Examples

[Fire Notification When Activating a Sheet (VBA)](Fire_Notification_When_Sheet_is_Activated_Example_VB.htm)

## Remarks

This event only fires when a drawing sheet is interactively activated in the SOLIDWORKS Design user interface; this event does not fire when a sheet is activated via an API call.

If developing a C++ application, use [swDrawingActivateSheetPostNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
