---
title: "ConfigurationNames Property (ICosmeticThreadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICosmeticThreadFeatureData"
member: "ConfigurationNames"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData~ConfigurationNames.html"
---

# ConfigurationNames Property (ICosmeticThreadFeatureData)

Gets or sets the thread configuration names.

## Syntax

### Visual Basic (Declaration)

```vb
Property ConfigurationNames As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmeticThreadFeatureData
Dim value As System.Object

instance.ConfigurationNames = value

value = instance.ConfigurationNames
```

### C#

```csharp
System.object ConfigurationNames {get; set;}
```

### C++/CLI

```cpp
property System.Object^ ConfigurationNames {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of configuration names

## VBA Syntax

See [CosmeticThreadFeatureData::ConfigurationNames](ms-its:sldworksapivb6.chm::/sldworks~CosmeticThreadFeatureData~ConfigurationNames.html).

## See Also

[ICosmeticThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData.html)
[ICosmeticThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
