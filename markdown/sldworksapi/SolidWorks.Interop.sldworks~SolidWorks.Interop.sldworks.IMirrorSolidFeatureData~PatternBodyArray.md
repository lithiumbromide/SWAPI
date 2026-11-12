---
title: "PatternBodyArray Property (IMirrorSolidFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorSolidFeatureData"
member: "PatternBodyArray"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData~PatternBodyArray.html"
---

# PatternBodyArray Property (IMirrorSolidFeatureData)

Gets or sets the seed bodies to pattern for this mirror solid feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property PatternBodyArray As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorSolidFeatureData
Dim value As System.Object

instance.PatternBodyArray = value

value = instance.PatternBodyArray
```

### C#

```csharp
System.object PatternBodyArray {get; set;}
```

### C++/CLI

```cpp
property System.Object^ PatternBodyArray {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of seed [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) to pattern

## VBA Syntax

See [MirrorSolidFeatureData::PatternBodyArray](ms-its:sldworksapivb6.chm::/sldworks~MirrorSolidFeatureData~PatternBodyArray.html).

## Examples

[Get Mirror Solid Feature Data (C#)](Get_Mirror_Solid_Feature_Data_Example_CSharp.htm)
[Get Mirror Solid Feature Data (VB.NET)](Get_Mirror_Solid_Feature_Data_Example_VBNET.htm)
[Get Mirror Solid Feature Data (VBA)](Get_Mirror_Solid_Data_Example_VB.htm)

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IMirrorSolidFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData.html)
[IMirrorSolidFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData_members.html)
[IMirrorSolidFeatureData::GetPatternBodyCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData~GetPatternBodyCount.html)
[IMirrorSolidFeatureData::IGetPatternBodyArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData~IGetPatternBodyArray.html)
[IMirrorSolidFeatureData::ISetPatternBodyArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData~ISetPatternBodyArray.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
