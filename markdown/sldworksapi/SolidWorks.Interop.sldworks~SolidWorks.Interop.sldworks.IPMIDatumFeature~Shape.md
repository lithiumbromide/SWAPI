---
title: "Shape Property (IPMIDatumFeature)"
project: "SOLIDWORKS API Help"
interface: "IPMIDatumFeature"
member: "Shape"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumFeature~Shape.html"
---

# Shape Property (IPMIDatumFeature)

Gets the PMI datum shape.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property Shape As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIDatumFeature
Dim value As System.Integer

instance.Shape = value

value = instance.Shape
```

### C#

```csharp
System.int Shape {get; set;}
```

### C++/CLI

```cpp
property System.int Shape {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

PMI datum shape as defined in [swPMIDatumShape_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPMIDatumShape_e.html)

## VBA Syntax

See [PMIDatumFeature::Shape](ms-its:sldworksapivb6.chm::/sldworks~PMIDatumFeature~Shape.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## See Also

[IPMIDatumFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumFeature.html)
[IPMIDatumFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumFeature_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
