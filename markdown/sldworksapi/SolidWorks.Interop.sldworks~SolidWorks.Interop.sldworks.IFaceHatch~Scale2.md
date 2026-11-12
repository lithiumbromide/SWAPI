---
title: "Scale2 Property (IFaceHatch)"
project: "SOLIDWORKS API Help"
interface: "IFaceHatch"
member: "Scale2"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch~Scale2.html"
---

# Scale2 Property (IFaceHatch)

Gets or sets the scale for this face hatch.

## Syntax

### Visual Basic (Declaration)

```vb
Property Scale2 As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IFaceHatch
Dim value As System.Double

instance.Scale2 = value

value = instance.Scale2
```

### C#

```csharp
System.double Scale2 {get; set;}
```

### C++/CLI

```cpp
property System.double Scale2 {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Scale for this face hatch

## VBA Syntax

See [FaceHatch::Scale2](ms-its:sldworksapivb6.chm::/sldworks~FaceHatch~Scale2.html).

## Examples

[Get Crosshatches on View (VBA)](Get_Crosshatches_on_View_Example_VB.htm)
[Get Face Hatch Data (C#)](Get_Face_Hatch_Data_Example_CSharp.htm)
[Get Face Hatch Data (VB.NET)](Get_Face_Hatch_Data_Example_VBNET.htm)
[Get Face Hatch Data (VBA)](Get_Face_Hatch_Data_Example_VB.htm)

## See Also

[IFaceHatch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch.html)
[IFaceHatch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch_members.html)

## Availability

SOLIDWORKS 2003 SP2, Revision Number 11.2
