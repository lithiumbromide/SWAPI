---
title: "Inverse Method (IMathTransform)"
project: "SOLIDWORKS API Help"
interface: "IMathTransform"
member: "Inverse"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~Inverse.html"
---

# Inverse Method (IMathTransform)

Creates a new math transform by inverting the values in an already existing math transform.

## Syntax

### Visual Basic (Declaration)

```vb
Function Inverse() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMathTransform
Dim value As System.Object

value = instance.Inverse()
```

### C#

```csharp
System.object Inverse()
```

### C++/CLI

```cpp
System.Object^ Inverse();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Math transform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html) or NULL if the operation fails

## VBA Syntax

See [MathTransform::Inverse](ms-its:sldworksapivb6.chm::/sldworks~MathTransform~Inverse.html).

## Examples

[Create Holes Using Hole Wizard and Sketch Points (VBA)](Create_Holes_using_Hole_Wizard_and_Sketch_Points_Example_VB.htm)
[Evaluate Curves Defined in Sketch Space (VBA)](Evaluate_Curves_Defined_in_Sketch_Space_Example_VB.htm)
[Get Names of Sketch Segments (VBA)](Get_Names_of_Sketch_Segments_Example_VB.htm)
[Get x,y,z Locations of Points in Sketch (VBA)](Get_x,y,z_Locations_of_Points_in_Sketch_Example_VB.htm)
[Transform Coordinates from Sketch to Model Space (VBA)](Transform_Coordinates_from_Sketch_to_Model_Space_Example_VB.htm)
[Transform Sketch to Model (VBA)](Transform_Sketch_to_Model_Example_VB.htm)
[Get Points of Repeating Elements in Table-driven Pattern (C#)](Get_Points_of_Repeating_Elements_in_Table-driven_Pattern_Example_CSharp.htm)
[Get Points of Repeating Elements in Table-driven Pattern (VB.NET)](Get_Points_of_Repeating_Elements_in_Table-driven_Pattern_Example_VBNET.htm)
[Get Points of Repeating Elements in Table-driven Pattern (VBA)](Get_Points_of_Repeating_Elements_in_Table-driven_Pattern_Example_VB.htm)

## See Also

[IMathTransform Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.html)
[IMathTransform Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform_members.html)
[IMathTransform::IInverse Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~IInverse.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
