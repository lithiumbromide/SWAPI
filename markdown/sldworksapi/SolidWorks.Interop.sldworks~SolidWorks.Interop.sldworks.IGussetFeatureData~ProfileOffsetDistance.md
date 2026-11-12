---
title: "ProfileOffsetDistance Property (IGussetFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IGussetFeatureData"
member: "ProfileOffsetDistance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData~ProfileOffsetDistance.html"
---

# ProfileOffsetDistance Property (IGussetFeatureData)

Gets or sets the offset distance of the profile for this gusset feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ProfileOffsetDistance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IGussetFeatureData
Dim value As System.Double

instance.ProfileOffsetDistance = value

value = instance.ProfileOffsetDistance
```

### C#

```csharp
System.double ProfileOffsetDistance {get; set;}
```

### C++/CLI

```cpp
property System.double ProfileOffsetDistance {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Distance

## VBA Syntax

See [GussetFeatureData::ProfileOffsetDistance](ms-its:sldworksapivb6.chm::/sldworks~GussetFeatureData~ProfileOffsetDistance.html).

## Examples

[Get Gusset Feature Data (C#)](Get_Gusset_Feature_Data_Example_CSharp.htm)
[Get Gusset Feature Data (VB.NET)](Get_Gusset_Feature_Data_Example_VBNET.htm)
[Get Gusset Feature Data (VBA)](Get_Gusset_Feature_Data_Example_VB.htm)

## Remarks

[IGussetFeatureData::OffsetUsed](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGussetFeatureData~OffsetUsed.html) must be set to True.

## See Also

[IGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData.html)
[IGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
