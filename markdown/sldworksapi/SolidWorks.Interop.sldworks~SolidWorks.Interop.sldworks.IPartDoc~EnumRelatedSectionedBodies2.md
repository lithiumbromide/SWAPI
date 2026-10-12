---
title: "EnumRelatedSectionedBodies2 Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "EnumRelatedSectionedBodies2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~EnumRelatedSectionedBodies2.html"
---

# EnumRelatedSectionedBodies2 Method (IPartDoc)

Gets an enumeration of the related sectioned bodies in a part.

## Syntax

### Visual Basic (Declaration)

```vb
Function EnumRelatedSectionedBodies2( _
   ByVal ViewIn As ModelView _
) As EnumBodies2
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim ViewIn As ModelView
Dim value As EnumBodies2

value = instance.EnumRelatedSectionedBodies2(ViewIn)
```

### C#

```csharp
EnumBodies2 EnumRelatedSectionedBodies2(
   ModelView ViewIn
)
```

### C++/CLI

```cpp
EnumBodies2^ EnumRelatedSectionedBodies2(
   ModelView^ ViewIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ViewIn`: [Model view](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView.html)

### Return Value

[Enumeration of the related sectioned bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumBodies2.html)

## VBA Syntax

See [PartDoc::EnumRelatedSectionedBodies2](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~EnumRelatedSectionedBodies2.html).

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IPartDoc::EnumRelatedBodies2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~EnumRelatedBodies2.html)
[IPartDoc::EnumBodies3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~EnumBodies3.html)
[IPartDoc::GetRelatedBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetRelatedBodies.html)
[IPartDoc::GetRelatedSectionedBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetRelatedSectionedBodies.html)
[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number
