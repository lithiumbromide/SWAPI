---
title: "EditRebuildAll Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "EditRebuildAll"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~EditRebuildAll.html"
---

# EditRebuildAll Method (IModelDocExtension)

Rebuilds only those features that need to be rebuilt in all configurations without activating each configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function EditRebuildAll() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Boolean

value = instance.EditRebuildAll()
```

### C#

```csharp
System.bool EditRebuildAll()
```

### C++/CLI

```cpp
System.bool EditRebuildAll();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if only those features that need to be rebuilt are rebuilt in all configurations without activating each configuration, false if not

## VBA Syntax

See [ModelDocExtension::EditRebuildAll](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~EditRebuildAll.html).

## Examples

[Rebuild All Configurations Without Activating Each Configuration (C#)](Rebuild_All_Configurations_Without_Activating_Each_Configuration_Example_CSharp.htm)
[Rebuild All Configurations Without Activating Each Configuration (VB.NET)](Rebuild_All_Configurations_Without_Activating_Each_Configuration_Example_VBNET.htm)
[Rebuild All Configurations Without Activating Each Configuration (VBA)](Rebuild_All_Configurations_Without_Activating_Each_Configuration_Example_VB.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::ForceRebuildAll Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ForceRebuildAll.html)
[IModelDocExtension::Rebuild Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Rebuild.html)
[IModelDocExtension::NeedsRebuild2 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~NeedsRebuild2.html)
[IModelDoc2::EditRebuild3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.html)
[IModelDoc2::ForceRebuild3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ForceRebuild3.html)
[IConfiguration::NeedsRebuild Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~NeedsRebuild.html)
[IConfiguration::AddRebuildSaveMark Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddRebuildSaveMark.html)
[IConfigurationManager::AddRebuildSaveMark Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~AddRebuildSaveMark.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
