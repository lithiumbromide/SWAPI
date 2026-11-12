---
title: "CreateBaseFeature Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "CreateBaseFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~CreateBaseFeature.html"
---

# CreateBaseFeature Method (IBody)

Obsolete. Superseded by [IBody2::CreateBaseFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~CreateBaseFeature.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateBaseFeature( _
   ByVal BodyIn As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim BodyIn As System.Object
Dim value As System.Boolean

value = instance.CreateBaseFeature(BodyIn)
```

### C#

```csharp
System.bool CreateBaseFeature(
   System.object BodyIn
)
```

### C++/CLI

```cpp
System.bool CreateBaseFeature(
   System.Object^ BodyIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BodyIn`:

## VBA Syntax

See [Body::CreateBaseFeature](ms-its:sldworksapivb6.chm::/sldworks~Body~CreateBaseFeature.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
