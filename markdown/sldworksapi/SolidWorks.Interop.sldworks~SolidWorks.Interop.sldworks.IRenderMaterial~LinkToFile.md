---
title: "LinkToFile Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "LinkToFile"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~LinkToFile.html"
---

# LinkToFile Property (IRenderMaterial)

Gets or sets whether to link instances of the appearance to an appearance file (.p2m).

## Syntax

### Visual Basic (Declaration)

```vb
Property LinkToFile As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Boolean

instance.LinkToFile = value

value = instance.LinkToFile
```

### C#

```csharp
System.bool LinkToFile {get; set;}
```

### C++/CLI

```cpp
property System.bool LinkToFile {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to link instances of the appearance to an appearance file (.p2m), false to not

## VBA Syntax

See [RenderMaterial::LinkToFile](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~LinkToFile.html).

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
