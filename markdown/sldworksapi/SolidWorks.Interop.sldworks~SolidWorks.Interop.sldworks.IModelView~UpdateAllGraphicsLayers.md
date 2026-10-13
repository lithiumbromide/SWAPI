---
title: "UpdateAllGraphicsLayers Property (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "UpdateAllGraphicsLayers"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~UpdateAllGraphicsLayers.html"
---

# UpdateAllGraphicsLayers Property (IModelView)

Gets or sets whether to update all graphic layers in any mode.

## Syntax

### Visual Basic (Declaration)

```vb
Property UpdateAllGraphicsLayers As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim value As System.Boolean

instance.UpdateAllGraphicsLayers = value

value = instance.UpdateAllGraphicsLayers
```

### C#

```csharp
System.bool UpdateAllGraphicsLayers {get; set;}
```

### C++/CLI

```cpp
property System.bool UpdateAllGraphicsLayers {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to enable all graphic layers in any mode, false to not

## VBA Syntax

See [ModelView::UpdateAllGraphicsLayers](ms-its:sldworksapivb6.chm::/Sldworks~ModelView~UpdateAllGraphicsLayers.html).

## Remarks

SceneGraph organizes contents into layer 0 and 1. Layer 0 contains general geometry, and layer 1 contains sketch geometry. By default this property is set to false, which means only layer 1 is updated when in edit mode. When this property is set to true, then all layers are updated regardless of mode, including edit mode.

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
