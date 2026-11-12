---
title: "SolidFill Property (IFaceHatch)"
project: "SOLIDWORKS API Help"
interface: "IFaceHatch"
member: "SolidFill"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch~SolidFill.html"
---

# SolidFill Property (IFaceHatch)

Gets whether the face hatch is a solid color.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property SolidFill As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFaceHatch
Dim value As System.Boolean

instance.SolidFill = value

value = instance.SolidFill
```

### C#

```csharp
System.bool SolidFill {get; set;}
```

### C++/CLI

```cpp
property System.bool SolidFill {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if face hatch is a solid color, false if not

## VBA Syntax

See [FaceHatch::SolidFill](ms-its:sldworksapivb6.chm::/sldworks~FaceHatch~SolidFill.html).

## Examples

[Get Crosshatches on the View (VBA)](Get_Crosshatches_on_View_Example_VB.htm)
[Get Face Hatch Data (C#)](Get_Face_Hatch_Data_Example_CSharp.htm)
[Get Face Hatch Data (VB.NET)](Get_Face_Hatch_Data_Example_VBNET.htm)
[Get Face Hatch Data (VBA)](Get_Face_Hatch_Data_Example_VB.htm)

## See Also

[IFaceHatch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch.html)
[IFaceHatch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision number 11.0
