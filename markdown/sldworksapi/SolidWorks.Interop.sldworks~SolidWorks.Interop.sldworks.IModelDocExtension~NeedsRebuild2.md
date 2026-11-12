---
title: "NeedsRebuild2 Property (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "NeedsRebuild2"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~NeedsRebuild2.html"
---

# NeedsRebuild2 Property (IModelDocExtension)

Gets whether the model document needs to be rebuilt.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property NeedsRebuild2 As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Integer

value = instance.NeedsRebuild2
```

### C#

```csharp
System.int NeedsRebuild2 {get;}
```

### C++/CLI

```cpp
property System.int NeedsRebuild2 {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Rebuild status of model document as defined in [swModelRebuildStatus_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swModelRebuildStatus_e.html)

## VBA Syntax

See [ModelDocExtension::NeedsRebuild2](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~NeedsRebuild2.html).

## Examples

[Move Freeze Bar (C#)](Move_Freeze_Bar_Example_CSharp.htm)
[Move Freeze Bar (VB.NET)](Move_Freeze_Bar_Example_VBNET.htm)
[Move Freeze Bar (VBA)](Move_Freeze_Bar_Example_VB.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDoc2::EditRebuild3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.html)
[IModelDoc2::ForceRebuild3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ForceRebuild3.html)
[IModelDoc2::Rebuild Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Rebuild.html)
[IConfiguration::AddRebuildSaveMark](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddRebuildSaveMark.html)
[IConfiguration::NeedsRebuild](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~NeedsRebuild.html)
[IModelDocExtension::ShowPartRebuildIndicators Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ShowPartRebuildIndicators.html)
[IModelDocExtension::EditRebuildAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~EditRebuildAll.html)
[IModelDocExtension::ForceRebuildAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ForceRebuildAll.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
