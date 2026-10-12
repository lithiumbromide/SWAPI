---
title: "Value Method (ISwColorContour1)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "ISwColorContour1"
member: "Value"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwColorContour1~Value.html"
---

# Value Method (ISwColorContour1)

Gets the value that is associated with the specified location on the model.

## Syntax

### Visual Basic (Declaration)

```vb
Function Value( _
   ByVal face As System.Object, _
   ByVal vertex_x As System.Single, _
   ByVal vertex_y As System.Single, _
   ByVal vertex_z As System.Single, _
   ByVal normal_x As System.Single, _
   ByVal normal_y As System.Single, _
   ByVal normal_z As System.Single, _
   ByRef Value As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwColorContour1
Dim face As System.Object
Dim vertex_x As System.Single
Dim vertex_y As System.Single
Dim vertex_z As System.Single
Dim normal_x As System.Single
Dim normal_y As System.Single
Dim normal_z As System.Single
Dim Value As System.Double
Dim value As System.Integer

value = instance.Value(face, vertex_x, vertex_y, vertex_z, normal_x, normal_y, normal_z, Value)
```

### C#

```csharp
System.int Value(
   System.object face,
   System.float vertex_x,
   System.float vertex_y,
   System.float vertex_z,
   System.float normal_x,
   System.float normal_y,
   System.float normal_z,
   out System.double Value
)
```

### C++/CLI

```cpp
System.int Value(
   System.Object^ face,
   System.float vertex_x,
   System.float vertex_y,
   System.float vertex_z,
   System.float normal_x,
   System.float normal_y,
   System.float normal_z,
   [Out] System.double Value
)
```

### Parameters

- `face`: Face to color
- `vertex_x`: X coordinate of vertex to color
- `vertex_y`: Y coordinate of vertex to color
- `vertex_z`: Z coordinate of vertex to color
- `normal_x`: X coordinate of normal to color
- `normal_y`: Y coordinate of normal to color
- `normal_z`: Z coordinate of normal to color
- `Value`: Function of the specified face or coordinates of the model (see **Remarks**)

### Return Value

Not used

## VBA Syntax

See [SwColorContour1::Value](ms-its:swpublishedapivb6.chm::/swpublished~SwColorContour1~Value.html).

## Examples

[Custom Colorize a Model Example (C#)](Custom_Colorize_a_Model_Example_CSharp.htm)
[Custom Colorize a Model Example (VB.NET)](Custom_Colorize_a_Model_Example_VBNET.htm)

## Remarks

When you implement this method, you need to populate the Value output parameter. Value can be a function of the specified coordinates or the properties of the face. By default Value is the input parameter for [ISwColorContour1::Color](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwColorContour1~Color.html) and [ISwColorContour1::DisplayString](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwColorContour1~DisplayString.html).

In VB.NET implementations, you need to change the name of the Value output parameter to avoid a compiler error. When you change the name, use the same name for the input parameters of your ISwColorContour1::Color and ISwColorContour1::DisplayString implementations.

## See Also

[ISwColorContour1 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwColorContour1.html)
[ISwColorContour1 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwColorContour1_members.html)

## Availability

SOLIDWORKS 2010 SP05, Revision Number 18.5 and SOLIDWORKS 2011 SP01, Revision Number 19.1
