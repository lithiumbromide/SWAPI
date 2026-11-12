---
title: "ISetAngularUnits Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "ISetAngularUnits"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~ISetAngularUnits.html"
---

# ISetAngularUnits Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::ISetAngularUnits](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ISetAngularUnits.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetAngularUnits( _
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

instance.ISetAngularUnits(UType, FractBase, FractDenom, SigDigits)
```

### C#

```csharp
void ISetAngularUnits(
   System.short UType,
   System.short FractBase,
   System.short FractDenom,
   System.short SigDigits
)
```

### C++/CLI

```cpp
void ISetAngularUnits(
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

See [ModelDoc::ISetAngularUnits](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~ISetAngularUnits.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
