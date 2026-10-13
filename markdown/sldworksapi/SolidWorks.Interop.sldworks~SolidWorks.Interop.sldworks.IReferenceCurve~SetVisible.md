---
title: "SetVisible Method (IReferenceCurve)"
project: "SOLIDWORKS API Help"
interface: "IReferenceCurve"
member: "SetVisible"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve~SetVisible.html"
---

# SetVisible Method (IReferenceCurve)

Hides or shows the reference curve feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetVisible( _
   ByVal Visible As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IReferenceCurve
Dim Visible As System.Boolean
Dim value As System.Boolean

value = instance.SetVisible(Visible)
```

### C#

```csharp
System.bool SetVisible(
   System.bool Visible
)
```

### C++/CLI

```cpp
System.bool SetVisible(
   System.bool Visible
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Visible`: True for visible, false for hidden

### Return Value

True if set, false if not

## VBA Syntax

See [ReferenceCurve::SetVisible](ms-its:sldworksapivb6.chm::/sldworks~ReferenceCurve~SetVisible.html).

## See Also

[IReferenceCurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve.html)
[IReferenceCurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve_members.html)
