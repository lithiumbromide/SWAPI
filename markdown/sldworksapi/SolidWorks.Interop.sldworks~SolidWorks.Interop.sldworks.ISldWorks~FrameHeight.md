---
title: "FrameHeight Property (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "FrameHeight"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~FrameHeight.html"
---

# FrameHeight Property (ISldWorks)

Get or sets the height of the SOLIDWORKS window.

## Syntax

### Visual Basic (Declaration)

```vb
Property FrameHeight As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim value As System.Integer

instance.FrameHeight = value

value = instance.FrameHeight
```

### C#

```csharp
System.int FrameHeight {get; set;}
```

### C++/CLI

```cpp
property System.int FrameHeight {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Height of the SOLIDWORKS window in pixels

## VBA Syntax

See [SldWorks::FrameHeight](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~FrameHeight.html).

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
[ISldWorks::FrameLeft Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~FrameLeft.html)
[ISldWorks::FrameTop Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~FrameTop.html)
[ISldWorks::FrameWidth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~FrameWidth.html)
[IModelView::FrameHeight Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~FrameHeight.html)
[IModelView::FrameLeft Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~FrameLeft.html)
[IModelView::FrameState Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~FrameState.html)
[IModelView::FrameTop Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~FrameTop.html)
[IModelView::FrameWidth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~FrameWidth.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
