---
title: "ICreateTrimmedSheet Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "ICreateTrimmedSheet"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~ICreateTrimmedSheet.html"
---

# ICreateTrimmedSheet Method (ISurface)

Obsolete. Superseded by [ISurface::ICreateTrimmedSheet4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~ICreateTrimmedSheet4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateTrimmedSheet( _
   ByVal NCurves As System.Integer, _
   ByRef Curves As Curve _
) As Body
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim NCurves As System.Integer
Dim Curves As Curve
Dim value As Body

value = instance.ICreateTrimmedSheet(NCurves, Curves)
```

### C#

```csharp
Body ICreateTrimmedSheet(
   System.int NCurves,
   ref Curve Curves
)
```

### C++/CLI

```cpp
Body^ ICreateTrimmedSheet(
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
