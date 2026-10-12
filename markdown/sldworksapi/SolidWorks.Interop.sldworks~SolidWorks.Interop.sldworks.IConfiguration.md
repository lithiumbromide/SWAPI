---
title: "IConfiguration Interface"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html"
---

# IConfiguration Interface

Allows you to manage different part or assembly states.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IConfiguration
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
```

### C#

```csharp
public interface IConfiguration
```

### C++/CLI

```cpp
public interface class IConfiguration
```

## VBA Syntax

See [Configuration](ms-its:sldworksapivb6.chm::/sldworks~Configuration.html).

## Examples

[Add Derived Configurations (VBA)](Add_Derived_Configurations_Example_VB.htm)
[Traverse Assembly at Component and Feature Levels Using Recursion (VBA)](Traverse_Assembly_at_Component_and_Feature_Levels_Using_Recursion_Example_VB.htm)
[Traverse Assembly at Component and Feature Levels Using Recursion (VB.NET)](Traverse_Assembly_at_Component_and_Feature_Levels_Using_Recursion_Example_VBNET.htm)
[Traverse Assembly at Component and Feature Levels Using Recursion (C#)](Traverse_Assembly_at_Component_and_Feature_Levels_Using_Recursion_Example_CSharp.htm)

## Remarks

You can hide or suppress features on a part and save that state as a configuration. In an assembly, you can hide or suppress assembly-level features or assembly components and save each state as a configuration.

## Accessors

[IAssemblyDoc::AddComponentConfiguration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~AddComponentConfiguration.html)

[IConfiguration::GetChildren](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~GetChildren.html) and [IConfiguration::IGetChildren](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~IGetChildren.html)

[IConfiguration::GetParent](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~GetParent.html)

[IConfigurationManager::ActiveConfiguration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfigurationManager~ActiveConfiguration.html)

[IConfigurationManager::AddCADFamilyConfiguration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~AddCADFamilyConfiguration.html)

[IConfigurationManager::AddConfiguration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfigurationManager~AddConfiguration.html)

[IModelDoc2::AddConfiguration3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~AddConfiguration3.html) and [IModelDoc2::IAddConfiguration3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IAddConfiguration3.html)

[IModelDoc2::GetConfigurationByName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetConfigurationByName.html) and [IModelDoc2::IGetConfigurationByName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IGetConfigurationByName.html)

## Access Diagram

[Configuration](SWObjectModel.pdf#Configuration)

## See Also

[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
