---
title: "ViewportDisplay Property (IModelViewManager)"
project: "SOLIDWORKS API Help"
interface: "IModelViewManager"
member: "ViewportDisplay"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~ViewportDisplay.html"
---

# ViewportDisplay Property (IModelViewManager)

Sets the model's viewport arrangement.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property ViewportDisplay As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelViewManager

instance.ViewportDisplay = value
```

### C#

```csharp
System.int ViewportDisplay {set;}
```

### C++/CLI

```cpp
property System.int ViewportDisplay {
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Viewport arrangement as defined by [swViewportDisplay_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swViewportDisplay_e.html)

## VBA Syntax

See [ModelViewManager::ViewportDisplay](ms-its:sldworksapivb6.chm::/sldworks~ModelViewManager~LinkedViews.html).

## Examples

[Set Viewports (VB.NET)](Set_Viewports_Example_VBNET.htm)
[Set Viewports (VBA)](Set_Viewports_Example_VB.htm)
[Set Viewports (C#)](Set_Viewports_Example_CSharp.htm)

## See Also

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.html)
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.html)
[IModelViewManager::LinkedViews Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~LinkedViews.html)
[IModelView::Linked Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Linked.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
