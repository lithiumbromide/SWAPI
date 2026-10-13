---
title: "CreateFeatureFromBody2 Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "CreateFeatureFromBody2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~CreateFeatureFromBody2.html"
---

# CreateFeatureFromBody2 Method (IPartDoc)

Obsolete. Superseded by [IPartDoc::CreateFeatureFromBody3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~CreateFeatureFromBody3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateFeatureFromBody2( _
   ByVal Body As System.Object, _
   ByVal MakeRefSurface As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim Body As System.Object
Dim MakeRefSurface As System.Boolean
Dim value As System.Object

value = instance.CreateFeatureFromBody2(Body, MakeRefSurface)
```

### C#

```csharp
System.object CreateFeatureFromBody2(
   System.object Body,
   System.bool MakeRefSurface
)
```

### C++/CLI

```cpp
System.Object^ CreateFeatureFromBody2(
   System.Object^ Body,
   System.bool MakeRefSurface
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Body`:
- `MakeRefSurface`:

## VBA Syntax

See [PartDoc::CreateFeatureFromBody2](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~CreateFeatureFromBody2.html).

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
