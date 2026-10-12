---
title: "Face Property (IFaceHatch)"
project: "SOLIDWORKS API Help"
interface: "IFaceHatch"
member: "Face"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch~Face.html"
---

# Face Property (IFaceHatch)

Gets the face that is associated with the hatch.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property Face As Face2
```

### Visual Basic (Usage)

```vb
Dim instance As IFaceHatch
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

Pointer to the [face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) associated with the hatch

## VBA Syntax

See [FaceHatch::Face](ms-its:sldworksapivb6.chm::/sldworks~FaceHatch~Face.html).

## Examples

[Get Hatching Data (VBA)](Get_Hatching_Data_Example_VB.htm)

## See Also

[IFaceHatch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch.html)
[IFaceHatch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
