---
title: "UseAngle Property (IGussetFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IGussetFeatureData"
member: "UseAngle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData~UseAngle.html"
---

# UseAngle Property (IGussetFeatureData)

Gets or sets whether an angle is used for specifying the dimensions of the polygonal profile for this gusset feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseAngle As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IGussetFeatureData
Dim value As System.Boolean

instance.UseAngle = value

value = instance.UseAngle
```

### C#

```csharp
System.bool UseAngle {get; set;}
```

### C++/CLI

```cpp
property System.bool UseAngle {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if an angle is used, false if not

## VBA Syntax

See [GussetFeatureData::UseAngle](ms-its:sldworksapivb6.chm::/sldworks~GussetFeatureData~UseAngle.html).

## Remarks

[IGussetFeatureData::ProfileType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGussetFeatureData~ProfileType.html) must be set to swGussetProfilePolygon.

## See Also

[IGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData.html)
[IGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
