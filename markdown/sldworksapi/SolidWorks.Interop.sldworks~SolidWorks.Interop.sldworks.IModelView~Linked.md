---
title: "Linked Property (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "Linked"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Linked.html"
---

# Linked Property (IModelView)

Gets whether or not this viewport is linked or not.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Linked As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim value As System.Boolean

value = instance.Linked
```

### C#

```csharp
System.bool Linked {get;}
```

### C++/CLI

```cpp
property System.bool Linked {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if this viewport is linked, false if not

## VBA Syntax

See [ModelView::Linked](ms-its:sldworksapivb6.chm::/sldworks~ModelView~Linked.html).

## Examples

[Set Viewports (VB.NET)](Set_Viewports_Example_VBNET.htm)
[Set Viewports (VBA)](Set_Viewports_Example_VB.htm)
[Set Viewports (C#)](Set_Viewports_Example_CSharp.htm)

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)
[IModelViewManager::LinkedViews Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~LinkedViews.html)
[IModelViewManager::ViewportDisplay Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~ViewportDisplay.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
