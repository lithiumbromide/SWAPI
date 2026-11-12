---
title: "ProfileDistance3 Property (IGussetFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IGussetFeatureData"
member: "ProfileDistance3"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData~ProfileDistance3.html"
---

# ProfileDistance3 Property (IGussetFeatureData)

Gets or sets the distance for the Profile Distance 3 parameter for this gusset feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ProfileDistance3 As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IGussetFeatureData
Dim value As System.Double

instance.ProfileDistance3 = value

value = instance.ProfileDistance3
```

### C#

```csharp
System.double ProfileDistance3 {get; set;}
```

### C++/CLI

```cpp
property System.double ProfileDistance3 {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Distance

## VBA Syntax

See [GussetFeatureData::ProfileDistance3](ms-its:sldworksapivb6.chm::/sldworks~GussetFeatureData~ProfileDistance3.html).

## Remarks

[IGussetFeatureData::ProfileType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGussetFeatureData~ProfileType.html) must be set to swGussetProfilePolygon.

## See Also

[IGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData.html)
[IGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
