---
title: "ICreateFeatureFromBody3 Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "ICreateFeatureFromBody3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ICreateFeatureFromBody3.html"
---

# ICreateFeatureFromBody3 Method (IPartDoc)

Obsolete. Superseded by [IPartDoc::ICreateFeatureFromBody4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~ICreateFeatureFromBody4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateFeatureFromBody3( _
   ByVal Body As Body, _
   ByVal MakeRefSurface As System.Boolean, _
   ByVal Options As System.Integer _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim Body As Body
Dim MakeRefSurface As System.Boolean
Dim Options As System.Integer
Dim value As Feature

value = instance.ICreateFeatureFromBody3(Body, MakeRefSurface, Options)
```

### C#

```csharp
Feature ICreateFeatureFromBody3(
   Body Body,
   System.bool MakeRefSurface,
   System.int Options
)
```

### C++/CLI

```cpp
Feature^ ICreateFeatureFromBody3(
   Body^ Body,
   System.bool MakeRefSurface,
   System.int Options
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Body`:
- `MakeRefSurface`:
- `Options`:

## VBA Syntax

See [PartDoc::ICreateFeatureFromBody3](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~ICreateFeatureFromBody3.html).

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
