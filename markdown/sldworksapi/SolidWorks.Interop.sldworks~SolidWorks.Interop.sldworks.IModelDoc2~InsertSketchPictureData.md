---
title: "InsertSketchPictureData Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertSketchPictureData"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSketchPictureData.html"
---

# InsertSketchPictureData Method (IModelDoc2)

Obsolete. Superseded by [IModelDoc2::InsertSketchPictureDatax64](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSketchPictureDatax64.html).

This method is unsafe to use with 64-bit SOLIDWORKS, i.e. all versions since SOLIDWORKS 2016.

The 32-bit integer returned may be to small to contain the 64-bit window handle/pointer, and will be truncated silently. A critical exception will occur sometime later, when the truncated handle/pointer is used.

Inserts a picture into the current sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertSketchPictureData( _
   ByVal Width As System.Short, _
   ByVal Height As System.Short, _
   ByVal PDataIn As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Width As System.Short
Dim Height As System.Short
Dim PDataIn As System.Integer

instance.InsertSketchPictureData(Width, Height, PDataIn)
```

### C#

```csharp
void InsertSketchPictureData(
   System.short Width,
   System.short Height,
   System.int PDataIn
)
```

### C++/CLI

```cpp
void InsertSketchPictureData(
   System.short Width,
   System.short Height,
   System.int PDataIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Width`: Width of the image
- `Height`: Height of the image
- `PDataIn`: Pointer to a raw bitmap (HBITMAP) cast as a long

## VBA Syntax

See [ModelDoc2::InsertSketchPictureData](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertSketchPictureData.html).

## Remarks

**All applications are required to be compatible with SOLIDWORKS x64. You must replace all calls to 32-bit only APIs with calls to their 64-bit safe counterparts.**

See [Eliminating 32-bit only API use](sldworksapiprogguide.chm::/Overview/Eliminating_32-Bit_Only_API_Use.htm) for more information.

A copy of the specified bitmap data is created. The SOLIDWORKS Design software does not release your bitmap object.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::InsertSketchPicture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSketchPicture.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
