---
title: "Depth Property (IBrokenOutSectionFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBrokenOutSectionFeatureData"
member: "Depth"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData~Depth.html"
---

# Depth Property (IBrokenOutSectionFeatureData)

Gets or sets the depth of exposure of inner details of the model in the broken-out section feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Depth As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IBrokenOutSectionFeatureData
Dim value As System.Double

instance.Depth = value

value = instance.Depth
```

### C#

```csharp
System.double Depth {get; set;}
```

### C++/CLI

```cpp
property System.double Depth {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Depth exposure of inner details (see **Remarks**)

## VBA Syntax

See [BrokenOutSectionFeatureData::Depth](ms-its:sldworksapivb6.chm::/sldworks~BrokenOutSectionFeatureData~Depth.html).

## Examples

[Get Broken-Out Section Feature Data (C#)](Get_Broken_Out_Section_Feature_Data_Example_CSharp.htm)
[Get Broken-Out Section Feature Data (VB.NET)](Get_Broken_Out_Section_Feature_Data_Example_VBNET.htm)
[Get Broken-Out Section Feature Data (VBA)](Get_Broken_Out_Section_Feature_Data_Example_VB.htm)

## Remarks

Before setting this property, you must set [IBrokenOutSectionFeatureData::EditSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBrokenOutSectionFeatureData~EditSketch.html) to false.

This property is valid only if [IBrokenOutSectionFeatureData::DepthReference](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBrokenOutSectionFeatureData~DepthReference.html) is null and the selection list is empty.

## See Also

[IBrokenOutSectionFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData.html)
[IBrokenOutSectionFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
