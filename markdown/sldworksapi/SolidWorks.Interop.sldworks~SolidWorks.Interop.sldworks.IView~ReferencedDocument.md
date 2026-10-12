---
title: "ReferencedDocument Property (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "ReferencedDocument"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ReferencedDocument.html"
---

# ReferencedDocument Property (IView)

Gets the document referenced by this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ReferencedDocument As ModelDoc2
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As ModelDoc2

value = instance.ReferencedDocument
```

### C#

```csharp
ModelDoc2 ReferencedDocument {get;}
```

### C++/CLI

```cpp
property ModelDoc2^ ReferencedDocument {
   ModelDoc2^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Model document](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html)

## VBA Syntax

See [View::ReferencedDocument](ms-its:sldworksapivb6.chm::/sldworks~View~ReferencedDocument.html).

## Examples

[Get Document Referenced by Drawing View (VBA)](Get_Document_Referenced_by_Drawing_View_Example_VB.htm)
[Set Body for View (C#)](Set_Body_for_View_Example_CSharp.htm)
[Set Body for View (VB.NET)](Set_Body_for_View_Example_VBNET.htm)
[Set Body for View (VBA)](Set_Body_for_View_Example_VB.htm)

## Remarks

Because section views do not have referenced documents, this method returns an empty string for this type of view. Instead, use [IView::GetBaseView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetBaseView.html) or [IView::IGetBaseView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetBaseView.html) to get the parent view of a section, and then get its referenced document from that view.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::ReferencedConfiguration Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ReferencedConfiguration.html)
[IView::GetReferencedModelName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetReferencedModelName.html)
[IView::ReferencedConfigurationID Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ReferencedConfigurationID.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
