---
title: "InsertionPoint Property (ISketchBlockDefinition)"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockDefinition"
member: "InsertionPoint"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~InsertionPoint.html"
---

# InsertionPoint Property (ISketchBlockDefinition)

Gets or sets the insertion point for the block definition.

## Syntax

### Visual Basic (Declaration)

```vb
Property InsertionPoint As MathPoint
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchBlockDefinition
Dim value As MathPoint

instance.InsertionPoint = value

value = instance.InsertionPoint
```

### C#

```csharp
MathPoint InsertionPoint {get; set;}
```

### C++/CLI

```cpp
property MathPoint^ InsertionPoint {
   MathPoint^ get();
   void set (    MathPoint^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Insertion point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) for this block definition

## VBA Syntax

See [SketchBlockDefinition::InsertionPoint](ms-its:sldworksapivb6.chm::/sldworks~SketchBlockDefinition~InsertionPoint.html).

## Examples

[Get and Set Blocks in Any Document (VBA)](Get_and_Set_Blocks_Data_in_Any_Document_Example_VB.htm)

## Remarks

The insertion point of a block definition is the point around which instances of the block rotate or scale. It is the origin of the sketch containing the geometry that is part of the block definition. This implies that the base point of a block definition is always (0,0,0), because the sketch origin is (0,0). Therefore, get version of SketchBlockDefinition::InsertionPoint always returns (0,0,0).

The BlockDefinition::InsertionPoint values are specified relative to the current base point. However, when the insertion point is changed, it must become the sketch origin again, that is, it must become the (0,0,0) point again. So, if you use the this set/put version of this property and then immediately use get version of this property, it returns (0,0,0).

Changing the insertion point does not affect how instances of the block look in a drawing, so when the base point changes, the sketch geometry in the definition is adjusted to allow for that behavior. This means that if you get the block definition sketch and sketch geometry, the sketch geometry coordinates will be different after the insertion point is changed.

## See Also

[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.html)
[ISketchBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition_members.html)
[ISketchBlockInstance::Angle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~Angle.html)
[ISketchBlockInstance::InstancePosition Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~InstancePosition.html)
[ISketchBlockInstance::LockAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~LockAngle.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
