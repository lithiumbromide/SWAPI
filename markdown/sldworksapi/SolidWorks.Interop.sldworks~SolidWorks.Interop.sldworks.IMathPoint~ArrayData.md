---
title: "ArrayData Property (IMathPoint)"
project: "SOLIDWORKS API Help"
interface: "IMathPoint"
member: "ArrayData"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~ArrayData.html"
---

# ArrayData Property (IMathPoint)

Gets or sets the array of x,y,z coordinates that describe this math point.

## Syntax

### Visual Basic (Declaration)

```vb
Property ArrayData As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMathPoint
Dim value As System.Object

instance.ArrayData = value

value = instance.ArrayData
```

### C#

```csharp
System.object ArrayData {get; set;}
```

### C++/CLI

```cpp
property System.Object^ ArrayData {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of 3 doubles representing the x,y,z coordinates of the math point

## VBA Syntax

See [MathPoint::ArrayData](ms-its:sldworksapivb6.chm::/sldworks~MathPoint~ArrayData.html).

## Examples

[Dimension Edge in Drawing (VBA)](Dimension_Edge_in_Drawing_Example_VB.htm)
[Get Names of Sketch Segments (VBA)](Get_Names_of_Sketch_Segments_Example_VB.htm)
[Get Reference Point Data (VBA)](Get_Reference_Point_Data_Example_VB.htm)
[Insert Reference Points (VBA)](Insert_Reference_Points_Example_VB.htm)
[Transform Sketch to Model (VBA)](Transform_Sketch_to_Model_Example_VB.htm)
[Get Points of Repeating Elements in Table-driven Pattern (C#)](Get_Points_of_Repeating_Elements_in_Table-driven_Pattern_Example_CSharp.htm)
[Get Points of Repeating Elements in Table-driven Pattern (VB.NET)](Get_Points_of_Repeating_Elements_in_Table-driven_Pattern_Example_VBNET.htm)
[Get Points of Repeating Elements in Table-driven Pattern (VBA)](Get_Points_of_Repeating_Elements_in_Table-driven_Pattern_Example_VB.htm)
[Get Coordinates of the Plane's Bounding Box (C#)](Get_Coordinates_of_the_Plane's_Bounding_Box_Example_CSharp.htm)
[Get Coordinates of the Plane's Bounding Box (VB.NET)](Get_Coordinates_of_the_Plane's_Bounding_Box_Example_VBNET.htm)
[Get Coordinates of the Plane's Bounding Box (VBA)](Get_Coordinates_of_the_Plane's_Bounding_Box_Example_VB.htm)

## See Also

[IMathPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.html)
[IMathPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint_members.html)
[IMathPoint::IArrayData Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~IArrayData.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
