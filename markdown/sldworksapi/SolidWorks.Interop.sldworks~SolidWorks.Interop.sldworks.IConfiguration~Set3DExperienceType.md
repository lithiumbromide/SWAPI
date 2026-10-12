---
title: "Set3DExperienceType Method (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "Set3DExperienceType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~Set3DExperienceType.html"
---

# Set3DExperienceType Method (IConfiguration)

Converts this configuration in [SOLIDWORKS Design connected to the 3DEXPERIENCE platform](ms-its:sldworksapiprogguide.chm:://Overview/SOLIDWORKS_Connected.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Function Set3DExperienceType( _
   ByVal IsPhysicalProduct As System.Boolean, _
   ByVal RepresentationParentName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim IsPhysicalProduct As System.Boolean
Dim RepresentationParentName As System.String
Dim value As System.Boolean

value = instance.Set3DExperienceType(IsPhysicalProduct, RepresentationParentName)
```

### C#

```csharp
System.bool Set3DExperienceType(
   System.bool IsPhysicalProduct,
   System.string RepresentationParentName
)
```

### C++/CLI

```cpp
System.bool Set3DExperienceType(
   System.bool IsPhysicalProduct,
   System.String^ RepresentationParentName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `IsPhysicalProduct`: True to convert this configuration to a parent configuration (Physical Product/Family), false to convert it to a derived configuration (Representation)
- `RepresentationParentName`: Parent Physical Product/Family name of derived configuration (Representation); valid only if IsPhysicalProduct is false

### Return Value

True if configuration successfully converted, false if not

## VBA Syntax

See [Configuration::Set3DExperienceType](ms-its:sldworksapivb6.chm::/sldworks~Configuration~Set3DExperienceType.html).

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)
[IConfiguration::Get3DExperienceType Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~Get3DExperienceType.html)
[IConfiguration::AddCADFamilyConfiguration Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~AddCADFamilyConfiguration.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
