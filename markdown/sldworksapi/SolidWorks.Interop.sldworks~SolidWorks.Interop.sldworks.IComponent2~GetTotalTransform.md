---
title: "GetTotalTransform Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "GetTotalTransform"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetTotalTransform.html"
---

# GetTotalTransform Method (IComponent2)

Combines the original transform of this component with the presentation transform of this component.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTotalTransform( _
   ByVal IncludePresentationXform As System.Boolean _
) As MathTransform
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim IncludePresentationXform As System.Boolean
Dim value As MathTransform

value = instance.GetTotalTransform(IncludePresentationXform)
```

### C#

```csharp
MathTransform GetTotalTransform(
   System.bool IncludePresentationXform
)
```

### C++/CLI

```cpp
MathTransform^ GetTotalTransform(
   System.bool IncludePresentationXform
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `IncludePresentationXform`: True to combine the transforms, false to not

### Return Value

Pointer to the [IMathTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html) object

## VBA Syntax

See [Component2::GetTotalTransform](ms-its:sldworksapivb6.chm::/sldworks~Component2~GetTotalTransform.html).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IAssemblyDoc::EnablePresentation Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~EnablePresentation.html)
[IComponent2::PresentationTransform Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~PresentationTransform.html)
[IComponent2::RemovePresentationTransform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~RemovePresentationTransform.html)
[IComponent2::SetTransformAndSolve2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetTransformAndSolve2.html)
[IComponent2::Transform2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Transform2.html)
[IComponent2::GetSpecificTransform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetSpecificTransform.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
