---
title: "IActiveView Property (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "IActiveView"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IActiveView.html"
---

# IActiveView Property (IModelDoc2)

Gets the current active model view in read-only mode.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property IActiveView As ModelView
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
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

### Property Value

Current active [model view](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView.html) in this document

## VBA Syntax

See [ModelDoc2::IActiveView](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~IActiveView.html).

## Examples

[Access Assembly (C++)](Access_Assembly_Example_CPlusPlus_COM.htm)
[Dynamic View Rotation (C++)](Dynamic_View_Rotation_Example_CPlusPlus_COM.htm)

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::ActiveView Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ActiveView.html)
[IModelDoc2::EnumModelViews Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EnumModelViews.html)
[IModelDoc2::GetFirstModelView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetFirstModelView.html)
[IModelDoc2::IGetFirstModelView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetFirstModelView.html)
[IModelView::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetNext.html)
[IModelView::IGetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~IGetNext.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
