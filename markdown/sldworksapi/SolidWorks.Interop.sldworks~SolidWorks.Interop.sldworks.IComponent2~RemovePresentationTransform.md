---
title: "RemovePresentationTransform Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "RemovePresentationTransform"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~RemovePresentationTransform.html"
---

# RemovePresentationTransform Method (IComponent2)

Removes the presentation transform from this component.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RemovePresentationTransform()
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2

instance.RemovePresentationTransform()
```

### C#

```csharp
void RemovePresentationTransform()
```

### C++/CLI

```cpp
void RemovePresentationTransform();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [Component2::RemovePresentationTransform](ms-its:sldworksapivb6.chm::/sldworks~Component2~RemovePresentationTransform.html).

## Examples

[Use Presentation Transforms to Move Component (VBA)](Use_Presentation_Transforms_to_Move_Component_Example_VB.htm)

## Remarks

Set [IAssemblyDoc::EnablePresentation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~EnablePresentation.html) to false after a user is finished with presentation transforms and has called IComponent2::RemovePresentationTransform, which removes any transform applied by [IComponent::PresentationTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~PresentationTransform.html).

After calling IComponent2::RemovePresentationTransfrom, the component is next drawn in a position consistent with its underlying geometry ([IComponent2::Transform2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~Transform2.html)).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IAssemblyDoc::EnablePresentation Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~EnablePresentation.html)
[IComponent2::GetTotalTransform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetTotalTransform.html)
[IComponent2::PresentationTransform Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~PresentationTransform.html)
[IComponent2::Transform2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Transform2.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
