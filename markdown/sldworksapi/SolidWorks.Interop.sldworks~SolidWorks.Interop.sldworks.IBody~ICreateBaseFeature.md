---
title: "ICreateBaseFeature Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "ICreateBaseFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~ICreateBaseFeature.html"
---

# ICreateBaseFeature Method (IBody)

Obsolete. Superseded by [IBody2::ICreateBaseFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ICreateBaseFeature.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateBaseFeature( _
   ByVal BodyIn As Body _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim BodyIn As Body
Dim value As System.Boolean

value = instance.ICreateBaseFeature(BodyIn)
```

### C#

```csharp
System.bool ICreateBaseFeature(
   Body BodyIn
)
```

### C++/CLI

```cpp
System.bool ICreateBaseFeature(
   Body^ BodyIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BodyIn`:

## VBA Syntax

See [Body::ICreateBaseFeature](ms-its:sldworksapivb6.chm::/sldworks~Body~ICreateBaseFeature.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
