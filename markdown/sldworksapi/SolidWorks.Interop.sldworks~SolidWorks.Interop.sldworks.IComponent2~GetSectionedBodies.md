---
title: "GetSectionedBodies Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "GetSectionedBodies"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetSectionedBodies.html"
---

# GetSectionedBodies Method (IComponent2)

Gets the sectioned bodies in the specified section view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSectionedBodies( _
   ByVal ViewIn As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim ViewIn As System.Object
Dim value As System.Object

value = instance.GetSectionedBodies(ViewIn)
```

### C#

```csharp
System.object GetSectionedBodies(
   System.object ViewIn
)
```

### C++/CLI

```cpp
System.Object^ GetSectionedBodies(
   System.Object^ ViewIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ViewIn`: Model view displaying the sectioned view

### Return Value

Array of the sectioned bodies in the specified view

## VBA Syntax

See [Component2::GetSectionedBodies](ms-its:sldworksapivb6.chm::/sldworks~Component2~GetSectionedBodies.html).

## Examples

[Get Sectioned Bodies (VBA)](Get_Sectioned_Bodies_Example_VB.htm)

## Remarks

To determine if the model view you want is currently displaying a sectioned view, use [IModelView::GetDisplayState](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~GetDisplayState.html).

If you need the full body representation, use [IComponent2::GetBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~GetBody.html), [IPartDoc::GetBodies2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~GetBodies2.html), or [IPartDoc::EnumBodies3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~EnumBodies3.html), which ignore the sectioning operation.

For COM implementations, see [IComponent2::EnumSectionedBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~EnumSectionedBodies.html).

If a component is suppressed or lightweight, this method returns NULL because the component is not loaded into memory by SOLIDWORKS. For more information on lightweight components, see [Work With Lightweight Components](sldworksAPIProgGuide.chm::/OVERVIEW/Work_with_Lightweight_Components.htm).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
