---
title: "EditSketch Property (IBrokenOutSectionFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBrokenOutSectionFeatureData"
member: "EditSketch"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData~EditSketch.html"
---

# EditSketch Property (IBrokenOutSectionFeatureData)

Gets or sets whether to place this broken-out section feature in edit sketch mode.

## Syntax

### Visual Basic (Declaration)

```vb
Property EditSketch As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBrokenOutSectionFeatureData
Dim value As System.Boolean

instance.EditSketch = value

value = instance.EditSketch
```

### C#

```csharp
System.bool EditSketch {get; set;}
```

### C++/CLI

```cpp
property System.bool EditSketch {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to place this feature in edit sketch mode, false to not (see **Remarks**)

## VBA Syntax

See [BrokenOutSectionFeatureData::EditSketch](ms-its:sldworksapivb6.chm::/sldworks~BrokenOutSectionFeatureData~EditSketch.html).

## Examples

[Get Broken-Out Section Feature Data (C#)](Get_Broken_Out_Section_Feature_Data_Example_CSharp.htm)
[Get Broken-Out Section Feature Data (VB.NET)](Get_Broken_Out_Section_Feature_Data_Example_VBNET.htm)
[Get Broken-Out Section Feature Data (VBA)](Get_Broken_Out_Section_Feature_Data_Example_VB.htm)

## Remarks

To get the sketch segments that circumscribe this broken-out section feature:

1. Set this property to true.
2. Call [IBrokenOutSectionFeatureData::SketchSegment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBrokenOutSectionFeatureData~SketchSegment.html) or [IBrokenOutSectionFeatureData::IGetSketchSegment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBrokenOutSectionFeatureData~IGetSketchSegment.html).

To set the depth or depth reference for this broken-out section feature:

1. Set this property to false.
2. Call [IBrokenOutSectionFeatureData::Depth](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBrokenOutSectionFeatureData~Depth.html) or [IBrokenOutSectionFeatureData::DepthReference](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBrokenOutSectionFeatureData~DepthReference.html).

## See Also

[IBrokenOutSectionFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData.html)
[IBrokenOutSectionFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
