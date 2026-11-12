---
title: "Visible Property (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "Visible"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Visible.html"
---

# Visible Property (IComponent2)

Gets or sets the visibility state of this component.

## Syntax

### Visual Basic (Declaration)

```vb
Property Visible As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.Integer

instance.Visible = value

value = instance.Visible
```

### C#

```csharp
System.int Visible {get; set;}
```

### C++/CLI

```cpp
property System.int Visible {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Visibility state as defined in [swComponentVisibilityState_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swComponentVisibilityState_e.html)

## VBA Syntax

See [Component2::Visible](ms-its:sldworksapivb6.chm::/sldworks~Component2~Visible.html).

## Examples

[Open Assembly in Large Design Review Mode (C#)](Open_Assembly_in_Large_Design_Review_Mode_Example_CSharp.htm)
[Open Assembly in Large Design Review Mode (VB.NET)](Open_Assembly_in_Large_Design_Review_Mode_Example_VBNET.htm)
[Open Assembly in Large Design Review Mode (VBA)](Open_Assembly_in_Large_Design_Review_Mode_Example_VB.htm)

## Remarks

This functionality is also available using [IModelDoc2::HideComponent2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~HideComponent2.html) and [IModelDoc2::ShowComponent2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ShowComponent2.html).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IAssemblyDoc::ISetComponentVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ISetComponentVisibility.html)
[IAssemblyDoc::SetComponentVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetComponentVisibility.html)
[IComponent2::GetVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetVisibility.html)
[IComponent2::IGetVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetVisibility.html)
[IComponent2::ISetVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ISetVisibility.html)
[IComponent2::SetVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetVisibility.html)
[IComponent2::IsHidden Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsHidden.html)
[IAssemblyDoc::CompConfigProperties5 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CompConfigProperties5.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
