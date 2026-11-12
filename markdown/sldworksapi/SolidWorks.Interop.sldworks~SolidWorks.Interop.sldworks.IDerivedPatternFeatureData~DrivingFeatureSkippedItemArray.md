---
title: "DrivingFeatureSkippedItemArray Property (IDerivedPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDerivedPatternFeatureData"
member: "DrivingFeatureSkippedItemArray"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData~DrivingFeatureSkippedItemArray.html"
---

# DrivingFeatureSkippedItemArray Property (IDerivedPatternFeatureData)

Gets the skipped instances in the driving feature of this derived pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property DrivingFeatureSkippedItemArray As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDerivedPatternFeatureData
Dim value As System.Object

value = instance.DrivingFeatureSkippedItemArray
```

### C#

```csharp
System.object DrivingFeatureSkippedItemArray {get;}
```

### C++/CLI

```cpp
property System.Object^ DrivingFeatureSkippedItemArray {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of longs or integers of the skipped instances in the driving feature

## VBA Syntax

See [DerivedPatternFeatureData::DrivingFeatureSkippedItemArray](ms-its:sldworksapivb6.chm::/sldworks~DerivedPatternFeatureData~DrivingFeatureSkippedItemArray.html).

## Examples

[Get Number of Instances Skipped in Driving Feature (C#)](Get_Number_of_Instances_Skipped_in_Driving_Feature_Example_CSharp.htm)
[Get Number of Instances Skipped in Driving Feature (VB.NET)](Get_Number_of_Instances_Skipped_in_Driving_Feature_Example_VBNET.htm)
[Get Number of Instances Skipped in Driving Feature (VBA)](Get_Number_of_Instances_Skipped_in_Driving_Feature_Example_VB.htm)

## See Also

[IDerivedPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData.html)
[IDerivedPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData_members.html)
[IDerivedPatternFeatureData::PatternFeature Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData~PatternFeature.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
