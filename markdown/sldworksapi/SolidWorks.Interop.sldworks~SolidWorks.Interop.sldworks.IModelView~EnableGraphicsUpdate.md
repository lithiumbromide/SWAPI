---
title: "EnableGraphicsUpdate Property (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "EnableGraphicsUpdate"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~EnableGraphicsUpdate.html"
---

# EnableGraphicsUpdate Property (IModelView)

Gets or sets whether or not to refresh the model view.

## Syntax

### Visual Basic (Declaration)

```vb
Property EnableGraphicsUpdate As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim value As System.Boolean

instance.EnableGraphicsUpdate = value

value = instance.EnableGraphicsUpdate
```

### C#

```csharp
System.bool EnableGraphicsUpdate {get; set;}
```

### C++/CLI

```cpp
property System.bool EnableGraphicsUpdate {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to refresh the model view, false to not

## VBA Syntax

See [ModelView::EnableGraphicsUpdate](ms-its:sldworksapivb6.chm::/sldworks~ModelView~EnableGraphicsUpdate.html).

## Remarks

This property affects whether to refresh the model view during a selection, such as [IEntity::Select4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity~Select4.html) or [IFeature::Select2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~Select2.html).

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)

## Availability

SOLIDWORKS 2004 SP3, Revision Number 12.3
