---
title: "DynamicMode Property (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "DynamicMode"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~DynamicMode.html"
---

# DynamicMode Property (IModelView)

Gets the dynamic mode.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property DynamicMode As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim value As System.Integer

value = instance.DynamicMode
```

### C#

```csharp
System.int DynamicMode {get;}
```

### C++/CLI

```cpp
property System.int DynamicMode {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Dynamic mode state as defined in [swDynamicMode_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDynamicMode_e.html)

## VBA Syntax

See [ModelView::DynamicMode](ms-its:sldworksapivb6.chm::/sldworks~ModelView~DynamicMode.html).

## Remarks

If there is no geometry in the part or assembly, then this method returns swNoDynamics regardless of whether spinning, panning, zooming.

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)
[IModelView::StartDynamics Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~StartDynamics.html)
[IModelView::StopDynamics Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~StopDynamics.html)
[IModelView::HlrQuality Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~HlrQuality.html)
