---
title: "IGetTrimCurveSize2 Method (IFace)"
project: "SOLIDWORKS API Help"
interface: "IFace"
member: "IGetTrimCurveSize2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace~IGetTrimCurveSize2.html"
---

# IGetTrimCurveSize2 Method (IFace)

Obsolete. Superseded by [IFace2::IGetTrimCurveSize2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~IGetTrimCurveSize2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTrimCurveSize2( _
   ByVal WantCubic As System.Integer, _
   ByVal WantNRational As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFace
Dim WantCubic As System.Integer
Dim WantNRational As System.Integer
Dim value As System.Integer

value = instance.IGetTrimCurveSize2(WantCubic, WantNRational)
```

### C#

```csharp
System.int IGetTrimCurveSize2(
   System.int WantCubic,
   System.int WantNRational
)
```

### C++/CLI

```cpp
System.int IGetTrimCurveSize2(
   System.int WantCubic,
   System.int WantNRational
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WantCubic`:
- `WantNRational`:

## VBA Syntax

See [Face::IGetTrimCurveSize2](ms-its:sldworksapivb6.chm::/sldworks~Face~IGetTrimCurveSize2.html).

## See Also

[IFace Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace.html)
[IFace Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace_members.html)
