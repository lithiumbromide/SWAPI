---
title: "SetSuppression2 Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "SetSuppression2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetSuppression2.html"
---

# SetSuppression2 Method (IComponent2)

Sets the suppression state of this component.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetSuppression2( _
   ByVal State As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim State As System.Integer
Dim value As System.Integer

value = instance.SetSuppression2(State)
```

### C#

```csharp
System.int SetSuppression2(
   System.int State
)
```

### C++/CLI

```cpp
System.int SetSuppression2(
   System.int State
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `State`: Suppression state of this component as defined in [swComponentSuppressionState_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swComponentSuppressionState_e.html)

### Return Value

Status as defined in [swSuppressionError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSuppressionError_e.html)

## VBA Syntax

See [Component2::SetSuppression2](ms-its:sldworksapivb6.chm::/sldworks~Component2~SetSuppression2.html).

## Examples

[Access Assembly (C++)](Access_Assembly_Example_CPlusPlus_COM.htm)
[Set All Assembly Components Lightweight or Resolved (VBA)](Set_All_Assembly_Components_Lightweight_or_Resolved_Example_VB.htm)
[Set Fully Resolved Assembly to Lightweight (C#)](Set_Fully_Resolved_Assembly_to_Lightweight_Example_CSharp.htm)
[Set Fully Resolved Assembly to Lightweight (VB.NET)](Set_Fully_Resolved_Assembly_to_Lightweight_Example_VBNET.htm)
[Set Fully Resolved Assembly to Lightweight (VBA)](Set_Fully_Resolved_Assembly_to_Lightweight_Example_VB.htm)

## Remarks

SOLIDWORKS does not allow suppressing components while a PropertyManager page is open.

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IAssemblyDoc::LightweightAllResolved Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~LightweightAllResolved.html)
[IAssemblyDoc::SetComponentSuppression Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetComponentSuppression.html)
[IComponent2::GetSuppression Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetSuppression.html)
[IComponent2::IsSuppressed Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsSuppressed.html)
[IComponent2::IsHidden Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsHidden.html)
[IAssemblyDoc::CompConfigProperties5 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CompConfigProperties5.html)

## Availability

SOLIDWORKS 2004 SP4, Revision Number 12.4
