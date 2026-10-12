---
title: "ICreateSurfaceFeatureFromBodyCount Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "ICreateSurfaceFeatureFromBodyCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ICreateSurfaceFeatureFromBodyCount.html"
---

# ICreateSurfaceFeatureFromBodyCount Method (IPartDoc)

Obsolete. Superseded by [IPartDoc::ICreateSurfaceFeatureFromBodyCount2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~ICreateSurfaceFeatureFromBodyCount2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateSurfaceFeatureFromBodyCount( _
   ByVal Body As Body, _
   ByVal Options As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim Body As Body
Dim Options As System.Integer
Dim value As System.Integer

value = instance.ICreateSurfaceFeatureFromBodyCount(Body, Options)
```

### C#

```csharp
System.int ICreateSurfaceFeatureFromBodyCount(
   Body Body,
   System.int Options
)
```

### C++/CLI

```cpp
System.int ICreateSurfaceFeatureFromBodyCount(
   Body^ Body,
   System.int Options
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Body`:
- `Options`:

## VBA Syntax

See [PartDoc::ICreateSurfaceFeatureFromBodyCount](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~ICreateSurfaceFeatureFromBodyCount.html).

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
