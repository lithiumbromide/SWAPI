---
title: "ProfileType Property (IGussetFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IGussetFeatureData"
member: "ProfileType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData~ProfileType.html"
---

# ProfileType Property (IGussetFeatureData)

Gets or sets the type of profile for this gusset feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ProfileType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IGussetFeatureData
Dim value As System.Integer

instance.ProfileType = value

value = instance.ProfileType
```

### C#

```csharp
System.int ProfileType {get; set;}
```

### C++/CLI

```cpp
property System.int ProfileType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of profile as defined in [swGussetProfileType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swGussetProfileType_e.html)

## VBA Syntax

See [GussetFeatureData::ProfileType](ms-its:sldworksapivb6.chm::/sldworks~GussetFeatureData~ProfileType.html).

## Examples

[Get Gusset Feature Data (C#)](Get_Gusset_Feature_Data_Example_CSharp.htm)
[Get Gusset Feature Data (VB.NET)](Get_Gusset_Feature_Data_Example_VBNET.htm)
[Get Gusset Feature Data (VBA)](Get_Gusset_Feature_Data_Example_VB.htm)

## See Also

[IGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData.html)
[IGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
