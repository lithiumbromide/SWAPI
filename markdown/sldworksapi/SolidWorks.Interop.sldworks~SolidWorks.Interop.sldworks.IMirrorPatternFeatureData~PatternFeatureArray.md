---
title: "PatternFeatureArray Property (IMirrorPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorPatternFeatureData"
member: "PatternFeatureArray"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~PatternFeatureArray.html"
---

# PatternFeatureArray Property (IMirrorPatternFeatureData)

Gets or sets the seed features to use to create the mirror pattern.

## Syntax

### Visual Basic (Declaration)

```vb
Property PatternFeatureArray As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorPatternFeatureData
Dim value As System.Object

instance.PatternFeatureArray = value

value = instance.PatternFeatureArray
```

### C#

```csharp
System.object PatternFeatureArray {get; set;}
```

### C++/CLI

```cpp
property System.Object^ PatternFeatureArray {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Seed [features](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) on which this pattern feature is based

## VBA Syntax

See [MirrorPatternFeatureData::PatternFeatureArray](ms-its:sldworksapivb6.chm::/sldworks~MirrorPatternFeatureData~PatternFeatureArray.html).

## Examples

[Get Mirror Pattern Feature Data (C#)](Get_Mirror_Pattern_Feature_Data_Example_CSharp.htm)
[Get Mirror Pattern Feature Data (VB.NET)](Get_Mirror_Pattern_Feature_Data_Example_VBNET.htm)
[Get Mirror Pattern Feature Data (VBA)](Get_Mirror_Feature_Data_Example_VB.htm)

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IMirrorPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData.html)
[IMirrorPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData_members.html)
[IMirrorPatternFeatureData::GetPatternFeatureCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~GetPatternFeatureCount.html)
[IMirrorPatternFeatureData::IGetPatternFeatureArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~IGetPatternFeatureArray.html)
[IMirrorPatternFeatureData::ISetPatternFeatureArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~ISetPatternFeatureArray.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
