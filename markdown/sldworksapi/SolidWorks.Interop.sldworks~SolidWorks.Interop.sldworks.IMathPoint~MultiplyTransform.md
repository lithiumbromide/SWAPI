---
title: "MultiplyTransform Method (IMathPoint)"
project: "SOLIDWORKS API Help"
interface: "IMathPoint"
member: "MultiplyTransform"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~MultiplyTransform.html"
---

# MultiplyTransform Method (IMathPoint)

Multiplies a math point with a math transform; the point is rotated, scaled, and then translated.

## Syntax

### Visual Basic (Declaration)

```vb
Function MultiplyTransform( _
   ByVal TransformObjIn As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMathPoint
Dim TransformObjIn As System.Object
Dim value As System.Object

value = instance.MultiplyTransform(TransformObjIn)
```

### C#

```csharp
System.object MultiplyTransform(
   System.object TransformObjIn
)
```

### C++/CLI

```cpp
System.Object^ MultiplyTransform(
   System.Object^ TransformObjIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TransformObjIn`: Math transform by which to multiply this math point

### Return Value

Newly created translated [math point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) or null if the operation fails

## VBA Syntax

See [MathPoint::MultiplyTransform](ms-its:sldworksapivb6.chm::/sldworks~MathPoint~MultiplyTransform.html).

## Examples

[Dimension Edge in Drawing (VBA)](Dimension_Edge_in_Drawing_Example_VB.htm)
[Evaluate Curves Defined in Sketch Space (VBA)](Evaluate_Curves_Defined_in_Sketch_Space_Example_VB.htm)
[Get Names of Sketch Segments (VBA)](Get_Names_of_Sketch_Segments_Example_VB.htm)
[Transform Coordinates from Sketch to Model Space (VBA)](Transform_Coordinates_from_Sketch_to_Model_Space_Example_VB.htm)
[Transform Sketch to Model (VBA)](Transform_Sketch_to_Model_Example_VB.htm)
[Zoom to Region (VBA)](Zoom_to_Region_Example_VB.htm)
[Get Points of Repeating Elements in Table-driven Pattern (C#)](Get_Points_of_Repeating_Elements_in_Table-driven_Pattern_Example_CSharp.htm)
[Get Points of Repeating Elements in Table-driven Pattern (VB.NET)](Get_Points_of_Repeating_Elements_in_Table-driven_Pattern_Example_VBNET.htm)
[Get Points of Repeating Elements in Table-driven Pattern (VBA)](Get_Points_of_Repeating_Elements_in_Table-driven_Pattern_Example_VB.htm)

## See Also

[IMathPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.html)
[IMathPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint_members.html)
[IMathPoint::IMultiplyTransform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~IMultiplyTransform.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
