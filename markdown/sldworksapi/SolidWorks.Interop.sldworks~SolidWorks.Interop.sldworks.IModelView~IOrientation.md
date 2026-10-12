---
title: "IOrientation Property (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "IOrientation"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~IOrientation.html"
---

# IOrientation Property (IModelView)

Obsolete. Superseded by [IModelView::Orientation3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~Orientation3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property IOrientation As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim value As System.Double

instance.IOrientation = value

value = instance.IOrientation
```

### C#

```csharp
System.double IOrientation {get; set;}
```

### C++/CLI

```cpp
property System.double IOrientation {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelView::IOrientation](ms-its:sldworksapivb6.chm::/sldworks~ModelView~IOrientation.html).

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)
