---
title: "SetUserValueIn Method (IDimension)"
project: "SOLIDWORKS API Help"
interface: "IDimension"
member: "SetUserValueIn"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetUserValueIn.html"
---

# SetUserValueIn Method (IDimension)

Obsolete. Superseded by [IDimension::SetUserValueIn2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimension~SetUserValueIn2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetUserValueIn( _
   ByVal Doc As System.Object, _
   ByVal NewValue As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IDimension
Dim Doc As System.Object
Dim NewValue As System.Double

instance.SetUserValueIn(Doc, NewValue)
```

### C#

```csharp
void SetUserValueIn(
   System.object Doc,
   System.double NewValue
)
```

### C++/CLI

```cpp
void SetUserValueIn(
   System.Object^ Doc,
   System.double NewValue
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Doc`:
- `NewValue`:

## VBA Syntax

See [Dimension::SetUserValueIn](ms-its:sldworksapivb6.chm::/sldworks~Dimension~SetUserValueIn.html).

## See Also

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.html)
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.html)
