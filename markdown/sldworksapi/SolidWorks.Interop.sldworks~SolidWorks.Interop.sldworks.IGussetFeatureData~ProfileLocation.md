---
title: "ProfileLocation Property (IGussetFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IGussetFeatureData"
member: "ProfileLocation"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData~ProfileLocation.html"
---

# ProfileLocation Property (IGussetFeatureData)

Gets or sets where to locate the profile for this gusset feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ProfileLocation As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IGussetFeatureData
Dim value As System.Integer

instance.ProfileLocation = value

value = instance.ProfileLocation
```

### C#

```csharp
System.int ProfileLocation {get; set;}
```

### C++/CLI

```cpp
property System.int ProfileLocation {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Location of profile as defined by [swGussetProfileLocationType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swGussetProfileLocationType_e.html)

## VBA Syntax

See [GussetFeatureData::ProfileLocation](ms-its:sldworksapivb6.chm::/sldworks~GussetFeatureData~ProfileLocation.html).

## See Also

[IGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData.html)
[IGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
