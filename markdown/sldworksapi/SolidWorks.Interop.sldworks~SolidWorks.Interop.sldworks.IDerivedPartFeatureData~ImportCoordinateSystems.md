---
title: "ImportCoordinateSystems Property (IDerivedPartFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDerivedPartFeatureData"
member: "ImportCoordinateSystems"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData~ImportCoordinateSystems.html"
---

# ImportCoordinateSystems Property (IDerivedPartFeatureData)

Gets or sets whether to import coordinate systems with the derived part feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ImportCoordinateSystems As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDerivedPartFeatureData
Dim value As System.Boolean

instance.ImportCoordinateSystems = value

value = instance.ImportCoordinateSystems
```

### C#

```csharp
System.bool ImportCoordinateSystems {get; set;}
```

### C++/CLI

```cpp
property System.bool ImportCoordinateSystems {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to import its coordinate systems, false to not

## VBA Syntax

See [DerivedPartFeatureData::ImportCoordinateSystems](ms-its:sldworksapivb6.chm::/sldworks~DerivedPartFeatureData~ImportCoordinateSystems.html).

## See Also

[IDerivedPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData.html)
[IDerivedPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
