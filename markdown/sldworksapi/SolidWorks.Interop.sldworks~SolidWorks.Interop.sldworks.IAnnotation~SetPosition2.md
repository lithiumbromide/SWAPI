---
title: "SetPosition2 Method (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "SetPosition2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetPosition2.html"
---

# SetPosition2 Method (IAnnotation)

Sets the position of this annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetPosition2( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Boolean

value = instance.SetPosition2(X, Y, Z)
```

### C#

```csharp
System.bool SetPosition2(
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
System.bool SetPosition2(
   System.double X,
   System.double Y,
   System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`: X coordinate of the origin of the annotation
- `Y`: Y coordinate of the origin of the annotation
- `Z`: Z coordinate of the origin of the annotation

### Return Value

True if the position of the annotation is successfully set, false if not

## VBA Syntax

See [Annotation::SetPosition2](ms-its:sldworksapivb6.chm::/sldworks~Annotation~SetPosition2.html).

## Examples

[Insert a Note (VBA)](Insert_a_Note_Example_VB.htm)
[Insert a Note (VB.NET)](Insert_a_Note_Example_VBNET.htm)
[Insert a Note (C#)](Insert_a_Note_Example_CSharp.htm)
[Traverse Annotations (C#)](Traverse_Annotations_Example_CSharp.htm)
[Traverse Annotations (VB.NET)](Traverse_Annotations_Example_VBNET.htm)
[Traverse Annotations (VBA)](Traverse_Annotations_Example_VB.htm)

## Remarks

The following table lists the types of annotations that this method supports and the position of the x, y, z origin. In a drawing, the x, y, z origin is relative to the origin of the drawing sheet (the lower-left corner of the sheet).

| Type of Annotation | Position of XYZ Origin |
| --- | --- |
| Datum Feature Symbols | Point where leader hits symbol |
| Datum Target Symbols | Center point of the circle that is attached to the leader |
| Display dimensions | Point of leader attachment centered on a text box border / center point of bottom border of text box |
| Geometric Tolerances | Upper-left corner of the symbol |
| Notes | Upper-left corner of the text box |
| Revision Clouds | Position of x,y,z determined by IRevisionCloud::Shape |
| Surface Finish Symbols | Lower-left point of symbol |
| Table Annotations | Position of x,y,z determined by ITableAnnotation::AnchorType |
| Weld Symbols | Left endpoint of the main horizontal line in the symbol |

If you use this method on any other types of annotations, SOLIDWORKS takes no action and returns false.

The position of an annotation can be subject to certain restrictions. These restrictions apply to setting the position through the user interface and using this method. One example of a restriction is a surface-finish symbol that is inserted directly on a face (that is, no leaders). It can only be moved within the borders of that face. If it is inserted directly on an edge, it can only be moved along that edge or extensions of that edge. Datum feature symbols have similar restrictions. If this method attempts to set a position of an annotation that violates any restrictions, the annotation is placed as near as possible to the specified position.

The position of table annotations cannot be set if the table is anchored. Use [ITableAnnotation::Anchored](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITableAnnotation~Anchored.html) to determine if the table is anchored.

| If a dimension has offset text , and you want to move... | Then... |
| --- | --- |
| Dimension text, dimension line, and extension lines | Turn offset text off. Use this method to move the dimension text, dimension line, and extension lines. Turn offset text back on. |
| Dimension text only | Use this method to move the dimension text. The dimension line and extension lines will not move. |

Because radial and diametric dimensions are already attached to the end of a leader, this property is not available for these types of dimensions.

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)
[IAnnotation::GetPosition Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPosition.html)
[INote::LockPosition Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~LockPosition.html)

## Availability

SOLIDWORKS 2014 SP3, Revision Number 22.3
