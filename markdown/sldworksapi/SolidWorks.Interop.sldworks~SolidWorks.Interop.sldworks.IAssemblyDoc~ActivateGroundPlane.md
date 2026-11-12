---
title: "ActivateGroundPlane Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "ActivateGroundPlane"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ActivateGroundPlane.html"
---

# ActivateGroundPlane Method (IAssemblyDoc)

Activates the ground plane for the specified configurations.

## Syntax

### Visual Basic (Declaration)

```vb
Function ActivateGroundPlane( _
   ByVal Config_opt As System.Integer, _
   ByVal Config_names As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim Config_opt As System.Integer
Dim Config_names As System.Object
Dim value As System.Boolean

value = instance.ActivateGroundPlane(Config_opt, Config_names)
```

### C#

```csharp
System.bool ActivateGroundPlane(
   System.int Config_opt,
   System.object Config_names
)
```

### C++/CLI

```cpp
System.bool ActivateGroundPlane(
   System.int Config_opt,
   System.Object^ Config_names
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Config_opt`: Configurations in which to activate a ground plane as defined in [swInConfigurationOpts_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swInConfigurationOpts_e.html):

  - swThisConfiguration
  - swAllConfigurations
  - swSpecifyConfiguration
- `Config_names`: Array of configurations in which to activate a ground plane; valid only if Config_opt is set to swInConfiguration_e.swSpecifyConfiguration (see **Remarks**)

### Return Value

True if ground plane successfully activated in the specified configurations, false if not

## VBA Syntax

See [AssemblyDoc::ActivateGroundPlane](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~ActivateGroundPlane.html).

## Examples

[Insert and Activate Ground Plane (VBA)](Insert_Ground_Plane_Example_VB.htm)

## Remarks

To populate config_names, use [IModelDoc2::GetConfigurationNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetConfigurationNames.html).

Before calling this method, use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html) to select the ground plane to activate in the specified configurations.

Only one ground plane can be active at a given time in each assembly configuration.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::GetActiveGroundPlane Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetActiveGroundPlane.html)
[IFeatureManager::InsertGroundPlane Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertGroundPlane.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
