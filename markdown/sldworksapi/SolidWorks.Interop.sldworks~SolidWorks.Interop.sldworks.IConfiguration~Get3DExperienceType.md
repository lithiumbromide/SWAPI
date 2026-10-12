---
title: "Get3DExperienceType Method (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "Get3DExperienceType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~Get3DExperienceType.html"
---

# Get3DExperienceType Method (IConfiguration)

Gets how this configuration is viewed in [SOLIDWORKS Design connected to the 3DEXPERIENCE platform](ms-its:sldworksapiprogguide.chm:://Overview/SOLIDWORKS_Connected.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Function Get3DExperienceType() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim value As System.Integer

value = instance.Get3DExperienceType()
```

### C#

```csharp
System.int Get3DExperienceType()
```

### C++/CLI

```cpp
System.int Get3DExperienceType();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Type of 3DEXPERIENCE configuration as defined in [sw3DExperienceCfgType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.sw3DExperienceCfgType_e.html)

## VBA Syntax

See [Configuration::Get3DExperienceType](ms-its:sldworksapivb6.chm::/sldworks~Configuration~Get3DExperienceType.html).

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)
[IConfiguration::GetRepresentationParent Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetRepresentationParent.html)
[IConfiguration::Set3DExperienceType Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~Set3DExperienceType.html)
[IConfigurationManager::AddCADFamilyConfiguration Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~AddCADFamilyConfiguration.html)

## Availability

SOLIDWORKS 2020 SP3.1, Revision Number 28.3.1
