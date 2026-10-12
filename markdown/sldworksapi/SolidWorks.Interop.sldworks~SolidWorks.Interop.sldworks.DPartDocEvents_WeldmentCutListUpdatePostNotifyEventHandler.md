---
title: "DPartDocEvents_WeldmentCutListUpdatePostNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_WeldmentCutListUpdatePostNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_WeldmentCutListUpdatePostNotifyEventHandler.html"
---

# DPartDocEvents_WeldmentCutListUpdatePostNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Post-notifies the user program when the weldment cut list in this part is updated.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_WeldmentCutListUpdatePostNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_WeldmentCutListUpdatePostNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_WeldmentCutListUpdatePostNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_WeldmentCutListUpdatePostNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [WeldmentCutListUpdatePostNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~WeldmentCutListUpdatePostNotify_EV.html).

## Examples

[Update Weldment Cut List and Fire Post-Notify Event (VBA)](Update_Weldment_Cut_List_and_Fire_Post-Notify_Event_Example_VB.htm)
[Update Weldment Cut List and Fire Post-Notify Event (VB.NET)](Update_Weldment_Cut_List_and_Fire_Post-Notify_Event_Example_VBNET.htm)
[Update Weldment Cut List and Fire Post-Notify Event (C#)](Update_Weldment_Cut_List_and_Fire_Post-Notify_Event_Example_CSharp.htm)

## Remarks

If developing a C++ application, use [swPartWeldmentCutListUpdatePostNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
