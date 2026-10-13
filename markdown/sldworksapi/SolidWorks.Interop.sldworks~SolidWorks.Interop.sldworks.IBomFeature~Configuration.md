---
title: "Configuration Property (IBomFeature)"
project: "SOLIDWORKS API Help"
interface: "IBomFeature"
member: "Configuration"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~Configuration.html"
---

# Configuration Property (IBomFeature)

Gets or sets the name of configuration for this BOM table.

## Syntax

### Visual Basic (Declaration)

```vb
Property Configuration As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IBomFeature
Dim value As System.String

instance.Configuration = value

value = instance.Configuration
```

### C#

```csharp
System.string Configuration {get; set;}
```

### C++/CLI

```cpp
property System.String^ Configuration {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Name of the configuration shown in the BOM table

## VBA Syntax

See [BomFeature::Configuration](ms-its:sldworksapivb6.chm::/sldworks~BomFeature~Configuration.html).

## Examples

See [IBomFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomFeature.html) examples.

## Examples

[Insert BOM Table and BOM Balloon (VB.NET)](Insert_BOM_Table_and_BOM_Balloon_Example_VBNET.htm)
[Insert BOM Table and BOM Balloon (VBA)](Insert_BOM_Table_and_BOM_Balloon_Example_VB.htm)

## Remarks

You can only use this property for BOM tables that show one configuration at a time, such as for parts and indented subassembly style BOM tables.

You cannot use this property for top-level only BOM tables because information on multiple configurations can be shown at once in that style table. In that scenario, getting this property returns an empty string and setting the property has no effect. Use the [IBomFeature::GetConfigurationCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomFeature~GetConfigurationCount.html), [IBomFeature::GetConfigurations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomFeature~GetConfigurations.html), [IBomFeature::IGetConfigurations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomFeature~IGetConfigurations.html), [IBomFeature::SetConfigurations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomFeature~SetConfigurations.html), or [IBomFeature::ISetConfigurations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomFeature~ISetConfigurations.html) for that type of table.

## See Also

[IBomFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.html)
[IBomFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12
