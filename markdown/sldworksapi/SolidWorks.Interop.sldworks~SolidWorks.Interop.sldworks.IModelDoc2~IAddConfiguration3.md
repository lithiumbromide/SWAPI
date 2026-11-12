---
title: "IAddConfiguration3 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "IAddConfiguration3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IAddConfiguration3.html"
---

# IAddConfiguration3 Method (IModelDoc2)

Adds a new configuration to this model document.

## Syntax

### Visual Basic (Declaration)

```vb
Function IAddConfiguration3( _
   ByVal Name As System.String, _
   ByVal Comment As System.String, _
   ByVal AlternateName As System.String, _
   ByVal Options As System.Integer _
) As Configuration
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Name As System.String
Dim Comment As System.String
Dim AlternateName As System.String
Dim Options As System.Integer
Dim value As Configuration

value = instance.IAddConfiguration3(Name, Comment, AlternateName, Options)
```

### C#

```csharp
Configuration IAddConfiguration3(
   System.string Name,
   System.string Comment,
   System.string AlternateName,
   System.int Options
)
```

### C++/CLI

```cpp
Configuration^ IAddConfiguration3(
   System.String^ Name,
   System.String^ Comment,
   System.String^ AlternateName,
   System.int Options
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`: Name of the new configuration
- `Comment`: Comment displayed in Configuration Properties
- `AlternateName`: Alternate configuration name; used if swConfigOption_UseAlternateName is set to True
- `Options`: Combination of one or more BOOLEAN configuration options as defined in [swConfigurationOptions2_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swConfigurationOptions2_e.html) (see **Remarks**)

## VBA Syntax

See [ModelDoc2::IAddConfiguration3](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~IAddConfiguration3.html).

## Remarks

The Options argument can be a combination of any of the following values:

- swConfigOption_SuppressByDefault True if you want to suppress newly added features and mates in this configuration, false if not
- swConfigOption_HideByDefault - True if you want newly added components to be hidden, false if not
- swConfigOption_MinFeatureManager True if you want newly added components to only display their component name in the FeatureManager design tree, false if you want newly added components to display their name and each of their features in the FeatureManager design tree
- swConfigOption_DontActivate - True if you do not want the new configuration activated, false if not

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::GetConfigurationByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetConfigurationByName.html)
[IModelDoc2::GetConfigurationCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetConfigurationCount.html)
[IModelDoc2::GetConfigurationNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetConfigurationNames.html)
[IModelDoc2::IGetConfigurationByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetConfigurationByName.html)
[IModelDoc2::IGetCustomInfoNames2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetCustomInfoNames2.html)
[IModelDoc2::AddConfiguration3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddConfiguration3.html)
[IModelDoc2::ShowConfiguration2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ShowConfiguration2.html)
[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
