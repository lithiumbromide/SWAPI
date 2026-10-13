---
title: "FileName Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "FileName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~FileName.html"
---

# FileName Property (IRenderMaterial)

Gets or sets the path and file name (.p2m) of the appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property FileName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.String

instance.FileName = value

value = instance.FileName
```

### C#

```csharp
System.string FileName {get; set;}
```

### C++/CLI

```cpp
property System.String^ FileName {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Path and file name (.p2m) of the appearance

## VBA Syntax

See [RenderMaterial::FileName](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~FileName.html).

## Examples

[Add Decal (VBA)](Add_Decal_Example_VB.htm)
[Add Decal (VB.NET)](Add_Decal_Example_VBNET.htm)
[Add Decal (C#)](Add_Decal_Example_CSharp.htm)
[Get Appearance File Name (C#)](Get_Appearance_Filename_Example_CSharp.htm)
[Get Appearance File Name (VB.NET)](Get_Appearance_Filename_Example_VBNET.htm)
[Get Appearance File Name (VBA)](Get_Appearance_Filename_Example_VB.htm)

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
