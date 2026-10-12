---
title: "SetUnits Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "SetUnits"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SetUnits.html"
---

# SetUnits Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::SetUnits](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetUnits.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetUnits( _
   ByVal UType As System.Short, _
   ByVal FractBase As System.Short, _
   ByVal FractDenom As System.Short, _
   ByVal SigDigits As System.Short, _
   ByVal RoundToFraction As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim UType As System.Short
Dim FractBase As System.Short
Dim FractDenom As System.Short
Dim SigDigits As System.Short
Dim RoundToFraction As System.Boolean

instance.SetUnits(UType, FractBase, FractDenom, SigDigits, RoundToFraction)
```

### C#

```csharp
void SetUnits(
   System.short UType,
   System.short FractBase,
   System.short FractDenom,
   System.short SigDigits,
   System.bool RoundToFraction
)
```

### C++/CLI

```cpp
void SetUnits(
   System.short UType,
   System.short FractBase,
   System.short FractDenom,
   System.short SigDigits,
   System.bool RoundToFraction
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UType`:
- `FractBase`:
- `FractDenom`:
- `SigDigits`:
- `RoundToFraction`:

## VBA Syntax

See [ModelDoc::SetUnits](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~SetUnits.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
