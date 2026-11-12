---
title: "DDrawingDocEvents_ActivateSheetPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DDrawingDocEvents_ActivateSheetPreNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_ActivateSheetPreNotifyEventHandler.html"
---

# DDrawingDocEvents_ActivateSheetPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Notifies the user program before activating the drawing sheet.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DDrawingDocEvents_ActivateSheetPreNotifyEventHandler( _
   ByVal SheetName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DDrawingDocEvents_ActivateSheetPreNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DDrawingDocEvents_ActivateSheetPreNotifyEventHandler(
   System.string SheetName
)
```

### C++/CLI

```cpp
public delegate System.int DDrawingDocEvents_ActivateSheetPreNotifyEventHandler(
   System.String^ SheetName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SheetName`: Name of the drawing sheet

## VBA Syntax

See [ActivateSheetPreNotify Event (DrawingDoc)](ms-its:sldworksapivb6.chm::/SldWorks~DrawingDoc~ActivateSheetPreNotify_EV.html).

## Examples

[Fire Notification When Activating a Sheet (VBA)](Fire_Notification_When_Sheet_is_Activated_Example_VB.htm)
[Fire Notification When Activating a Sheet (VB.NET)](Fire_Notification_When_Sheet_Is_Activated_Example_VBNET.htm)
[Fire Notification When Activating a Sheet (C#)](Fire_Notification_When_Sheet_Is_Activated_Example_CSharp.htm)

## Remarks

If developing a C++ application, use [swDrawingActivateSheetPreNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
