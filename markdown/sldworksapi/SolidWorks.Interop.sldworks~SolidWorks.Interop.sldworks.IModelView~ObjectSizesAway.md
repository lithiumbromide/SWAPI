---
title: "ObjectSizesAway Property (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "ObjectSizesAway"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~ObjectSizesAway.html"
---

# ObjectSizesAway Property (IModelView)

Helps define the perspective of the current model view by relating the size of a displayed object with the distance of the object from the observer.

## Syntax

### Visual Basic (Declaration)

```vb
Property ObjectSizesAway As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim value As System.Double

instance.ObjectSizesAway = value

value = instance.ObjectSizesAway
```

### C#

```csharp
System.double ObjectSizesAway {get; set;}
```

### C++/CLI

```cpp
property System.double ObjectSizesAway {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Distance of the object from the observer, relative to the size of the object

## VBA Syntax

See [ModelView::ObjectSizesAway](ms-its:sldworksapivb6.chm::/sldworks~ModelView~ObjectSizesAway.html).

## Remarks

This property controls the same value as the view, display, perspective information dialog box. It gives the ratio of the distance of the object from the observer to the size of the object. The smaller the value, the greater the amount of perspective distortion.

You can only modify or get this property when the current model view has the perspective display enabled. See [IModelView::AddPerspective](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~AddPerspective.html) and [IModelView::RemovePerspective](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~RemovePerspective.html). If perspective display is disabled, getting the property returns -1, and setting the property has no effect.

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)
[IModelView::HasPerspective Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~HasPerspective.html)
