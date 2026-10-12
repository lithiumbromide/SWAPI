---
title: "GetTrimCurves Method (IFace)"
project: "SOLIDWORKS API Help"
interface: "IFace"
member: "GetTrimCurves"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace~GetTrimCurves.html"
---

# GetTrimCurves Method (IFace)

Obsolete. Superseded by [IFace2::GetTrimCurves2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~GetTrimCurves2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTrimCurves( _
   ByVal WantCubic As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFace
Dim WantCubic As System.Boolean
Dim value As System.Object

value = instance.GetTrimCurves(WantCubic)
```

### C#

```csharp
System.object GetTrimCurves(
   System.bool WantCubic
)
```

### C++/CLI

```cpp
System.Object^ GetTrimCurves(
   System.bool WantCubic
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WantCubic`:

## VBA Syntax

See [Face::GetTrimCurves](ms-its:sldworksapivb6.chm::/sldworks~Face~GetTrimCurves.html).

## See Also

[IFace Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace.html)
[IFace Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace_members.html)
