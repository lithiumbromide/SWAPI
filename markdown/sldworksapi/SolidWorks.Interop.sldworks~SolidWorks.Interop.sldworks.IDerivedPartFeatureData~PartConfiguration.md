---
title: "PartConfiguration Property (IDerivedPartFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDerivedPartFeatureData"
member: "PartConfiguration"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData~PartConfiguration.html"
---

# PartConfiguration Property (IDerivedPartFeatureData)

Gets or sets the part configuration to use to create the derived part feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property PartConfiguration As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDerivedPartFeatureData
Dim value As System.String

instance.PartConfiguration = value

value = instance.PartConfiguration
```

### C#

```csharp
System.string PartConfiguration {get; set;}
```

### C++/CLI

```cpp
property System.String^ PartConfiguration {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Name of the part configuration to use; Nothing or null to use the Default configuration

## VBA Syntax

See [DerivedPartFeatureData::PartConfiguration](ms-its:sldworksapivb6.chm::/sldworks~DerivedPartFeatureData~PartConfiguration.html).

## See Also

[IDerivedPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData.html)
[IDerivedPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
