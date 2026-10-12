---
title: "IgnoreMissingFile Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "IgnoreMissingFile"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~IgnoreMissingFile.html"
---

# IgnoreMissingFile Property (IRenderMaterial)

Gets or sets whether to ignore any missing image file warnings.

## Syntax

### Visual Basic (Declaration)

```vb
Property IgnoreMissingFile As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Boolean

instance.IgnoreMissingFile = value

value = instance.IgnoreMissingFile
```

### C#

```csharp
System.bool IgnoreMissingFile {get; set;}
```

### C++/CLI

```cpp
property System.bool IgnoreMissingFile {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to ignore any missing image file warnings, false to not

## VBA Syntax

See [RenderMaterial::IgnoreMissingFile](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~IgnoreMissingFile.html).

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
