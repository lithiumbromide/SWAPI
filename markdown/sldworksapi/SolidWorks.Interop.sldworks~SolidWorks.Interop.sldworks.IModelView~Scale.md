---
title: "Scale Property (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "Scale"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Scale.html"
---

# Scale Property (IModelView)

Obsolete. Superseded by [IModelView::Scale2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~Scale2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property Scale As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim value As System.Double

instance.Scale = value

value = instance.Scale
```

### C#

```csharp
System.double Scale {get; set;}
```

### C++/CLI

```cpp
property System.double Scale {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelView::Scale](ms-its:sldworksapivb6.chm::/sldworks~ModelView~Scale.html).

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)
