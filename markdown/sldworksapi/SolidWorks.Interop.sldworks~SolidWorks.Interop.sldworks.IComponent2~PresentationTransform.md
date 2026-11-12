---
title: "PresentationTransform Property (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "PresentationTransform"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~PresentationTransform.html"
---

# PresentationTransform Property (IComponent2)

Gets or sets the component transform.

## Syntax

### Visual Basic (Declaration)

```vb
Property PresentationTransform As MathTransform
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As MathTransform

instance.PresentationTransform = value

value = instance.PresentationTransform
```

### C#

```csharp
MathTransform PresentationTransform {get; set;}
```

### C++/CLI

```cpp
property MathTransform^ PresentationTransform {
   MathTransform^ get();
   void set (    MathTransform^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Component transform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html)

## VBA Syntax

See [Component2::PresentationTransform](ms-its:sldworksapivb6.chm::/sldworks~Component2~PresentationTransform.html).

## Examples

[Use Presentation Transforms to Move Component (VBA)](Use_Presentation_Transforms_to_Move_Component_Example_VB.htm)

## Remarks

This property affects the graphical display; it does not affect the underlying model geometry.

This property:

- gets or sets the component transform for graphical display.
- ignores all mate and in-context relationships. Only the display of the component on the screen is affected.
- does not apply the transform to component geometry.
- does not display any changes. To display changes, call [IModelDoc2::GraphicsRedraw2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GraphicsRedraw2.html).

This property's functionality is for graphical purposes only and does not affect solid models. For example, if you want to animate the explode steps for an assembly, then maintaining assembly mate and in-context relationships is not needed or desirable.

You must first enable a presentation transform by setting [IAssemblyDoc::EnablePresentation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~EnablePresentation.html) to true. [IComponent2::RemovePresentationTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~RemovePresentationTransform.html) removes any transform applied by IComponent2::PresentationTransform. Set IAssemblyDoc::EnablePresentation to false after calling IComponent2::RemovePresentationTransform. After calling this method, the component is next drawn in a position consistent with its underlying geometry ([IComponent2::Transform2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~Transform2.html)).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::GetSpecificTransform Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetSpecificTransform.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
