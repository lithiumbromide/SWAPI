---
title: "Layer Property (IFaceHatch)"
project: "SOLIDWORKS API Help"
interface: "IFaceHatch"
member: "Layer"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch~Layer.html"
---

# Layer Property (IFaceHatch)

Gets the drawing layer of the component to which the hatch is attached.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property Layer As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IFaceHatch
Dim value As System.String

instance.Layer = value

value = instance.Layer
```

### C#

```csharp
System.string Layer {get; set;}
```

### C++/CLI

```cpp
property System.String^ Layer {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Layer for the face hatch

## VBA Syntax

See [FaceHatch::Layer](ms-its:sldworksapivb6.chm::/sldworks~FaceHatch~Layer.html).

## Examples

[Get Crosshatches on View (VBA)](Get_Crosshatches_on_View_Example_VB.htm)
[Get Face Hatch Data (C#)](Get_Face_Hatch_Data_Example_CSharp.htm)
[Get Face Hatch Data (VB.NET)](Get_Face_Hatch_Data_Example_VBNET.htm)
[Get Face Hatch Data (VBA)](Get_Face_Hatch_Data_Example_VB.htm)

## See Also

[IFaceHatch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch.html)
[IFaceHatch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
