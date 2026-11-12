---
title: "SketchSegment Property (IBrokenOutSectionFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBrokenOutSectionFeatureData"
member: "SketchSegment"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData~SketchSegment.html"
---

# SketchSegment Property (IBrokenOutSectionFeatureData)

Gets the sketch segments that form the border of this broken-out section feature.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property SketchSegment As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBrokenOutSectionFeatureData
Dim value As System.Object

value = instance.SketchSegment
```

### C#

```csharp
System.object SketchSegment {get;}
```

### C++/CLI

```cpp
property System.Object^ SketchSegment {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of [ISketchSegment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html)s

## VBA Syntax

See [BrokenOutSectionFeatureData::SketchSegment](ms-its:sldworksapivb6.chm::/sldworks~BrokenOutSectionFeatureData~SketchSegment.html).

## Examples

[Get Broken-Out Section Feature Data (VBA)](Get_Broken_Out_Section_Feature_Data_Example_VB.htm)
[Get Broken-Out Section Feature Data (VB.NET)](Get_Broken_Out_Section_Feature_Data_Example_VBNET.htm)
[Get Broken-Out Section Feature Data (C#)](Get_Broken_Out_Section_Feature_Data_Example_CSharp.htm)

## Remarks

To get the sketch segments that form the border of this broken-out section feature:

1. Set the property [IBrokenOutSectionFeatureData::EditSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBrokenOutSectionFeatureData~EditSketch.html) to true.
2. Call this property.

## See Also

[IBrokenOutSectionFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData.html)
[IBrokenOutSectionFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData_members.html)
[IBrokenOutSectionFeatureData::GetSketchSegmentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData~GetSketchSegmentCount.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
