---
title: "EditConfiguration3 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "EditConfiguration3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditConfiguration3.html"
---

# EditConfiguration3 Method (IModelDoc2)

Edits the specified configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function EditConfiguration3( _
   ByVal Name As System.String, _
   ByVal NewName As System.String, _
   ByVal Comment As System.String, _
   ByVal AlternateName As System.String, _
   ByVal Options As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Name As System.String
Dim NewName As System.String
Dim Comment As System.String
Dim AlternateName As System.String
Dim Options As System.Integer
Dim value As System.Boolean

value = instance.EditConfiguration3(Name, NewName, Comment, AlternateName, Options)
```

### C#

```csharp
System.bool EditConfiguration3(
   System.string Name,
   System.string NewName,
   System.string Comment,
   System.string AlternateName,
   System.int Options
)
```

### C++/CLI

```cpp
System.bool EditConfiguration3(
   System.String^ Name,
   System.String^ NewName,
   System.String^ Comment,
   System.String^ AlternateName,
   System.int Options
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`: Current configuration name
- `NewName`: New configuration name
- `Comment`: Comment used in configuration properties
- `AlternateName`: Alternate configuration name; used if swConfigOption_UseAlternateName is set to True
- `Options`: Combination of one or more BOOLEAN configuration options as defined in [swConfigurationOptions2_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swConfigurationOptions2_e.html) (see **Remarks**)

### Return Value

True if configuration name was changed, false if not

## VBA Syntax

See [ModelDoc2::EditConfiguration3](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~EditConfiguration3.html).

## Remarks

The Options argument can be a combination of any of the following values:

- swConfigOption_SuppressByDefault True if you want to suppress newly added features and mates in this configuration, false if not
- swConfigOption_HideByDefault - True if you want newly added components to be hidden, false if not
- swConfigOption_MinFeatureManager True if you want newly added components to only display their component name in the FeatureManager design tree, false if you want newly added components to display their name and each of their features in the FeatureManager design tree

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::AddConfiguration3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddConfiguration3.html)
[IModelDoc2::DeleteConfiguration2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeleteConfiguration2.html)
[IModelDoc2::GetConfigurationByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetConfigurationByName.html)
[IModelDoc2::GetConfigurationCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetConfigurationCount.html)
[IModelDoc2::GetConfigurationNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetConfigurationNames.html)
[IModelDoc2::IGetConfigurationByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetConfigurationByName.html)
[IModelDoc2::IGetConfigurationNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetConfigurationNames.html)
[IModelDoc2::ShowConfiguration2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ShowConfiguration2.html)
[IModelDoc2::ConfigurationManager Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ConfigurationManager.html)
[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IModelDoc2::IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.html)
[IModelDoc2::IAddConfiguration3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IAddConfiguration3.html)

## Availability

SOLIDWORKS 2001Pus FCS, Revision Number 10.0
