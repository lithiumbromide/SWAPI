---
title: "GetActiveGroundPlane Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "GetActiveGroundPlane"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetActiveGroundPlane.html"
---

# GetActiveGroundPlane Method (IAssemblyDoc)

Gets the active ground plane for the specified configurations.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetActiveGroundPlane( _
   ByVal Config_opt As System.Integer, _
   ByVal Config_names As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim Config_opt As System.Integer
Dim Config_names As System.Object
Dim value As System.Object

value = instance.GetActiveGroundPlane(Config_opt, Config_names)
```

### C#

```csharp
System.object GetActiveGroundPlane(
   System.int Config_opt,
   System.object Config_names
)
```

### C++/CLI

```cpp
System.Object^ GetActiveGroundPlane(
   System.int Config_opt,
   System.Object^ Config_names
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Config_opt`: Configurations from which to retrieve active ground planes as defined in [swInConfigurationOpts_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swInConfigurationOpts_e.html):

  - swThisConfiguration
  - swAllConfigurations
  - swSpecifyConfiguration

  (see **Remarks**)
- `Config_names`: Array of the names of configurations from which to retrieve active ground planes; valid only if Config_opt is set to swInConfiguration_e.swSpecifyConfiguration (see **Remarks**)

### Return Value

Array of ground plane [features](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)

## VBA Syntax

See [AssemblyDoc::GetActiveGroundPlane](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~GetActiveGroundPlane.html).

## Examples

[Insert and Activate Ground Plane (VBA)](Insert_Ground_Plane_Example_VB.htm)

## Remarks

| If Config_opt is set to swInConfiguration_e... | Then the returned array contains one active ground plane or null for... |
| --- | --- |
| swAllConfigurations | Each configuration in the assembly. |
| swSpecifyConfiguration | Each configuration in Config_names. |
| swThisConfiguration | The current configuration. |

To populate config_names, use [IModelDoc2::GetConfigurationNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetConfigurationNames.html).

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::ActivateGroundPlane Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ActivateGroundPlane.html)
[IFeatureManager::InsertGroundPlane Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertGroundPlane.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
