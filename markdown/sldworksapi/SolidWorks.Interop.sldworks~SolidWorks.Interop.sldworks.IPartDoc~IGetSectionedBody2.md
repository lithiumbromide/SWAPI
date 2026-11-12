---
title: "IGetSectionedBody2 Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "IGetSectionedBody2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetSectionedBody2.html"
---

# IGetSectionedBody2 Method (IPartDoc)

Gets the sectioned body seen in the specified drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSectionedBody2( _
   ByVal ViewIn As ModelView _
) As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim ViewIn As ModelView
Dim value As Body2

value = instance.IGetSectionedBody2(ViewIn)
```

### C#

```csharp
Body2 IGetSectionedBody2(
   ModelView ViewIn
)
```

### C++/CLI

```cpp
Body2^ IGetSectionedBody2(
   ModelView^ ViewIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ViewIn`: [Model view](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView.html)

### Return Value

[Sectioned body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

## VBA Syntax

See [PartDoc::IGetSectionedBody2](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~IGetSectionedBody2.html).

## Remarks

To determine if the desired model view is currently displaying a sectioned view, use [IModelView::GetDisplayState](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~GetDisplayState.html).

If you need the full body representation, use [IPartDoc::GetBodies2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~GetBodies2.html) or [IPartDoc::EnumBodies3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~EnumBodies3.html), which ignores the sectioning operation.

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IPartDoc::IGetSectionedBody2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetSectionedBody2.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
