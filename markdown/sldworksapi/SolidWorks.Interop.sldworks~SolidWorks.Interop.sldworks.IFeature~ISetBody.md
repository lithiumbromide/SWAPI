---
title: "ISetBody Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "ISetBody"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ISetBody.html"
---

# ISetBody Method (IFeature)

Obsolete. Superseded by [IFeature::ISetBody3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ISetBody3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ISetBody( _
   ByVal BodyIn As Body _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim BodyIn As Body
Dim value As System.Boolean

value = instance.ISetBody(BodyIn)
```

### C#

```csharp
System.bool ISetBody(
   Body BodyIn
)
```

### C++/CLI

```cpp
System.bool ISetBody(
   Body^ BodyIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BodyIn`:

## VBA Syntax

See [Feature::ISetBody](ms-its:sldworksapivb6.chm::/sldworks~Feature~ISetBody.html).

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
