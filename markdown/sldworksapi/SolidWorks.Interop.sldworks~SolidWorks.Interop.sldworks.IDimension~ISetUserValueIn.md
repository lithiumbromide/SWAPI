---
title: "ISetUserValueIn Method (IDimension)"
project: "SOLIDWORKS API Help"
interface: "IDimension"
member: "ISetUserValueIn"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetUserValueIn.html"
---

# ISetUserValueIn Method (IDimension)

Obsolete. Superseded by [IDimension::ISetUserValueIn3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimension~ISetUserValueIn3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetUserValueIn( _
   ByVal Doc As ModelDoc, _
   ByVal NewValue As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IDimension
Dim Doc As ModelDoc
Dim NewValue As System.Double

instance.ISetUserValueIn(Doc, NewValue)
```

### C#

```csharp
void ISetUserValueIn(
   ModelDoc Doc,
   System.double NewValue
)
```

### C++/CLI

```cpp
void ISetUserValueIn(
   ModelDoc^ Doc,
   System.double NewValue
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Doc`:
- `NewValue`:

## VBA Syntax

See [Dimension::ISetUserValueIn](ms-its:sldworksapivb6.chm::/sldworks~Dimension~ISetUserValueIn.html).

## See Also

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.html)
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.html)
