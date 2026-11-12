---
title: "SetBody Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "SetBody"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetBody.html"
---

# SetBody Method (IFeature)

Obsolete. Superseded by [IFeature::SetBody2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~SetBody2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetBody( _
   ByVal BodyIn As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim BodyIn As System.Object
Dim value As System.Boolean

value = instance.SetBody(BodyIn)
```

### C#

```csharp
System.bool SetBody(
   System.object BodyIn
)
```

### C++/CLI

```cpp
System.bool SetBody(
   System.Object^ BodyIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BodyIn`:

## VBA Syntax

See [Feature::SetBody](ms-its:sldworksapivb6.chm::/sldworks~Feature~SetBody.html).

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
