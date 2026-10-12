---
title: "GetSuppression2 Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "GetSuppression2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetSuppression2.html"
---

# GetSuppression2 Method (IComponent2)

Gets the suppression state of this component.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSuppression2() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.Integer

value = instance.GetSuppression2()
```

### C#

```csharp
System.int GetSuppression2()
```

### C++/CLI

```cpp
System.int GetSuppression2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Suppression state of this component or internal ID mismatch error code as defined in [swComponentSuppressionState_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swComponentSuppressionState_e.html)

## VBA Syntax

See [Component2::GetSuppression2](ms-its:sldworksapivb6.chm::/sldworks~Component2~GetSuppression2.html).

## Examples

[Get and Set Component's Suppression State (VBA)](Get_and_Set_Component_s_Suppression_State_Example_VB.htm)

## Remarks

The difference between this method and the now obsolete IComponent2::GetSuppression is that this method returns an error code (5 = swComponentSuppressionState_e.swComponentInternalIdMismatch) if there is an internal ID mismatch.

Use this method to determine if the component is suppressed, lightweight, or fully resolved. It is critical to know the component's suppression state because lightweight and suppressed components contain only a small subset of data compared to a fully resolved component. For more information, see [Work With Lightweight Components](sldworksAPIProgGuide.chm::/OVERVIEW/Work_with_Lightweight_Components.htm).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IAssemblyDoc::LightweightAllResolved Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~LightweightAllResolved.html)
[IAssemblyDoc::SetComponentState Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetComponentState.html)
[IAssemblyDoc::SetComponentSuppression Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetComponentSuppression.html)
[IComponent2::IsSuppressed Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsSuppressed.html)
[IComponent2::SetSuppression2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetSuppression2.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
