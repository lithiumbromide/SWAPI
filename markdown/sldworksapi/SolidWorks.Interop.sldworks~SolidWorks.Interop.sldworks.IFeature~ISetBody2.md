---
title: "ISetBody2 Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "ISetBody2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ISetBody2.html"
---

# ISetBody2 Method (IFeature)

Obsolete. Superseded by [IFeature::ISetBody3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ISetBody3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ISetBody2( _
   ByVal BodyIn As Body, _
   ByVal ApplyUserIds As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim BodyIn As Body
Dim ApplyUserIds As System.Boolean
Dim value As System.Boolean

value = instance.ISetBody2(BodyIn, ApplyUserIds)
```

### C#

```csharp
System.bool ISetBody2(
   Body BodyIn,
   System.bool ApplyUserIds
)
```

### C++/CLI

```cpp
System.bool ISetBody2(
   Body^ BodyIn,
   System.bool ApplyUserIds
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BodyIn`:
- `ApplyUserIds`:

## VBA Syntax

See [Feature::ISetBody2](ms-its:sldworksapivb6.chm::/sldworks~Feature~ISetBody2.html).

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
