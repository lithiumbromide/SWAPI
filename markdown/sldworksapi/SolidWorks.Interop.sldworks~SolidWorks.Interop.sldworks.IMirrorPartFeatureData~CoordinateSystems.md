---
title: "CoordinateSystems Property (IMirrorPartFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorPartFeatureData"
member: "CoordinateSystems"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData~CoordinateSystems.html"
---

# CoordinateSystems Property (IMirrorPartFeatureData)

Gets or sets whether to import coordinate systems.

## Syntax

### Visual Basic (Declaration)

```vb
Property CoordinateSystems As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorPartFeatureData
Dim value As System.Boolean

instance.CoordinateSystems = value

value = instance.CoordinateSystems
```

### C#

```csharp
System.bool CoordinateSystems {get; set;}
```

### C++/CLI

```cpp
property System.bool CoordinateSystems {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to import coordinate systems, false to not

## VBA Syntax

See [MirrorPartFeatureData::CoordinateSystems](ms-its:sldworksapivb6.chm::/sldworks~MirrorPartFeatureData~CoordinateSystems.html).

## See Also

[IMirrorPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData.html)
[IMirrorPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
