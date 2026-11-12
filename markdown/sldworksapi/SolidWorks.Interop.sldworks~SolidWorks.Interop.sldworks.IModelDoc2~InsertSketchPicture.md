---
title: "InsertSketchPicture Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertSketchPicture"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSketchPicture.html"
---

# InsertSketchPicture Method (IModelDoc2)

Inserts a picture into the current sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertSketchPicture( _
   ByVal FileName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim FileName As System.String
Dim value As System.Boolean

value = instance.InsertSketchPicture(FileName)
```

### C#

```csharp
System.bool InsertSketchPicture(
   System.string FileName
)
```

### C++/CLI

```cpp
System.bool InsertSketchPicture(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Path to image file including file extension

### Return Value

True if successful, false if not

## VBA Syntax

See [ModelDoc2::InsertSketchPicture](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertSketchPicture.html).

## Remarks

Supported image types are:

- Windows bitmap (*.bmp)
- Tagged Image Format (*.tif)

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::InsertSketchPictureData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSketchPictureData.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
