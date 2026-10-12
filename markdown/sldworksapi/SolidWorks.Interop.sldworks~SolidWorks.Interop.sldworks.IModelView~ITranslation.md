---
title: "ITranslation Property (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "ITranslation"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~ITranslation.html"
---

# ITranslation Property (IModelView)

Obsolete. Superseded by [IModelView::Translation3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~Translation3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property ITranslation As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim value As System.Double

instance.ITranslation = value

value = instance.ITranslation
```

### C#

```csharp
System.double ITranslation {get; set;}
```

### C++/CLI

```cpp
property System.double ITranslation {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelView::ITranslation](ms-its:sldworksapivb6.chm::/sldworks~ModelView~ITranslation.html).

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)
