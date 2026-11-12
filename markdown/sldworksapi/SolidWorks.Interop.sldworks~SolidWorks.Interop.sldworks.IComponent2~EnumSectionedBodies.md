---
title: "EnumSectionedBodies Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "EnumSectionedBodies"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~EnumSectionedBodies.html"
---

# EnumSectionedBodies Method (IComponent2)

Gets the sectioned bodies seen in the specified view and returns them in an enumerated list.

## Syntax

### Visual Basic (Declaration)

```vb
Function EnumSectionedBodies( _
   ByVal ViewIn As ModelView _
) As EnumBodies2
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim ViewIn As ModelView
Dim value As EnumBodies2

value = instance.EnumSectionedBodies(ViewIn)
```

### C#

```csharp
EnumBodies2 EnumSectionedBodies(
   ModelView ViewIn
)
```

### C++/CLI

```cpp
EnumBodies2^ EnumSectionedBodies(
   ModelView^ ViewIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ViewIn`: Pointer to the [model view](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView.html) displaying the sectioned view

### Return Value

Pointer to the [enumerated list of bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumBodies2.html)

## VBA Syntax

See [Component2::EnumSectionedBodies](ms-its:sldworksapivb6.chm::/sldworks~Component2~EnumSectionedBodies.html).

## Remarks

To determine if the model view you want is currently displaying a sectioned view, use [IModelView::GetDisplayState](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~GetDisplayState.html).

If you need the full body representation, use [IComponent2::GetBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~GetBody.html), [IPartDoc::GetBodies2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~GetBodies2.html), or [IPartDoc::EnumBodies3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~EnumBodies3.html), which ignore the sectioning operation.

For Dispatch implementations, see [IComponent2::GetSectionedBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~GetSectionedBodies.html).

If a component is suppressed or lightweight, this method returns NULL because the component is not loaded into memory by SOLIDWORKS. For more information on lightweight components, see [Work With Lightweight Components](sldworksAPIProgGuide.chm::/OVERVIEW/Work_with_Lightweight_Components.htm).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
