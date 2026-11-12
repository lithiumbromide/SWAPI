---
title: "DDrawingDocEvents_FeatureManagerTabActivatedPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DDrawingDocEvents_FeatureManagerTabActivatedPreNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_FeatureManagerTabActivatedPreNotifyEventHandler.html"
---

# DDrawingDocEvents_FeatureManagerTabActivatedPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired before the active tab in the Manager Pane changes.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DDrawingDocEvents_FeatureManagerTabActivatedPreNotifyEventHandler( _
   ByVal CommandIndex As System.Integer, _
   ByVal CommandTabName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DDrawingDocEvents_FeatureManagerTabActivatedPreNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DDrawingDocEvents_FeatureManagerTabActivatedPreNotifyEventHandler(
   System.int CommandIndex,
   System.string CommandTabName
)
```

### C++/CLI

```cpp
public delegate System.int DDrawingDocEvents_FeatureManagerTabActivatedPreNotifyEventHandler(
   System.int CommandIndex,
   System.String^ CommandTabName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CommandIndex`: Index of the active tab in the Manager Pane
- `CommandTabName`: Name of the active tab in the Manager Pane

## VBA Syntax

See [FeatureManagerTabActivatedPreNotify Event (DrawingDoc)](ms-its:sldworksapivb6.chm::/SldWorks~DrawingDoc~FeatureManagerTabActivatedPreNotify_EV.html).

## Remarks

If developing a C++ application, use [swDrawingFeatureManagerTabActivatedPreNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
