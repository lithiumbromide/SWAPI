---
title: "Definition Property (IFaceHatch)"
project: "SOLIDWORKS API Help"
interface: "IFaceHatch"
member: "Definition"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch~Definition.html"
---

# Definition Property (IFaceHatch)

Gets the definition for the face hatch.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property Definition As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IFaceHatch
Dim value As System.String

instance.Definition = value

value = instance.Definition
```

### C#

```csharp
System.string Definition {get; set;}
```

### C++/CLI

```cpp
property System.String^ Definition {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Definition for face hatch

## VBA Syntax

See [FaceHatch::Definition](ms-its:sldworksapivb6.chm::/sldworks~FaceHatch~Definition.html).

## Examples

[Get Face Hatch Data (C#)](Get_Face_Hatch_Data_Example_CSharp.htm)
[Get Face Hatch Data (VB.NET)](Get_Face_Hatch_Data_Example_VBNET.htm)
[Get Face Hatch Data (VBA)](Get_Face_Hatch_Data_Example_VB.htm)

## See Also

[IFaceHatch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch.html)
[IFaceHatch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
