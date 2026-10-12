---
title: "FrameTop Property (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "FrameTop"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~FrameTop.html"
---

# FrameTop Property (ISldWorks)

Gets or sets the top position of the SOLIDWORKS window.

## Syntax

### Visual Basic (Declaration)

```vb
Property FrameTop As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim value As System.Integer

instance.FrameTop = value

value = instance.FrameTop
```

### C#

```csharp
System.int FrameTop {get; set;}
```

### C++/CLI

```cpp
property System.int FrameTop {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Top position of the SOLIDWORKS window in pixels

## VBA Syntax

See [SldWorks::FrameTop](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~FrameTop.html).

## Examples

**Visual Basic for Applications (VBA)**

Option Explicit

Dim swApp As SldWorks.SldWorks

Sub main()

Set swApp = Application.SldWorks
' Set the SOLIDWORKS window the specified height, width, state, and location
swApp.**FrameHeight** = 500
swApp.**FrameLeft** = 100
swApp.**FrameState** = swWindowNormal
swApp.**FrameTop** = 100
swApp.**FrameWidth** = 500

End Sub

## Remarks

This property is valid only if [ISldWorks::FrameState](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~FrameState.html) is [swWindowState_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWindowState_e.html).swWindowNormal.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::FrameHeight Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~FrameHeight.html)
[ISldWorks::FrameLeft Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~FrameLeft.html)
[ISldWorks::FrameWidth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~FrameWidth.html)
[IModelView::FrameHeight Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~FrameHeight.html)
[IModelView::FrameLeft Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~FrameLeft.html)
[IModelView::FrameState Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~FrameState.html)
[IModelView::FrameTop Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~FrameTop.html)
[IModelView::FrameWidth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~FrameWidth.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
