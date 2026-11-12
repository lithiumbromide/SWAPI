---
title: "Scale Property (IFaceHatch)"
project: "SOLIDWORKS API Help"
interface: "IFaceHatch"
member: "Scale"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch~Scale.html"
---

# Scale Property (IFaceHatch)

Obsolete. Superseded by [IFaceHatch::Scale2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFaceHatch~Scale2.html).

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property Scale As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IFaceHatch
Dim value As System.Double

instance.Scale = value

value = instance.Scale
```

### C#

```csharp
System.double Scale {get; set;}
```

### C++/CLI

```cpp
property System.double Scale {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [FaceHatch::Scale](ms-its:sldworksapivb6.chm::/sldworks~FaceHatch~Scale.html).

## See Also

[IFaceHatch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch.html)
[IFaceHatch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch_members.html)
