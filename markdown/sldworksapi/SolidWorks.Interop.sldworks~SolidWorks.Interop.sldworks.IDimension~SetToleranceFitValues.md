---
title: "SetToleranceFitValues Method (IDimension)"
project: "SOLIDWORKS API Help"
interface: "IDimension"
member: "SetToleranceFitValues"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetToleranceFitValues.html"
---

# SetToleranceFitValues Method (IDimension)

Obsolete. Superseded by [IDimensionTolerance::SetFitValues](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~SetFitValues.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetToleranceFitValues( _
   ByVal NewLValue As System.String, _
   ByVal NewUValue As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimension
Dim NewLValue As System.String
Dim NewUValue As System.String
Dim value As System.Boolean

value = instance.SetToleranceFitValues(NewLValue, NewUValue)
```

### C#

```csharp
System.bool SetToleranceFitValues(
   System.string NewLValue,
   System.string NewUValue
)
```

### C++/CLI

```cpp
System.bool SetToleranceFitValues(
   System.String^ NewLValue,
   System.String^ NewUValue
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NewLValue`:
- `NewUValue`:

## VBA Syntax

See [Dimension::SetToleranceFitValues](ms-its:sldworksapivb6.chm::/sldworks~Dimension~SetToleranceFitValues.html).

## See Also

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.html)
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.html)
