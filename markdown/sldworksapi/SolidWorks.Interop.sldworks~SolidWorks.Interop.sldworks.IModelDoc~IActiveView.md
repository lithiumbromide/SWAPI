---
title: "IActiveView Property (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "IActiveView"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~IActiveView.html"
---

# IActiveView Property (IModelDoc)

Obsolete. Superseded by [IModelDoc2::IActiveView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IActiveView.html).

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property IActiveView As ModelView
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim value As ModelView

value = instance.IActiveView
```

### C#

```csharp
ModelView IActiveView {get;}
```

### C++/CLI

```cpp
property ModelView^ IActiveView {
   ModelView^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDoc::IActiveView](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~IActiveView.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
