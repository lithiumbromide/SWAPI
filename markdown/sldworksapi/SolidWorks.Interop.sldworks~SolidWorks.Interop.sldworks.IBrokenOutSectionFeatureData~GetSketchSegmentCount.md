---
title: "GetSketchSegmentCount Method (IBrokenOutSectionFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBrokenOutSectionFeatureData"
member: "GetSketchSegmentCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData~GetSketchSegmentCount.html"
---

# GetSketchSegmentCount Method (IBrokenOutSectionFeatureData)

Gets the number of sketch segments that form the border of this broken-out section feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSketchSegmentCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBrokenOutSectionFeatureData
Dim value As System.Integer

value = instance.GetSketchSegmentCount()
```

### C#

```csharp
System.int GetSketchSegmentCount()
```

### C++/CLI

```cpp
System.int GetSketchSegmentCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of sketch segments

## VBA Syntax

See [BrokenOutSectionFeatureData::GetSketchSegmentCount](ms-its:sldworksapivb6.chm::/sldworks~BrokenOutSectionFeatureData~GetSketchSegmentCount.html).

## Examples

[Get Broken-Out Section Feature Data (VBA)](Get_Broken_Out_Section_Feature_Data_Example_VB.htm)
[Get Broken-Out Section Feature Data (VB.NET)](Get_Broken_Out_Section_Feature_Data_Example_VBNET.htm)
[Get Broken-Out Section Feature Data (C#)](Get_Broken_Out_Section_Feature_Data_Example_CSharp.htm)

## Remarks

Before calling this method you must set [IBrokenOutSectionFeatureData::EditSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBrokenOutSectionFeatureData~EditSketch.html) to true.

Call this method to set the Count parameter of [IBrokenOutSectionFeatureData::IGetSketchSegment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBrokenOutSectionFeatureData~IGetSketchSegment.html).

## See Also

[IBrokenOutSectionFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData.html)
[IBrokenOutSectionFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData_members.html)
[IBrokenOutSectionFeatureData::SketchSegment Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData~SketchSegment.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
