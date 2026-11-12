---
title: "IGetSectionedBody Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "IGetSectionedBody"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetSectionedBody.html"
---

# IGetSectionedBody Method (IPartDoc)

Obsolete. Superseded by [IPartDoc::IGetSectionedBody2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~IGetSectionedBody2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSectionedBody( _
   ByVal ViewIn As ModelView _
) As Body
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim ViewIn As ModelView
Dim value As Body

value = instance.IGetSectionedBody(ViewIn)
```

### C#

```csharp
Body IGetSectionedBody(
   ModelView ViewIn
)
```

### C++/CLI

```cpp
Body^ IGetSectionedBody(
   ModelView^ ViewIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ViewIn`:

## VBA Syntax

See [PartDoc::IGetSectionedBody](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~IGetSectionedBody.html).

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
