---
title: "OffsetUsed Property (IGussetFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IGussetFeatureData"
member: "OffsetUsed"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData~OffsetUsed.html"
---

# OffsetUsed Property (IGussetFeatureData)

Gets or sets whether offset is used to locate the profile for this gusset feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property OffsetUsed As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IGussetFeatureData
Dim value As System.Boolean

instance.OffsetUsed = value

value = instance.OffsetUsed
```

### C#

```csharp
System.bool OffsetUsed {get; set;}
```

### C++/CLI

```cpp
property System.bool OffsetUsed {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if offset is used, false if not

## VBA Syntax

See [GussetFeatureData::OffsetUsed](ms-its:sldworksapivb6.chm::/sldworks~GussetFeatureData~OffsetUsed.html).

## Examples

[Get Gusset Feature Data (C#)](Get_Gusset_Feature_Data_Example_CSharp.htm)
[Get Gusset Feature Data (VB.NET)](Get_Gusset_Feature_Data_Example_VBNET.htm)
[Get Gusset Feature Data (VBA)](Get_Gusset_Feature_Data_Example_VB.htm)

## See Also

[IGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData.html)
[IGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
