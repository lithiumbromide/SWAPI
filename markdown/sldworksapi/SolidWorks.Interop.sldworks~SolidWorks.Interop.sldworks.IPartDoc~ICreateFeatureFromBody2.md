---
title: "ICreateFeatureFromBody2 Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "ICreateFeatureFromBody2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ICreateFeatureFromBody2.html"
---

# ICreateFeatureFromBody2 Method (IPartDoc)

Obsolete. Superseded by [IPartDoc::ICreateFeatureFromBody4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~ICreateFeatureFromBody4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateFeatureFromBody2( _
   ByVal Body As Body, _
   ByVal MakeRefSurface As System.Boolean _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim Body As Body
Dim MakeRefSurface As System.Boolean
Dim value As Feature

value = instance.ICreateFeatureFromBody2(Body, MakeRefSurface)
```

### C#

```csharp
Feature ICreateFeatureFromBody2(
   Body Body,
   System.bool MakeRefSurface
)
```

### C++/CLI

```cpp
Feature^ ICreateFeatureFromBody2(
   Body^ Body,
   System.bool MakeRefSurface
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Body`:
- `MakeRefSurface`:

## VBA Syntax

See [PartDoc::ICreateFeatureFromBody2](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~ICreateFeatureFromBody2.html).

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
