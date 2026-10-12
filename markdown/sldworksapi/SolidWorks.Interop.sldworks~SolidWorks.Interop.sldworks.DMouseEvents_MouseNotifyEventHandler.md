---
title: "DMouseEvents_MouseNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DMouseEvents_MouseNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DMouseEvents_MouseNotifyEventHandler.html"
---

# DMouseEvents_MouseNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired whenever a mouse event occurs.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DMouseEvents_MouseNotifyEventHandler( _
   ByVal Message As System.Integer, _
   ByVal WParam As System.Integer, _
   ByVal LParam As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DMouseEvents_MouseNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DMouseEvents_MouseNotifyEventHandler(
   System.int Message,
   System.int WParam,
   System.int LParam
)
```

### C++/CLI

```cpp
public delegate System.int DMouseEvents_MouseNotifyEventHandler(
   System.int Message,
   System.int WParam,
   System.int LParam
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Message`: Message to be sent
- `WParam`: Additional message_dependent information
- `LParam`: X, Y in a packed long requiring unpacking; see GET_X_LPARAM and GET_Y_LPARAM in MSDN for details on how to unpack LParam

## VBA Syntax

See [MouseNotify Event (Mouse)](ms-its:sldworksapivb6.chm::/SldWorks~Mouse~MouseNotify_EV.html).

## Examples

The following sample code shows a possible approach to decoding WParam and LParam.

```vb
'--------------------------------------------------------------
void NotifyHandler( UINT message, WPARAM wParam, LPARAM lParam)
{
long x = GET_X_LPARAM(lParam);//Uses Windows macro
long y = GET_Y_LPARAM(lParam);//Uses Windows macro

switch(message)
{
case WM_MOUSEWHEEL:
case WM_MOUSEMOVE:
//Your code to process event
break;
case WM_LBUTTONDOWN:
//Your code to process event
break;
case WM_LBUTTONUP:
//Your code to process event
break;
case WM_RBUTTONDOWN:
//Your code to process event
break;
case WM_RBUTTONUP:
//Your code to process event
break;
case WM_MBUTTONDOWN:
//Your code to process event
break;
case WM_MBUTTONUP:
//Your code to process event
break;
case WM_LBUTTONDBLCLK:
//Your code to process event
break;
case WM_RBUTTONDBLCLK:
//Your code to process event
break;
case WM_MBUTTONDBLCLK:
//Your code to process event
break;
}
}
```

## Remarks

If developing a C++ application, use [swMouseNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMouseNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
