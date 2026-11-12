---
title: "FlipProfileDistanceParameters Property (IGussetFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IGussetFeatureData"
member: "FlipProfileDistanceParameters"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData~FlipProfileDistanceParameters.html"
---

# FlipProfileDistanceParameters Property (IGussetFeatureData)

Gets or sets whether the Profile Distance 1 and Profile Distance 2 parameters are flipped for this gusset feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property FlipProfileDistanceParameters As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IGussetFeatureData
Dim value As System.Boolean

instance.FlipProfileDistanceParameters = value

value = instance.FlipProfileDistanceParameters
```

### C#

```csharp
System.bool FlipProfileDistanceParameters {get; set;}
```

### C++/CLI

```cpp
property System.bool FlipProfileDistanceParameters {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to flip Profile Distance 1 and Profile Distance 2 parameters, false to not

## VBA Syntax

See [GussetFeatureData::FlipProfileDistanceParameters](ms-its:sldworksapivb6.chm::/sldworks~GussetFeatureData~FlipProfileDistanceParameters.html).

## See Also

[IGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData.html)
[IGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
