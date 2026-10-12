---
title: "ReferencePart Property (IMotionPlotAxisFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMotionPlotAxisFeatureData"
member: "ReferencePart"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotAxisFeatureData~ReferencePart.html"
---

# ReferencePart Property (IMotionPlotAxisFeatureData)

Gets or sets the result component.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReferencePart As Component2
```

### Visual Basic (Usage)

```vb
Dim instance As IMotionPlotAxisFeatureData
Dim value As Component2

instance.ReferencePart = value

value = instance.ReferencePart
```

### C#

```csharp
Component2 ReferencePart {get; set;}
```

### C++/CLI

```cpp
property Component2^ ReferencePart {
   Component2^ get();
   void set (    Component2^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Result [component](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html)

## VBA Syntax

See [MotionPlotAxisFeatureData::ReferencePart](ms-its:sldworksapivb6.chm::/sldworks~MotionPlotAxisFeatureData~ReferencePart.html).

## Remarks

A component is one of the vector elements. To define a vector, you need to specify a coordinate frame. You can select a part or a subassembly to define the vector with regards to the origin coordinate system of the selected part or subassembly. If nothing is selected, then the top assembly's coordinate system is used to define the vector.

## See Also

[IMotionPlotAxisFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotAxisFeatureData.html)
[IMotionPlotAxisFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotAxisFeatureData_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
