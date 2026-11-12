---
title: "SetToleranceFontInfo Method (IDimension)"
project: "SOLIDWORKS API Help"
interface: "IDimension"
member: "SetToleranceFontInfo"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetToleranceFontInfo.html"
---

# SetToleranceFontInfo Method (IDimension)

Obsolete. Superseded by [IDimensionTolerance::SetFont](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~SetFont.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetToleranceFontInfo( _
   ByVal UseFontScale As System.Integer, _
   ByVal TolScale As System.Double, _
   ByVal TolHeight As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimension
Dim UseFontScale As System.Integer
Dim TolScale As System.Double
Dim TolHeight As System.Double
Dim value As System.Boolean

value = instance.SetToleranceFontInfo(UseFontScale, TolScale, TolHeight)
```

### C#

```csharp
System.bool SetToleranceFontInfo(
   System.int UseFontScale,
   System.double TolScale,
   System.double TolHeight
)
```

### C++/CLI

```cpp
System.bool SetToleranceFontInfo(
   System.int UseFontScale,
   System.double TolScale,
   System.double TolHeight
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UseFontScale`:
- `TolScale`:
- `TolHeight`:

## VBA Syntax

See [Dimension::SetToleranceFontInfo](ms-its:sldworksapivb6.chm::/sldworks~Dimension~SetToleranceFontInfo.html).

## See Also

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.html)
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.html)
