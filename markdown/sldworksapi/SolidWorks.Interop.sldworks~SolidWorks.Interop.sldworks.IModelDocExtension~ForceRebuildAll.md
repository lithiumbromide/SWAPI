---
title: "ForceRebuildAll Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "ForceRebuildAll"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ForceRebuildAll.html"
---

# ForceRebuildAll Method (IModelDocExtension)

Forces a rebuild of all features in all configurations without activating each configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function ForceRebuildAll() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Boolean

value = instance.ForceRebuildAll()
```

### C#

```csharp
System.bool ForceRebuildAll()
```

### C++/CLI

```cpp
System.bool ForceRebuildAll();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if all features in all configurations are rebuilt without activating each configuration, false if not

## VBA Syntax

See [ModelDocExtension::ForceRebuildAll](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~ForceRebuildAll.html).

## Examples

[Rebuild All Features in All Configurations (C#)](Rebuild_All_Features_in_All_Configurations_Example_CSharp.htm)
[Rebuild All Features in All Configurations (VB.NET)](Rebuild_All_Features_in_All_Configurations_Example_VBNET.htm)
[Rebuild All Features in All Configurations (VBA)](Rebuild_All_Features_in_All_Configurations_Example_VB.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::EditRebuildAll Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~EditRebuildAll.html)
[IModelDocExtension::Rebuild Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Rebuild.html)
[IModelDocExtension::NeedsRebuild2 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~NeedsRebuild2.html)
[IModelDoc2::EditRebuild3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.html)
[IModelDoc2::ForceRebuild3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ForceRebuild3.html)
[IConfiguration::NeedsRebuild Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~NeedsRebuild.html)
[IConfiguration::AddRebuildSaveMark Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddRebuildSaveMark.html)
[IConfigurationManager::AddRebuildSaveMark Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~AddRebuildSaveMark.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
