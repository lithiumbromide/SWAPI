---
title: "SetColor Method (IReferenceCurve)"
project: "SOLIDWORKS API Help"
interface: "IReferenceCurve"
member: "SetColor"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve~SetColor.html"
---

# SetColor Method (IReferenceCurve)

Sets the color of the reference curve feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetColor( _
   ByVal ColorIn As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IReferenceCurve
Dim ColorIn As System.Integer
Dim value As System.Boolean

value = instance.SetColor(ColorIn)
```

### C#

```csharp
System.bool SetColor(
   System.int ColorIn
)
```

### C++/CLI

```cpp
System.bool SetColor(
   System.int ColorIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ColorIn`: COLORREF value of the color

### Return Value

True if the color was set, false if not

## VBA Syntax

See [ReferenceCurve::SetColor](ms-its:sldworksapivb6.chm::/sldworks~ReferenceCurve~SetColor.html).

## See Also

[IReferenceCurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve.html)
[IReferenceCurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve_members.html)
