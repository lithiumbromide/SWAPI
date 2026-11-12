---
title: "SetAngularUnits Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "SetAngularUnits"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SetAngularUnits.html"
---

# SetAngularUnits Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::SetAngularUnits](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetAngularUnits.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetAngularUnits( _
   ByVal UType As System.Short, _
   ByVal FractBase As System.Short, _
   ByVal FractDenom As System.Short, _
   ByVal SigDigits As System.Short _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim UType As System.Short
Dim FractBase As System.Short
Dim FractDenom As System.Short
Dim SigDigits As System.Short

instance.SetAngularUnits(UType, FractBase, FractDenom, SigDigits)
```

### C#

```csharp
void SetAngularUnits(
   System.short UType,
   System.short FractBase,
   System.short FractDenom,
   System.short SigDigits
)
```

### C++/CLI

```cpp
void SetAngularUnits(
   System.short UType,
   System.short FractBase,
   System.short FractDenom,
   System.short SigDigits
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UType`:
- `FractBase`:
- `FractDenom`:
- `SigDigits`:

## VBA Syntax

See [ModelDoc::SetAngularUnits](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~SetAngularUnits.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
