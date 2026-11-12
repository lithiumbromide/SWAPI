---
title: "Component Property (IMotionPlotAxisFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMotionPlotAxisFeatureData"
member: "Component"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotAxisFeatureData~Component.html"
---

# Component Property (IMotionPlotAxisFeatureData)

Gets or sets the component of the result vector quantity.

## Syntax

### Visual Basic (Declaration)

```vb
Property Component As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMotionPlotAxisFeatureData
Dim value As System.Integer

instance.Component = value

value = instance.Component
```

### C#

```csharp
System.int Component {get; set;}
```

### C++/CLI

```cpp
property System.int Component {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Component of the result vector quantity as defined in [swMotionPlotAxisComponent_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMotionPlotAxisComponent_e.html)

## VBA Syntax

See [MotionPlotAxisFeatureData::Component](ms-its:sldworksapivb6.chm::/sldworks~MotionPlotAxisFeatureData~Component.html).

## Examples

[Create Plots and Get Values (C#)](Create_Plots_and_Get_Values_Example_CSharp.htm)
[Create Plots and Get Values (VB.NET)](Create_Plots_and_Get_Values_Example_VBNET.htm)
[Create Plots and Get Values (VBA)](Create_Plots_and_Get_Values_Example_VB.htm)

## Remarks

Some motion study results, such as linear displacement/velocity results, are a 3D vector where x, y, and z can be the component of the quantity. For example, if you want the x component of the result vector, then set this property to swMotionPlotAxisComponent_X.

## See Also

[IMotionPlotAxisFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotAxisFeatureData.html)
[IMotionPlotAxisFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotAxisFeatureData_members.html)
[IMotionPlotAxisFeatureData::ReferencePart Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotAxisFeatureData~ReferencePart.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
