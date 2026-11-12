---
title: "GetAnnotation Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "GetAnnotation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetAnnotation.html"
---

# GetAnnotation Method (IDisplayDimension)

Gets the IAnnotation object for this specific annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAnnotation() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Object

value = instance.GetAnnotation()
```

### C#

```csharp
System.object GetAnnotation()
```

### C++/CLI

```cpp
System.Object^ GetAnnotation();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Annotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)

## VBA Syntax

See [DisplayDimension::GetAnnotation](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~GetAnnotation.html).

## Examples

[Get Dimension Values in Drawing (VBA)](Get_Dimension_Values_in_Drawing_Example_VB.htm)
[Iterate Through Dimensions in Model (VBA)](Iterate_Through_Dimensions_in_Model_Example_VB.htm)
[Unlink Dimensions (VBA)](Unlink_Dimensions_Example_VB.htm)
[Get Annotation Object (VBA)](Get_Annotation_Object_Example_VB.htm)
[Get Annotation Object (VB.NET)](Get_Annotation_Object_Example_VBNET.htm)
[Get Annotation Object (C#)](Get_Annotation_Object_Example_CSharp.htm)
[Traverse Annotations (C#)](Traverse_Annotations_Example_CSharp.htm)
[Traverse Annotations (VB.NET)](Traverse_Annotations_Example_VBNET.htm)
[Traverse Annotations (VBA)](Traverse_Annotations_Example_VB.htm)

## Remarks

The IAnnotation object is a higher-level object that contains methods that are available to all types of annotations.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::IGetAnnotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~IGetAnnotation.html)

## Availability

SOLIDWORKS 99, datecode 1999207
