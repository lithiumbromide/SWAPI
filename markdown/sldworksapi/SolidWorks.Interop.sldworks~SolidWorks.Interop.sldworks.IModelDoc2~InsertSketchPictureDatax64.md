---
title: "InsertSketchPictureDatax64 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertSketchPictureDatax64"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSketchPictureDatax64.html"
---

# InsertSketchPictureDatax64 Method (IModelDoc2)

Inserts a picture into the current sketch in 64-bit applications.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertSketchPictureDatax64( _
   ByVal Width As System.Integer, _
   ByVal Height As System.Integer, _
   ByVal PDataIn As System.Long _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Width As System.Integer
Dim Height As System.Integer
Dim PDataIn As System.Long

instance.InsertSketchPictureDatax64(Width, Height, PDataIn)
```

### C#

```csharp
void InsertSketchPictureDatax64(
   System.int Width,
   System.int Height,
   System.long PDataIn
)
```

### C++/CLI

```cpp
void InsertSketchPictureDatax64(
   System.int Width,
   System.int Height,
   System.int64 PDataIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Width`: Width of the image
- `Height`: Height of the image
- `PDataIn`: Pointer to a raw bitmap (HBITMAP) cast as a LONGLONG

## VBA Syntax

See [ModelDoc2::InsertSketchPictureDatax64](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertSketchPictureDatax64.html).

## Remarks

This method is only available through early binding and with 64-bit versions of the SOLIDWORKS Design software.

A copy of the specified bitmap data is created. The SOLIDWORKS Design software does not release your bitmap object.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::InsertSketchPictureData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSketchPictureData.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
