---
title: "UseMaterialHatch Property (IFaceHatch)"
project: "SOLIDWORKS API Help"
interface: "IFaceHatch"
member: "UseMaterialHatch"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch~UseMaterialHatch.html"
---

# UseMaterialHatch Property (IFaceHatch)

Gets or sets whether this face hatch uses material crosshatch.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseMaterialHatch As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFaceHatch
Dim value As System.Boolean

instance.UseMaterialHatch = value

value = instance.UseMaterialHatch
```

### C#

```csharp
System.bool UseMaterialHatch {get; set;}
```

### C++/CLI

```cpp
property System.bool UseMaterialHatch {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use material crosshatch, false to not

## VBA Syntax

See [FaceHatch::UseMaterialHatch](ms-its:sldworksapivb6.chm::/sldworks~FaceHatch~UseMaterialHatch.html).

## Examples

[Get Face Hatch Data (C#)](Get_Face_Hatch_Data_Example_CSharp.htm)
[Get Face Hatch Data (VB.NET)](Get_Face_Hatch_Data_Example_VBNET.htm)
[Get Face Hatch Data (VBA)](Get_Face_Hatch_Data_Example_VB.htm)

## Remarks

Material crosshatches are valid for [section views](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrSection.html) and aligned section views only.

## See Also

[IFaceHatch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch.html)
[IFaceHatch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch_members.html)

## Availability

SOLIDWORKS 2009 SP4, Revision Number 17.4
