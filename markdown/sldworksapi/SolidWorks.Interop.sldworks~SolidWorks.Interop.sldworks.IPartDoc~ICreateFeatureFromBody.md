---
title: "ICreateFeatureFromBody Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "ICreateFeatureFromBody"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ICreateFeatureFromBody.html"
---

# ICreateFeatureFromBody Method (IPartDoc)

Obsolete. Superseded by [IPartDoc::ICreateFeatureFromBody4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~ICreateFeatureFromBody4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateFeatureFromBody( _
   ByVal Body As Body _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim Body As Body
Dim value As Feature

value = instance.ICreateFeatureFromBody(Body)
```

### C#

```csharp
Feature ICreateFeatureFromBody(
   Body Body
)
```

### C++/CLI

```cpp
Feature^ ICreateFeatureFromBody(
   Body^ Body
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Body`:

## VBA Syntax

See [PartDoc::ICreateFeatureFromBody](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~ICreateFeatureFromBody.html).

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
