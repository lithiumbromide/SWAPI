---
title: "SetDisplayDualDimensionInRangeValues Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "SetDisplayDualDimensionInRangeValues"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetDisplayDualDimensionInRangeValues.html"
---

# SetDisplayDualDimensionInRangeValues Method (IGtol)

Sets whether to display dual units in dimension range values.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetDisplayDualDimensionInRangeValues( _
   ByVal InValue As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim InValue As System.Boolean

instance.SetDisplayDualDimensionInRangeValues(InValue)
```

### C#

```csharp
void SetDisplayDualDimensionInRangeValues(
   System.bool InValue
)
```

### C++/CLI

```cpp
void SetDisplayDualDimensionInRangeValues(
   System.bool InValue
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `InValue`: True to display dual units in dimension range values, false to not

## VBA Syntax

See [Gtol::SetDisplayDualDimensionInRangeValues](ms-its:sldworksapivb6.chm::/sldworks~Gtol~SetDisplayDualDimensionInRangeValues.html).

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
[IGtol::GetDisplayDualDimensionInRangeValues Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetDisplayDualDimensionInRangeValues.html)

## Availability

SOLIDWORKS 2024 FCS, Revision Number 32
