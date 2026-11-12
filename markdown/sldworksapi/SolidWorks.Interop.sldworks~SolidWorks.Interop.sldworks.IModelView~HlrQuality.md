---
title: "HlrQuality Property (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "HlrQuality"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~HlrQuality.html"
---

# HlrQuality Property (IModelView)

Gets or sets the hidden-line removal quality property of this model view.

## Syntax

### Visual Basic (Declaration)

```vb
Property HlrQuality As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim value As System.Integer

instance.HlrQuality = value

value = instance.HlrQuality
```

### C#

```csharp
System.int HlrQuality {get; set;}
```

### C++/CLI

```cpp
property System.int HlrQuality {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of HLR done as defined in [swHlrQuality_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swHlrQuality_e.html)

## VBA Syntax

See [ModelView::HlrQuality](ms-its:sldworksapivb6.chm::/sldworks~ModelView~HlrQuality.html).

## Examples

[Get and Set Model View HLR Quality (VBA)](Get_and_Set_Model_View_HLR_Quality_Example_VB.htm)
[Get and Set Model View HLR Quality (VB.NET)](Get_and_Set_Model_View_HLR_Quality_Example_VBNET.htm)
[Get and Set Model View HLR Quality (C#)](Get_and_Set_Model_View_HLR_Quality_Example_CSharp.htm)

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)
[IModelView::DynamicMode Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~DynamicMode.html)
[IModelView::DisplayMode Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~DisplayMode.html)
[IModelView::StopDynamics Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~StopDynamics.html)
[IModelView::StartDynamics Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~StartDynamics.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
