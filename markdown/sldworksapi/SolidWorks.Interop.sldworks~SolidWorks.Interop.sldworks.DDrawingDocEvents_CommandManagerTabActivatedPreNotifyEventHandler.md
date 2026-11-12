---
title: "DDrawingDocEvents_CommandManagerTabActivatedPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DDrawingDocEvents_CommandManagerTabActivatedPreNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_CommandManagerTabActivatedPreNotifyEventHandler.html"
---

# DDrawingDocEvents_CommandManagerTabActivatedPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Pre-notifies you that a SOLIDWORKS CommandManager tab is about to be activated.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DDrawingDocEvents_CommandManagerTabActivatedPreNotifyEventHandler( _
   ByVal CommandTabIndex As System.Integer, _
   ByVal CommandTabName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DDrawingDocEvents_CommandManagerTabActivatedPreNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DDrawingDocEvents_CommandManagerTabActivatedPreNotifyEventHandler(
   System.int CommandTabIndex,
   System.string CommandTabName
)
```

### C++/CLI

```cpp
public delegate System.int DDrawingDocEvents_CommandManagerTabActivatedPreNotifyEventHandler(
   System.int CommandTabIndex,
   System.String^ CommandTabName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CommandTabIndex`: Index of the tab that is about to be activated
- `CommandTabName`: Name of the tab

## VBA Syntax

See [CommandManagerTabActivatedPreNotify Event (DrawingDoc)](ms-its:sldworksapivb6.chm::/SldWorks~DrawingDoc~CommandManagerTabActivatedPreNotify_EV.html).

## Remarks

If developing a C++ application, use [swDrawingCommandManagerTabActivatedPreNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
