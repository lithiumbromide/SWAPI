---
title: "ProfileAngle Property (IGussetFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IGussetFeatureData"
member: "ProfileAngle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData~ProfileAngle.html"
---

# ProfileAngle Property (IGussetFeatureData)

Gets or sets the profile angle for this gusset feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ProfileAngle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IGussetFeatureData
Dim value As System.Double

instance.ProfileAngle = value

value = instance.ProfileAngle
```

### C#

```csharp
System.double ProfileAngle {get; set;}
```

### C++/CLI

```cpp
property System.double ProfileAngle {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Angle

## VBA Syntax

See [GussetFeatureData::ProfileAngle](ms-its:sldworksapivb6.chm::/sldworks~GussetFeatureData~ProfileAngle.html).

## Remarks

[IGussetFeatureData::ProfileType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGussetFeatureData~ProfileType.html) must be set to swGussetProfilePolygon.

## See Also

[IGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData.html)
[IGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
