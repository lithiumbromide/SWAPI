---
title: "ConfigurationOption Property (ICosmeticThreadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICosmeticThreadFeatureData"
member: "ConfigurationOption"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData~ConfigurationOption.html"
---

# ConfigurationOption Property (ICosmeticThreadFeatureData)

Gets or sets the thread configuration option.

## Syntax

### Visual Basic (Declaration)

```vb
Property ConfigurationOption As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmeticThreadFeatureData
Dim value As System.Integer

instance.ConfigurationOption = value

value = instance.ConfigurationOption
```

### C#

```csharp
System.int ConfigurationOption {get; set;}
```

### C++/CLI

```cpp
property System.int ConfigurationOption {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Thread configuration option as defined in [swCosmeticConfigOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCosmeticConfigOptions_e.html)

## VBA Syntax

See [CosmeticThreadFeatureData::ConfigurationOption](ms-its:sldworksapivb6.chm::/sldworks~CosmeticThreadFeatureData~ConfigurationOption.html).

## Examples

See the [ICosmeticThreadFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICosmeticThreadFeatureData.html) examples.

## See Also

[ICosmeticThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData.html)
[ICosmeticThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
