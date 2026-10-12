---
title: "DDrawingDocEvents_DynamicHighlightNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DDrawingDocEvents_DynamicHighlightNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_DynamicHighlightNotifyEventHandler.html"
---

# DDrawingDocEvents_DynamicHighlightNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Post-notifies the application when dynamic highlighting of the selected object changes from on to off, and vice versa.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DDrawingDocEvents_DynamicHighlightNotifyEventHandler( _
   ByVal bHighlightState As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DDrawingDocEvents_DynamicHighlightNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DDrawingDocEvents_DynamicHighlightNotifyEventHandler(
   System.bool bHighlightState
)
```

### C++/CLI

```cpp
public delegate System.int DDrawingDocEvents_DynamicHighlightNotifyEventHandler(
   System.bool bHighlightState
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `bHighlightState`: True if highlighting is on, false if it is off

## VBA Syntax

See [DynamicHighlightNotify Event (DrawingDoc)](ms-its:sldworksapivb6.chm::/SldWorks~DrawingDoc~DynamicHighlightNotify_EV.html).

## Examples

```vb
Private Function drawdoc_DynamicHighlightNotify() As Long
Dim one As Object
Dim x As Integer
Dim pt As Variant
Set one = mgr.GetSelectedObject5(-1)
If Not one Is Nothing Then
    Debug.Print mgr.GetSelectedObjectType2(-1)
    one.Select True

    pt = mgr.GetSelectionPoint(-1)
    If Not IsEmpty(pt) Then
        Debug.Print pt(0), pt(1), pt(2)
    Else
        Debug.Print "Object selected in FeatureManager design tree, so no points."
    End If
Else
    Debug.Print "Dynamic highlighting is now off."
End If
```

## Remarks

To send this notification, specify -1 for the index for any of the [ISelectionMgr](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr.html) methods. See **Example**.

If developing a C++ application, use [swDrawingDynamicHighlightNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
