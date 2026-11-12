---
title: "GetAnnotation Method (ICenterLine)"
project: "SOLIDWORKS API Help"
interface: "ICenterLine"
member: "GetAnnotation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterLine~GetAnnotation.html"
---

# GetAnnotation Method (ICenterLine)

Gets the general annotation for this centerline.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAnnotation() As Annotation
```

### Visual Basic (Usage)

```vb
Dim instance As ICenterLine
Dim value As Annotation

value = instance.GetAnnotation()
```

### C#

```csharp
Annotation GetAnnotation()
```

### C++/CLI

```cpp
Annotation^ GetAnnotation();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation.html) object

## VBA Syntax

See [CenterLine::GetAnnotation](ms-its:sldworksapivb6.chm::/sldworks~CenterLine~GetAnnotation.html).

## Examples

[Get Centerline Annotation Information (VBA)](Get_Centerline_Annotation_Information_Example_VB.htm)
[Get Annotation Object (VBA)](Get_Annotation_Object_Example_VB.htm)
[Get Annotation Object (VB.NET)](Get_Annotation_Object_Example_VBNET.htm)
[Get Annotation Object (C#)](Get_Annotation_Object_Example_CSharp.htm)
[Get Centerlines in Drawing (C#)](Get_Centerlines_in_Drawing_Example_CSharp.htm)
[Get Centerlines in Drawing (VB.NET)](Get_Centerlines_in_Drawing_Example_VBNET.htm)
[Get Centerlines in Drawing (VBA)](Get_Centerlines_in_Drawing_Example_VB.htm)

## See Also

[ICenterLine Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterLine.html)
[ICenterLine Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterLine_members.html)

## Availability

SOLIDWORKS 2003 SP1, Revision 11.1
