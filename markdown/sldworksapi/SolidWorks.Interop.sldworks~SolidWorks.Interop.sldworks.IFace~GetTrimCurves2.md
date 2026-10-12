---
title: "GetTrimCurves2 Method (IFace)"
project: "SOLIDWORKS API Help"
interface: "IFace"
member: "GetTrimCurves2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace~GetTrimCurves2.html"
---

# GetTrimCurves2 Method (IFace)

Obsolete. Superseded by [IFace2::GetTrimCurves2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~GetTrimCurves2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTrimCurves2( _
   ByVal WantCubic As System.Boolean, _
   ByVal WantNRational As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFace
Dim WantCubic As System.Boolean
Dim WantNRational As System.Boolean
Dim value As System.Object

value = instance.GetTrimCurves2(WantCubic, WantNRational)
```

### C#

```csharp
System.object GetTrimCurves2(
   System.bool WantCubic,
   System.bool WantNRational
)
```

### C++/CLI

```cpp
System.Object^ GetTrimCurves2(
   System.bool WantCubic,
   System.bool WantNRational
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WantCubic`:
- `WantNRational`:

## VBA Syntax

See [Face::GetTrimCurves2](ms-its:sldworksapivb6.chm::/sldworks~Face~GetTrimCurves2.html).

## See Also

[IFace Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace.html)
[IFace Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace_members.html)
