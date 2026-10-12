---
title: "AddComponentConfiguration Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "AddComponentConfiguration"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddComponentConfiguration.html"
---

# AddComponentConfiguration Method (IAssemblyDoc)

Adds a new configuration for the last selected assembly component.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddComponentConfiguration( _
   ByVal Name As System.String, _
   ByVal Comment As System.String, _
   ByVal AlternateName As System.String, _
   ByVal Options As System.Integer _
) As Configuration
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim Name As System.String
Dim Comment As System.String
Dim AlternateName As System.String
Dim Options As System.Integer
Dim value As Configuration

value = instance.AddComponentConfiguration(Name, Comment, AlternateName, Options)
```

### C#

```csharp
Configuration AddComponentConfiguration(
   System.string Name,
   System.string Comment,
   System.string AlternateName,
   System.int Options
)
```

### C++/CLI

```cpp
Configuration^ AddComponentConfiguration(
   System.String^ Name,
   System.String^ Comment,
   System.String^ AlternateName,
   System.int Options
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`: Name of new configuration
- `Comment`: Comment displayed in Configuration Properties
- `AlternateName`: Alternate configuration name; used if swConfigOption_UseAlternateName is set to true (see **Remarks**)
- `Options`: Combination of one or more BOOLEAN configuration options as defined in [swConfigurationOptions2_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swConfigurationOptions2_e.html) (see Remarks)

### Return Value

[IConfiguration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration.html)

## VBA Syntax

See [AssemblyDoc::AddComponentConfiguration](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~AddComponentConfiguration.html).

## Remarks

The Options argument can be a combination of any of the following values:

- swConfigOption_SuppressByDefault True if you want to suppress newly added features and mates in this configuration, false if not
- swConfigOption_HideByDefault - True if you want newly added components to be hidden, false if not
- swConfigOption_MinFeatureManager True if you want newly added components to only display their component name in the FeatureManager design tree, false if you want newly added components to display their name and each of their features in the FeatureManager design tree
- swConfigOption_DontActivate - True if you do not want the new configuration activated, false if not

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13
