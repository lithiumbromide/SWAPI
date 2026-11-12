---
title: "InsertSketchPicture2 Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "InsertSketchPicture2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~InsertSketchPicture2.html"
---

# InsertSketchPicture2 Method (ISketchManager)

Inserts a picture on the current drawing sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertSketchPicture2( _
   ByVal FileName As System.String, _
   ByVal HighestResolution As System.Boolean _
) As SketchPicture
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim FileName As System.String
Dim HighestResolution As System.Boolean
Dim value As SketchPicture

value = instance.InsertSketchPicture2(FileName, HighestResolution)
```

### C#

```csharp
SketchPicture InsertSketchPicture2(
   System.string FileName,
   System.bool HighestResolution
)
```

### C++/CLI

```cpp
SketchPicture^ InsertSketchPicture2(
   System.String^ FileName,
   System.bool HighestResolution
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Path to image file including file extension
- `HighestResolution`: True to insert images up to 8192 pixels without compression, false to compress images to 2048 pixels before insertion (see **Remarks**)

### Return Value

[Picture](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPicture.html)

## VBA Syntax

See [SketchManager::InsertSketchPicture2](ms-its:sldworksapivb6.chm::/Sldworks~SketchManager~InsertSketchPicture2.html).

## Examples

[Flip Sketch Picture (VBA)](Flip_Sketch_Picture_Example_VB.htm)
[Flip Sketch Picture (VB.NET)](Flip_Sketch_Picture_Example_VBNET.htm)
[Flip Sketch Picture (C#)](Flip_Sketch_Picture_Example_CSharp.htm)

## Remarks

If the document type is not a drawing, then HighestResolution defaults to false.

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)

## Availability

SOLIDWORKS 2019 SP04, Revision Number 27.4
