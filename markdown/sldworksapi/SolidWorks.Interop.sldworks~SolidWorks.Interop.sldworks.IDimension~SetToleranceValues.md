---
title: "SetToleranceValues Method (IDimension)"
project: "SOLIDWORKS API Help"
interface: "IDimension"
member: "SetToleranceValues"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetToleranceValues.html"
---

# SetToleranceValues Method (IDimension)

Obsolete. Superseded by [IDimensionTolerance::SetValues](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~SetValues.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetToleranceValues( _
   ByVal TolMin As System.Double, _
   ByVal TolMax As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimension
Dim TolMin As System.Double
Dim TolMax As System.Double
Dim value As System.Boolean

value = instance.SetToleranceValues(TolMin, TolMax)
```

### C#

```csharp
System.bool SetToleranceValues(
   System.double TolMin,
   System.double TolMax
)
```

### C++/CLI

```cpp
System.bool SetToleranceValues(
   System.double TolMin,
   System.double TolMax
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TolMin`:
- `TolMax`:

## VBA Syntax

See [Dimension::SetToleranceValues](ms-its:sldworksapivb6.chm::/sldworks~Dimension~SetToleranceValues.html).

## See Also

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.html)
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.html)
