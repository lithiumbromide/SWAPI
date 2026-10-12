---
title: "ResolveAllLightWeightComponents Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "ResolveAllLightWeightComponents"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ResolveAllLightWeightComponents.html"
---

# ResolveAllLightWeightComponents Method (IAssemblyDoc)

Resolves the lightweight components in this assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function ResolveAllLightWeightComponents( _
   ByVal WarnUser As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim WarnUser As System.Boolean
Dim value As System.Integer

value = instance.ResolveAllLightWeightComponents(WarnUser)
```

### C#

```csharp
System.int ResolveAllLightWeightComponents(
   System.bool WarnUser
)
```

### C++/CLI

```cpp
System.int ResolveAllLightWeightComponents(
   System.bool WarnUser
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WarnUser`: True prompts the user to resolve components, false does not

### Return Value

Status of resolving the components as defined in [swComponentResolveStatus_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swComponentResolveStatus_e.html)

## VBA Syntax

See [AssemblyDoc::ResolveAllLightWeightComponents](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~ResolveAllLightWeightComponents.html).

## Examples

[Get Display Dimensions, GTols, and Surface-finish Symbols (VBA)](Get_Display_Dimensions,_Gtols,_and_Surface-Finish_Symbols_Example_VB.htm)
[Get Visibility of and Resolve Lightweight Components (VBA)](Get_Visibility_of_and_Resolve_Lightweight_Components_Example_VB.htm)
[Lock all External References (VBA)](Lock_All_External_References_Example_VB.htm)
[Resolve All Components and Fix a Component (C#)](Resolve_All_Components_Fix_A_Component_Example_CSharp.htm)
[Resolve All Components and Fix a Component (VB.NET)](Resolve_All_Components_Fix_A_Component_Example_VBNET.htm)
[Resolve All Components and Fix a Component (VBA)](Resolve_All_Components_Fix_A_Component_Example_VB.htm)

## Remarks

The assembly must be open in its own window. Call [ISldWorks::ActivateDoc2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~ActivateDoc2.html) or [IModelDoc2::Visible](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~Visible.html) to ensure that it is. If the assembly is only open as a reference in another document, then this method returns swComponentResolveStatus_e.swResolveNotPerformed.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::GetLightWeightComponentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetLightWeightComponentCount.html)
[IAssemblyDoc::LightweightAllResolved Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~LightweightAllResolved.html)
[IAssemblyDoc::ResolveAllLightweight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ResolveAllLightweight.html)
[IAssemblyDoc::ResolveOutOfDateLightWeightComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ResolveOutOfDateLightWeightComponents.html)
[IAssemblyDoc::SetComponentSuppression Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetComponentSuppression.html)
[IAssemblyDoc::SelectiveOpen Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SelectiveOpen.html)
