---
title: "AddTrimmingLoop Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "AddTrimmingLoop"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~AddTrimmingLoop.html"
---

# AddTrimmingLoop Method (ISurface)

Obsolete. Superseded by [ISurface::AddTrimmingLoop2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~AddTrimmingLoop2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddTrimmingLoop( _
   ByVal NCrvs As System.Integer, _
   ByVal VOrder As System.Object, _
   ByVal VDim As System.Object, _
   ByVal VPeriodic As System.Object, _
   ByVal VNumKnots As System.Object, _
   ByVal VNumCtrlPoints As System.Object, _
   ByVal VKnots As System.Object, _
   ByVal VCtrlPointDbls As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim NCrvs As System.Integer
Dim VOrder As System.Object
Dim VDim As System.Object
Dim VPeriodic As System.Object
Dim VNumKnots As System.Object
Dim VNumCtrlPoints As System.Object
Dim VKnots As System.Object
Dim VCtrlPointDbls As System.Object
Dim value As System.Boolean

value = instance.AddTrimmingLoop(NCrvs, VOrder, VDim, VPeriodic, VNumKnots, VNumCtrlPoints, VKnots, VCtrlPointDbls)
```

### C#

```csharp
System.bool AddTrimmingLoop(
   System.int NCrvs,
   System.object VOrder,
   System.object VDim,
   System.object VPeriodic,
   System.object VNumKnots,
   System.object VNumCtrlPoints,
   System.object VKnots,
   System.object VCtrlPointDbls
)
```

### C++/CLI

```cpp
System.bool AddTrimmingLoop(
   System.int NCrvs,
   System.Object^ VOrder,
   System.Object^ VDim,
   System.Object^ VPeriodic,
   System.Object^ VNumKnots,
   System.Object^ VNumCtrlPoints,
   System.Object^ VKnots,
   System.Object^ VCtrlPointDbls
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NCrvs`:
- `VOrder`:
- `VDim`:
- `VPeriodic`:
- `VNumKnots`:
- `VNumCtrlPoints`:
- `VKnots`:
- `VCtrlPointDbls`:

## VBA Syntax

See [Surface::AddTrimmingLoop](ms-its:sldworksapivb6.chm::/sldworks~Surface~AddTrimmingLoop.html).

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
