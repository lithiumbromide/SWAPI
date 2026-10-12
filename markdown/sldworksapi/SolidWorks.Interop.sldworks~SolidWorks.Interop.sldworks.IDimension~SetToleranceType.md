---
title: "SetToleranceType Method (IDimension)"
project: "SOLIDWORKS API Help"
interface: "IDimension"
member: "SetToleranceType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetToleranceType.html"
---

# SetToleranceType Method (IDimension)

Obsolete. Superseded by [IDimensionTolerance::Type](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~Type.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetToleranceType( _
   ByVal NewType As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimension
Dim NewType As System.Integer
Dim value As System.Boolean

value = instance.SetToleranceType(NewType)
```

### C#

```csharp
System.bool SetToleranceType(
   System.int NewType
)
```

### C++/CLI

```cpp
System.bool SetToleranceType(
   System.int NewType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NewType`:

## VBA Syntax

See [Dimension::SetToleranceType](ms-its:sldworksapivb6.chm::/sldworks~Dimension~SetToleranceType.html).

## See Also

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.html)
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.html)
