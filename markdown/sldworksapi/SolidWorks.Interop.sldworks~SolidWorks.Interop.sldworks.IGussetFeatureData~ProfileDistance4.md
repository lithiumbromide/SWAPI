---
title: "ProfileDistance4 Property (IGussetFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IGussetFeatureData"
member: "ProfileDistance4"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData~ProfileDistance4.html"
---

# ProfileDistance4 Property (IGussetFeatureData)

Gets or sets the distance for the Profile Distance 4 parameter for this gusset feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ProfileDistance4 As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IGussetFeatureData
Dim value As System.Double

instance.ProfileDistance4 = value

value = instance.ProfileDistance4
```

### C#

```csharp
System.double ProfileDistance4 {get; set;}
```

### C++/CLI

```cpp
property System.double ProfileDistance4 {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Distance

## VBA Syntax

See [GussetFeatureData::ProfileDistance4](ms-its:sldworksapivb6.chm::/sldworks~GussetFeatureData~ProfileDistance4.html).

## Remarks

[IGussetFeatureData::ProfileType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGussetFeatureData~ProfileType.html) must be set to swGussetProfilePolygon.

## See Also

[IGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData.html)
[IGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
