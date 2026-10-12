---
title: "EnumRelatedSectionedBodies Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "EnumRelatedSectionedBodies"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~EnumRelatedSectionedBodies.html"
---

# EnumRelatedSectionedBodies Method (IPartDoc)

Obsolete. Superseded by [IPartDoc::EnumRelatedSectionedBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~EnumRelatedSectionedBodies2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function EnumRelatedSectionedBodies( _
   ByVal ViewIn As ModelView _
) As EnumBodies
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim ViewIn As ModelView
Dim value As EnumBodies

value = instance.EnumRelatedSectionedBodies(ViewIn)
```

### C#

```csharp
EnumBodies EnumRelatedSectionedBodies(
   ModelView ViewIn
)
```

### C++/CLI

```cpp
EnumBodies^ EnumRelatedSectionedBodies(
   ModelView^ ViewIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ViewIn`:

## VBA Syntax

See [PartDoc::EnumRelatedSectionedBodies](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~EnumRelatedSectionedBodies.html).

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
