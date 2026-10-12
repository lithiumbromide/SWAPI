---
title: "GetSuppression Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "GetSuppression"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetSuppression.html"
---

# GetSuppression Method (IComponent2)

Obsolete. Superseded by [IComponent2::GetSuppression2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetSuppression2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSuppression() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.Integer

value = instance.GetSuppression()
```

### C#

```csharp
System.int GetSuppression()
```

### C++/CLI

```cpp
System.int GetSuppression();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Suppression state of this component instance as defined in [swComponentSuppressionState_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swComponentSuppressionState_e.html)

## VBA Syntax

See [Component2::GetSuppression](ms-its:sldworksapivb6.chm::/sldworks~Component2~GetSuppression.html).

## Examples

[Access Assembly (C++)](Access_Assembly_Example_CPlusPlus_COM.htm)
[Change Material Properties (VBA)](Change_Material_Properties_Example_VB.htm)
[Make Assembly Components Lightweight (VBA)](Make_Assembly_Components_Lightweight_Example_VB.htm)
[Get Component State (C#)](Get_Component_State_Example_CSharp.htm)
[Get Component State (VB.NET)](Get_Component_State_Example_VBNET.htm)
[Get Component State (VBA)](Get_Component_State_Example_VB.htm)

## Remarks

Use this method to determine if the component is suppressed, lightweight, or fully resolved. It is critical to know the component's suppression state because lightweight and suppressed components contain only a small subset of data compared to a fully resolved component. For more information, see [Work With Lightweight Components](sldworksAPIProgGuide.chm::/OVERVIEW/Work_with_Lightweight_Components.htm).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IAssemblyDoc::LightweightAllResolved Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~LightweightAllResolved.html)
[IAssemblyDoc::SetComponentState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetComponentState.html)
[IAssemblyDoc::SetComponentSuppression Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetComponentSuppression.html)
[IComponent2::IsSuppressed Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsSuppressed.html)
[IComponent2::SetSuppression2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetSuppression2.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
