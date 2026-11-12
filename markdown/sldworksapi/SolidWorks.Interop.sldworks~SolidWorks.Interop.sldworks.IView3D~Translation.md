---
title: "Translation Property (IView3D)"
project: "SOLIDWORKS API Help"
interface: "IView3D"
member: "Translation"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D~Translation.html"
---

# Translation Property (IView3D)

Gets or sets the translation vector of this 3D View.

## Syntax

### Visual Basic (Declaration)

```vb
Property Translation As MathVector
```

### Visual Basic (Usage)

```vb
Dim instance As IView3D
Dim value As MathVector

instance.Translation = value

value = instance.Translation
```

### C#

```csharp
MathVector Translation {get; set;}
```

### C++/CLI

```cpp
property MathVector^ Translation {
   MathVector^ get();
   void set (    MathVector^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Translation [vector](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html)

## VBA Syntax

See [View3D::Translation](ms-its:sldworksapivb6.chm::/sldworks~View3D~Translation.html).

## See Also

[IView3D Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D.html)
[IView3D Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
