---
title: "Select2 Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "Select2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Select2.html"
---

# Select2 Method (IFeature)

Selects and marks this feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function Select2( _
   ByVal Append As System.Boolean, _
   ByVal Mark As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim Append As System.Boolean
Dim Mark As System.Integer
Dim value As System.Boolean

value = instance.Select2(Append, Mark)
```

### C#

```csharp
System.bool Select2(
   System.bool Append,
   System.int Mark
)
```

### C++/CLI

```cpp
System.bool Select2(
   System.bool Append,
   System.int Mark
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Append`: True appends the feature to the current selection list, false replaces the current selection list
- `Mark`: Value you want to use as a mark; this number is used by functions that require ordered selection

### Return Value

True if the feature was selected, false if not

## VBA Syntax

See [Feature::Select2](ms-its:sldworksapivb6.chm::/sldworks~Feature~Select2.html).

## Examples

[Get Plane or Face for Sketch (VBA)](Get_Plane_or_Face_for_Sketch_Example_VB.htm)
[Insert DXF File and Add Dimension (VBA)](Insert_DXF_File_and_Add_Dimension_Example_VB.htm)
[Traverse Assembly and Hide All Sketches (VBA)](Traverse_Assembly_and_Hide_All_Sketches_Example_VB.htm)
[Suppress Component Feature (C#)](Suppress_Component_Feature_Example_CSharp.htm)
[Suppress Component Feature (VB.NET)](Suppress_Component_Feature_Example_VBNET.htm)
[Suppress Component Feature (VBA)](Suppress_Component_Feature_Example_VB.htm)
[Select Plane (VBA)](Select_Plane_Example_VB.htm)
[Select Plane (VB.NET)](Select_Plane_Example_VBNET.htm)
[Select Plane (C#)](Select_Plane_Example_CSharp.htm)

## Remarks

If an object is already selected with a mark of `x` and you attempt to select the same object again using this method with Append = true and Mark = `y`, then that object remains selected with a mark with `x`. Reselecting a previously selected object does not assign a new mark value.

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::DeSelect Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~DeSelect.html)
[IFeature::GetSpecificFeature2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetSpecificFeature2.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Numbe 10.0
