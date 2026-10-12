---
title: "GetSpecificTransform Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "GetSpecificTransform"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetSpecificTransform.html"
---

# GetSpecificTransform Method (IComponent2)

Get the collapsed or exploded transform of a component when the assembly is exploded.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSpecificTransform( _
   ByVal IgnoreExplode As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim IgnoreExplode As System.Boolean
Dim value As System.Object

value = instance.GetSpecificTransform(IgnoreExplode)
```

### C#

```csharp
System.object GetSpecificTransform(
   System.bool IgnoreExplode
)
```

### C++/CLI

```cpp
System.Object^ GetSpecificTransform(
   System.bool IgnoreExplode
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `IgnoreExplode`: True to get the component's collapsed transform when the assembly is exploded, false to get the component's exploded transform when the assembly is exploded

### Return Value

[Transform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.html)

## VBA Syntax

See [Component2::GetSpecificTransform](ms-its:sldworksapivb6.chm::/sldworks~Component2~GetSpecificTransform.html).

## Examples

[Get Collapsed Transform of Component in Exploded View (C#)](Get_Collapsed_Transform_of_Component_in_Exploded_View_Example_CSharp.htm)
[Get Collapsed Transform of Component in Exploded View (VB.NET)](Get_Collapsed_Transform_of_Component_in_Exploded_View_Example_VBNET.htm)
[Get Collapsed Transform of Component in Exploded View (VBA)](Get_Collapsed_Transform_of_Component_in_Exploded_View_Example_VB.htm)

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::GetTotalTransform Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetTotalTransform.html)
[IComponent2::SetTransformAndSolve2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetTransformAndSolve2.html)
[IComponent2::PresentationTransform Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~PresentationTransform.html)
[IComponent2::Transform2 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Transform2.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
