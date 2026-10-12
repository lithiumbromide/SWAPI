---
title: "Entities Property (IMotionPlotAxisFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMotionPlotAxisFeatureData"
member: "Entities"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotAxisFeatureData~Entities.html"
---

# Entities Property (IMotionPlotAxisFeatureData)

Gets or sets the entities whose motion you want to measure.

## Syntax

### Visual Basic (Declaration)

```vb
Property Entities As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMotionPlotAxisFeatureData
Dim value As System.Object

instance.Entities = value

value = instance.Entities
```

### C#

```csharp
System.object Entities {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Entities {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of [entities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity.html) to measure

## VBA Syntax

See [MotionPlotAxisFeatureData::Entities](ms-its:sldworksapivb6.chm::/sldworks~MotionPlotAxisFeatureData~Entities.html).

## Examples

[Create Plots and Get Values (C#)](Create_Plots_and_Get_Values_Example_CSharp.htm)
[Create Plots and Get Values (VB.NET)](Create_Plots_and_Get_Values_Example_VBNET.htm)
[Create Plots and Get Values (VBA)](Create_Plots_and_Get_Values_Example_VB.htm)

## Remarks

See the SOLIDWORKS Motion Studies Help for details about which entities can be measured.

## See Also

[IMotionPlotAxisFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotAxisFeatureData.html)
[IMotionPlotAxisFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotAxisFeatureData_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
