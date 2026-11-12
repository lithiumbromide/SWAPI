---
title: "ICreateTrimmedSheet2 Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "ICreateTrimmedSheet2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~ICreateTrimmedSheet2.html"
---

# ICreateTrimmedSheet2 Method (ISurface)

Obsolete. Superseded by [ISurface::ICreateTrimmedSheet4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~ICreateTrimmedSheet4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateTrimmedSheet2( _
   ByVal NCurves As System.Integer, _
   ByRef Curves As Curve _
) As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim NCurves As System.Integer
Dim Curves As Curve
Dim value As Body2

value = instance.ICreateTrimmedSheet2(NCurves, Curves)
```

### C#

```csharp
Body2 ICreateTrimmedSheet2(
   System.int NCurves,
   ref Curve Curves
)
```

### C++/CLI

```cpp
Body2^ ICreateTrimmedSheet2(
   System.int NCurves,
   Curve^% Curves
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NCurves`:
- `Curves`:

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
