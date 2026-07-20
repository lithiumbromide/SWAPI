---
title: "GetPosition Method (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "GetPosition"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPosition.html"
---

# GetPosition Method (IAnnotation)

Gets the position of this annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPosition() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim value As System.Object

value = instance.GetPosition()
```

### C#

```csharp
System.object GetPosition()
```

### C++/CLI

```cpp
System.Object^ GetPosition();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Return Value

Array of doubles (see**Remarks**)

## VBA Syntax

See

[Annotation::GetPosition](ms-its:sldworksapivb6.chm::/sldworks~Annotation~GetPosition.html)

.

## Examples

[Insert Autoballoons (VBA)](Insert_Autoballoons_Example_VB_AutoBalloon2_VB.htm)

[Traverse Annotations (C#)](Traverse_Annotations_Example_CSharp.htm)

[Traverse Annotations (VB.NET)](Traverse_Annotations_Example_VBNET.htm)

[Traverse Annotations (VBA)](Traverse_Annotations_Example_VB.htm)

## Remarks

The retval is an array of 3 doubles, the x, y, z origin of the annotation.

If this method is not successful in retrieving the position of the annotation in Visual Basic for Applications (VBA), then the VARIANT SafeArray is empty (OLE Automation only), or the status value is S_false (COM only). Make sure that you check this value before using the returned position.

The following table lists the types of annotations that this method supports and the position of the x, y, z origin. In a drawing, the x, y, z origin is relative to the origin of the drawing sheet (the lower-left corner of the sheet).

| Type of Annotation | Position of XYZ Origin |
| --- | --- |
| Datum Feature Symbols | Point where leader hits symbol |
| Datum Target Symbols | Centerpoint of the circle that is attached to the leader |
| Display Dimensions | Point of leader attachment centered on a text box border / center point of bottom border of text box |
| Geometric Tolerances | Upper-left corner of the symbol |
| Notes | Upper-left corner of the text box |
| Surface Finish Symbols | Lower-left point of symbol |
| Table Annotation | Position of x,y,z determined by ITableAnnotation::AnchorType |
| Weld Symbols | Left endpoint of the main horizontal line in the symbol |

If you use this method on any other types of annotations, SOLIDWORKS takes no action and returns false.

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)

[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)

[IAnnotation::IGetPosition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IGetPosition.html)

[IAnnotation::SetPosition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetPosition.html)

[INote::LockPosition Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~LockPosition.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0.
