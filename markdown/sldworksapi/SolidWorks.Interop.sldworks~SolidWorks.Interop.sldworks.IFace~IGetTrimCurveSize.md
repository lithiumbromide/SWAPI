---
title: "IGetTrimCurveSize Method (IFace)"
project: "SOLIDWORKS API Help"
interface: "IFace"
member: "IGetTrimCurveSize"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace~IGetTrimCurveSize.html"
---

# IGetTrimCurveSize Method (IFace)

Obsolete. Superseded by [IFace2::IGetTrimCurveSize2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~IGetTrimCurveSize2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTrimCurveSize( _
   ByVal WantCubic As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFace
Dim WantCubic As System.Boolean
Dim value As System.Integer

value = instance.IGetTrimCurveSize(WantCubic)
```

### C#

```csharp
System.int IGetTrimCurveSize(
   System.bool WantCubic
)
```

### C++/CLI

```cpp
System.int IGetTrimCurveSize(
   System.bool WantCubic
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WantCubic`:

## VBA Syntax

See [Face::IGetTrimCurveSize](ms-its:sldworksapivb6.chm::/sldworks~Face~IGetTrimCurveSize.html).

## See Also

[IFace Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace.html)
[IFace Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace_members.html)
