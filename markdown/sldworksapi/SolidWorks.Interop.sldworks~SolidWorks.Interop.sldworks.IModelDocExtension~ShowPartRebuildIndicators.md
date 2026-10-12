---
title: "ShowPartRebuildIndicators Property (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "ShowPartRebuildIndicators"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ShowPartRebuildIndicators.html"
---

# ShowPartRebuildIndicators Property (IModelDocExtension)

Gets or sets whether to display rebuild indicators on parts that have out-of-date frozen features.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShowPartRebuildIndicators As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Boolean

instance.ShowPartRebuildIndicators = value

value = instance.ShowPartRebuildIndicators
```

### C#

```csharp
System.bool ShowPartRebuildIndicators {get; set;}
```

### C++/CLI

```cpp
property System.bool ShowPartRebuildIndicators {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to display rebuild indicators, false to not

## VBA Syntax

See [ModelDocExtension::ShowPartRebuildIndicators](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~ShowPartRebuildIndicators.html).

## Examples

[Move Freeze Bar (VBA)](Move_Freeze_Bar_Example_VB.htm)
[Move Freeze Bar (VB.NET)](Move_Freeze_Bar_Example_VBNET.htm)
[Move Freeze Bar (C#)](Move_Freeze_Bar_Example_CSharp.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::NeedsRebuild2 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~NeedsRebuild2.html)
[IFeature::HasFrozenUpdatePending Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~HasFrozenUpdatePending.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
