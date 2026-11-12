---
title: "Face Property (IWrapSketchFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IWrapSketchFeatureData"
member: "Face"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWrapSketchFeatureData~Face.html"
---

# Face Property (IWrapSketchFeatureData)

Gets where this face was applied for this wrap feature or sets the face where to apply this wrap feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Face As Face2
```

### Visual Basic (Usage)

```vb
Dim instance As IWrapSketchFeatureData
Dim value As Face2

instance.Face = value

value = instance.Face
```

### C#

```csharp
Face2 Face {get; set;}
```

### C++/CLI

```cpp
property Face2^ Face {
   Face2^ get();
   void set (    Face2^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

## VBA Syntax

See [WrapSketchFeatureData::Face](ms-its:sldworksapivb6.chm::/sldworks~WrapSketchFeatureData~Face.html).

## Examples

[Change Wrap Feature Face (C#)](Change_Wrap_Feature_Face_Example_CSharp.htm)
[Change Wrap Feature Face (VB.NET)](Change_Wrap_Feature_Face_Example_VBNET.htm)
[Change Wrap Feature Face (VBA)](Change_Wrap_Feature_Face_Example_VB.htm)

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IWrapSketchFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWrapSketchFeatureData.html)
[IWrapSketchFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWrapSketchFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
