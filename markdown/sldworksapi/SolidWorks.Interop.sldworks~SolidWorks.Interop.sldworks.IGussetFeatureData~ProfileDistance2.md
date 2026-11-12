---
title: "ProfileDistance2 Property (IGussetFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IGussetFeatureData"
member: "ProfileDistance2"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData~ProfileDistance2.html"
---

# ProfileDistance2 Property (IGussetFeatureData)

Gets or sets the distance for the Profile Distance 2 parameter for this gusset feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ProfileDistance2 As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IGussetFeatureData
Dim value As System.Double

instance.ProfileDistance2 = value

value = instance.ProfileDistance2
```

### C#

```csharp
System.double ProfileDistance2 {get; set;}
```

### C++/CLI

```cpp
property System.double ProfileDistance2 {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Distance

## VBA Syntax

See [GussetFeatureData::ProfileDistance2](ms-its:sldworksapivb6.chm::/sldworks~GussetFeatureData~ProfileDistance2.html).

## See Also

[IGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData.html)
[IGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
