---
title: "DisplayMode Property (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "DisplayMode"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~DisplayMode.html"
---

# DisplayMode Property (IModelView)

Gets or sets the display mode for this model view.

## Syntax

### Visual Basic (Declaration)

```vb
Property DisplayMode As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim value As System.Integer

instance.DisplayMode = value

value = instance.DisplayMode
```

### C#

```csharp
System.int DisplayMode {get; set;}
```

### C++/CLI

```cpp
property System.int DisplayMode {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Display mode as defined by [swViewDisplayMode_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swViewDisplayMode_e.html)

## VBA Syntax

See [ModelView::DisplayMode](ms-its:sldworksapivb6.chm::/sldworks~ModelView~DisplayMode.html).

## Examples

[Set Model Display Mode (VBA)](Set_Model_Display_Mode_Example_VB.htm)

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)
[IModelView::StartDynamics Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~StartDynamics.html)
[IModelView::StopDynamics Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~StopDynamics.html)
[IModelView::HlrQuality Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~HlrQuality.html)
[IModelView::DynamicMode Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~DynamicMode.html)

## Availability

SOLIDWORKS 2004 SP1, Revision Number 12.1
