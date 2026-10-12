---
title: "IGetTrimCurveSize Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "IGetTrimCurveSize"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTrimCurveSize.html"
---

# IGetTrimCurveSize Method (IFace2)

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
Dim instance As IFace2
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

See [Face2::IGetTrimCurveSize](ms-its:sldworksapivb6.chm::/sldworks~Face2~IGetTrimCurveSize.html).

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
