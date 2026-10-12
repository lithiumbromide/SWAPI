---
title: "NeedsRebuild Property (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "NeedsRebuild"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~NeedsRebuild.html"
---

# NeedsRebuild Property (IConfiguration)

Gets whether the configuration needs to be rebuilt.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property NeedsRebuild As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim value As System.Boolean

value = instance.NeedsRebuild
```

### C#

```csharp
System.bool NeedsRebuild {get;}
```

### C++/CLI

```cpp
property System.bool NeedsRebuild {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the configuration needs to be rebuilt, false if not

## VBA Syntax

See [Configuration::NeedsRebuild](ms-its:sldworksapivb6.chm::/sldworks~Configuration~NeedsRebuild.html).

## Examples

[Are the Assembly Configurations Loaded (C#)](Are_the_Assembly_Configurations_Loaded_Example_CSharp.htm)
[Are the Assembly Configurations Loaded (VB.NET)](Are_the_Assembly_Configurations_Loaded_Example_VBNET.htm)
[Are the Assembly Configurations Loaded (VBA)](Are_the_Assembly_Configurations_Loaded_Example_VB.htm)

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)
[IModelDocExtension::NeedsRebuild2 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~NeedsRebuild2.html)
[IConfiguration::AddRebuildSaveMark Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddRebuildSaveMark.html)
[IModelDocExtension::EditRebuildAll Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~EditRebuildAll.html)
[IModelDocExtension::ForceRebuildAll Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ForceRebuildAll.html)
[IModelDoc2::EditRebuild3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.html)
[IModelDoc2::ForceRebuild3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ForceRebuild3.html)

## Availability

SOLIDWORKS 2010 SP3, Revision Number 18.3
