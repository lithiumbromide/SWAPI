---
title: "GetTrimCurves Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "GetTrimCurves"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTrimCurves.html"
---

# GetTrimCurves Method (IFace2)

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
Dim instance As IFace2
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

See [Face2::GetTrimCurves](ms-its:sldworksapivb6.chm::/sldworks~Face2~GetTrimCurves.html).

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
