---
title: "Type Property (ISketchPoint)"
project: "SOLIDWORKS API Help"
interface: "ISketchPoint"
member: "Type"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~Type.html"
---

# Type Property (ISketchPoint)

Gets or sets the type of sketch point.

## Syntax

### Visual Basic (Declaration)

```vb
Property Type As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPoint
Dim value As System.Integer

instance.Type = value

value = instance.Type
```

### C#

```csharp
System.int Type {get; set;}
```

### C++/CLI

```cpp
property System.int Type {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of sketch point as defined in [swSketchPointType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSketchPointType_e.html)

## VBA Syntax

See [SketchPoint::Type](ms-its:sldworksapivb6.chm::/sldworks~SketchPoint~Type.html).

## Examples

[Get Persistent Identifiers and Types for Sketch Points (VBA)](Get_Persistent_Identifiers_and_Type_for_Sketch_Points_Example_VB.htm)
[Get Persistent Identifiers and Types for Sketch Points (VB.NET)](Get_Persistent_Identifiers_and_Types_for_Sketch_Points_Example_VBNET.htm)
[Get Persistent Identifiers and Types for Sketch Points (C#)](Get_Persistent_Identifiers_and_Types_for_Sketch_Points_Example_CSharp.htm)

## Remarks

Sketch slot information is independent of the sketch point type.

## See Also

[ISketchPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.html)
[ISketchPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
