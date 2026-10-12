---
title: "UpAxisFlyout Property (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "UpAxisFlyout"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~UpAxisFlyout.html"
---

# UpAxisFlyout Property (IModelView)

Gets or sets the up axis flyout flag.

## Syntax

### Visual Basic (Declaration)

```vb
Property UpAxisFlyout As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim value As System.Integer

instance.UpAxisFlyout = value

value = instance.UpAxisFlyout
```

### C#

```csharp
System.int UpAxisFlyout {get; set;}
```

### C++/CLI

```cpp
property System.int UpAxisFlyout {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Up axis flyout option as defined by [swViewOrientationUpAxisFlyout_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swViewOrientationUpAxisFlyout_e.html)

## VBA Syntax

See [ModelView::UpAxisFlyout](ms-its:sldworksapivb6.chm::/sldworks~ModelView~UpAxisFlyout.html).

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)

## Availability

SOLIDWORKS 2026 SP01, Revision Number 34.1
