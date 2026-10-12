---
title: "DPartDocEvents_UserSelectionPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_UserSelectionPreNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_UserSelectionPreNotifyEventHandler.html"
---

# DPartDocEvents_UserSelectionPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when an interactive user moves the cursor over or clicks a model view in a part document.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_UserSelectionPreNotifyEventHandler( _
   ByVal SelType As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_UserSelectionPreNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_UserSelectionPreNotifyEventHandler(
   System.int SelType
)
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_UserSelectionPreNotifyEventHandler(
   System.int SelType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SelType`: Type of object to be selected as defined by [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

## VBA Syntax

See [UserSelectionPreNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~UserSelectionPreNotify_EV.html).

## Examples

[Disable Selection of Faces and Edges Using a Pre-Notify Event (VBA)](Disable_Selection_of_Faces_and_Edges_Using_a_Pre-Notify_Event_Example_VB.htm)
[Disable Selection of Faces and Edges Using a Pre-Notify Event (VB.NET)](Disable_Selection_of_Faces_and_Edges_Using_a_Pre-Notify_Event_Example_VBNET.htm)
[Disable Selection of Faces and Edges Using a Pre-Notify Event (C#)](Disable_Selection_of_Faces_and_Edges_Using_a_Pre-Notify_Event_Example_CSharp.htm)
[Get Preselected Object (C#)](Get_Preselected_Object_Example_CSharp.htm)
[Get Preselected Object (VB.NET)](Get_Preselected_Object_Example_VBNET.htm)
[Get Preselected Object (VBA)](Get_Preselected_Object_Example_VB.htm)

## Remarks

Only selections made interactively fire this event; selections made programmatically are ignored by this event.

If developing a C++ application, use [swPartUserSelectionPreNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
