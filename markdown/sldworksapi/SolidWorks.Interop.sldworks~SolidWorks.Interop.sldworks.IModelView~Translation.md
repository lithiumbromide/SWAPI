---
title: "Translation Property (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "Translation"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Translation.html"
---

# Translation Property (IModelView)

Obsolete. Superseded by [IModelView::Translation3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~Translation3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property Translation As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim value As System.Object

instance.Translation = value

value = instance.Translation
```

### C#

```csharp
System.object Translation {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Translation {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelView::Translation](ms-its:sldworksapivb6.chm::/sldworks~ModelView~Translation.html).

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)
