---
title: "SetSuppression Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "SetSuppression"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetSuppression.html"
---

# SetSuppression Method (IFeature)

Obsolete. Superseded by [IFeature::SetSuppression2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~SetSuppression2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetSuppression( _
   ByVal SuppressState As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim SuppressState As System.Integer
Dim value As System.Boolean

value = instance.SetSuppression(SuppressState)
```

### C#

```csharp
System.bool SetSuppression(
   System.int SuppressState
)
```

### C++/CLI

```cpp
System.bool SetSuppression(
   System.int SuppressState
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SuppressState`:

## VBA Syntax

See [Feature::SetSuppression](ms-its:sldworksapivb6.chm::/sldworks~Feature~SetSuppression.html).

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
