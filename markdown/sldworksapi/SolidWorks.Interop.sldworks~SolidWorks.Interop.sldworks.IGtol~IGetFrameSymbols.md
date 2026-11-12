---
title: "IGetFrameSymbols Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "IGetFrameSymbols"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetFrameSymbols.html"
---

# IGetFrameSymbols Method (IGtol)

Obsolete. Superseded by [IGtol::IGetFrameSymbols2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~IGetFrameSymbols2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFrameSymbols( _
   ByVal FrameNumber As System.Short _
) As System.Short
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim FrameNumber As System.Short
Dim value As System.Short

value = instance.IGetFrameSymbols(FrameNumber)
```

### C#

```csharp
System.short IGetFrameSymbols(
   System.short FrameNumber
)
```

### C++/CLI

```cpp
System.short IGetFrameSymbols(
   System.short FrameNumber
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FrameNumber`:

## VBA Syntax

See [Gtol::IGetFrameSymbols](ms-its:sldworksapivb6.chm::/sldworks~Gtol~IGetFrameSymbols.html).

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
