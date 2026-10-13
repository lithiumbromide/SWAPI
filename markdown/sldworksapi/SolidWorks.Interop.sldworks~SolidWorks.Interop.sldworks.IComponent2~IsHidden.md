---
title: "IsHidden Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "IsHidden"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsHidden.html"
---

# IsHidden Method (IComponent2)

Gets whether this component is hidden or suppressed.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsHidden( _
   ByVal ConsiderSuppressed As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim ConsiderSuppressed As System.Boolean
Dim value As System.Boolean

value = instance.IsHidden(ConsiderSuppressed)
```

### C#

```csharp
System.bool IsHidden(
   System.bool ConsiderSuppressed
)
```

### C++/CLI

```cpp
System.bool IsHidden(
   System.bool ConsiderSuppressed
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ConsiderSuppressed`: Controls whether suppressed components are hidden

### Return Value

True or false (see **Remarks**)

## VBA Syntax

See [Component2::IsHidden](ms-its:sldworksapivb6.chm::/sldworks~Component2~IsHidden.html).

## Examples

[Change Material Properties (VBA)](Change_Material_Properties_Example_VB.htm)
[Get Transforms of Assembly Components (VBA)](Get_Transforms_of_Assembly_Components_Example_VB.htm)
[Get Component State (C#)](Get_Component_State_Example_CSharp.htm)
[Get Component State (VB.NET](Get_Component_State_Example_VBNET.htm)
[Get Component State (VBA)](Get_Component_State_Example_VB.htm)

## Remarks

The state of this component can vary based on the active configuration.

| ConsiderSuppressed | Component | Component | IsHidden |
| --- | --- | --- | --- |
| True | Hidden | Unsuppressed | True |
| True | Hidden | Suppressed | True |
| True | Shown | Unsuppressed | False |
| True | Shown | Suppressed | True |
| False | Hidden | Unsuppressed | True |
| False | Hidden | Suppressed | True |
| False | Shown | Unsuppressed | False |
| False | Shown | Suppressed | False |

NOTE: For [lightweight](sldworksAPIProgGuide.chm::/OVERVIEW/Work_with_Lightweight_Components.htm) components, IsHidden returns True if ConsiderSuppressed is True.

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::ISetVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ISetVisibility.html)
[IComponent2::IsSuppressed Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsSuppressed.html)
[IComponent2::SetSuppression2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetSuppression2.html)
[IComponent2::SetVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetVisibility.html)
[IComponent2::Visible Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Visible.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
