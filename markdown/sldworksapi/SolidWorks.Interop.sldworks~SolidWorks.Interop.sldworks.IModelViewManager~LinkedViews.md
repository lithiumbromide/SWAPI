---
title: "LinkedViews Property (IModelViewManager)"
project: "SOLIDWORKS API Help"
interface: "IModelViewManager"
member: "LinkedViews"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~LinkedViews.html"
---

# LinkedViews Property (IModelViewManager)

Gets or sets whether linking of viewports is enabled in this document.

## Syntax

### Visual Basic (Declaration)

```vb
Property LinkedViews As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelViewManager
Dim value As System.Boolean

instance.LinkedViews = value

value = instance.LinkedViews
```

### C#

```csharp
System.bool LinkedViews {get; set;}
```

### C++/CLI

```cpp
property System.bool LinkedViews {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if linking of viewports is enabled in this document, false if not

## VBA Syntax

See [ModelViewManager::LinkedViews](ms-its:sldworksapivb6.chm::/sldworks~ModelViewManager~LinkedViews.html).

## Examples

[Set Viewports (VB.NET)](Set_Viewports_Example_VBNET.htm)
[Set Viewports (VBA)](Set_Viewports_Example_VB.htm)
[Set Viewports (C#)](Set_Viewports_Example_CSharp.htm)

## See Also

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.html)
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.html)
[IModelView::Linked Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Linked.html)
[IModelViewManager::ViewportDisplay Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~ViewportDisplay.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
