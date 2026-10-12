---
title: "AddCADFamilyConfiguration Method (IConfigurationManager)"
project: "SOLIDWORKS API Help"
interface: "IConfigurationManager"
member: "AddCADFamilyConfiguration"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~AddCADFamilyConfiguration.html"
---

# AddCADFamilyConfiguration Method (IConfigurationManager)

Adds the specified configuration to [SOLIDWORKS Design connected to the 3DEXPERIENCE platform](ms-its:sldworksapiprogguide.chm:://Overview/SOLIDWORKS_Connected.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddCADFamilyConfiguration( _
   ByVal Name As System.String, _
   ByVal Description As System.String, _
   ByVal IsPhysicalProduct As System.Boolean, _
   ByVal RepresentationParentName As System.String, _
   ByVal ConfigOptions As System.Integer, _
   ByVal ChildCompDisplayOption As System.Integer, _
   ByVal Rebuild As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IConfigurationManager
Dim Name As System.String
Dim Description As System.String
Dim IsPhysicalProduct As System.Boolean
Dim RepresentationParentName As System.String
Dim ConfigOptions As System.Integer
Dim ChildCompDisplayOption As System.Integer
Dim Rebuild As System.Boolean
Dim value As System.Object

value = instance.AddCADFamilyConfiguration(Name, Description, IsPhysicalProduct, RepresentationParentName, ConfigOptions, ChildCompDisplayOption, Rebuild)
```

### C#

```csharp
System.object AddCADFamilyConfiguration(
   System.string Name,
   System.string Description,
   System.bool IsPhysicalProduct,
   System.string RepresentationParentName,
   System.int ConfigOptions,
   System.int ChildCompDisplayOption,
   System.bool Rebuild
)
```

### C++/CLI

```cpp
System.Object^ AddCADFamilyConfiguration(
   System.String^ Name,
   System.String^ Description,
   System.bool IsPhysicalProduct,
   System.String^ RepresentationParentName,
   System.int ConfigOptions,
   System.int ChildCompDisplayOption,
   System.bool Rebuild
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`: Name of the configuration to add
- `Description`: Details about the configuration
- `IsPhysicalProduct`: True to add a parent configuration (Physical Product), false to add a derived configuration (Representation)
- `RepresentationParentName`: Parent Physical Product name of derived configuration (Representation); valid only if IsPhysicalProduct is false
- `ConfigOptions`: Configuration options as defined by [swCADFamilyCfgOptions_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCADFamilyCfgOptions_e.html)
- `ChildCompDisplayOption`: Child component display option as defined in [swChildComponentInBOMOption_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swChildComponentInBOMOption_e.html)
- `Rebuild`: True to rebuild the model after adding this configuration, false to not

### Return Value

[IConfiguration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)

## VBA Syntax

See [ConfigurationManager::AddCADFamilyConfiguration](ms-its:sldworksapivb6.chm::/sldworks~ConfigurationManager~AddCADFamilyConfiguration.html).

## See Also

[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.html)
[IConfigurationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager_members.html)
[IConfiguration::Get3DExperienceType Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~Get3DExperienceType.html)
[IConfiguration::Set3DExperienceType Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~Set3DExperienceType.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
