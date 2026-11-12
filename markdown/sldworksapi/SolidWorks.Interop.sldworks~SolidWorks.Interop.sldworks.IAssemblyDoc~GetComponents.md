---
title: "GetComponents Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "GetComponents"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetComponents.html"
---

# GetComponents Method (IAssemblyDoc)

Gets all of the components in the active configuration of this assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetComponents( _
   ByVal ToplevelOnly As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim ToplevelOnly As System.Boolean
Dim value As System.Object

value = instance.GetComponents(ToplevelOnly)
```

### C#

```csharp
System.object GetComponents(
   System.bool ToplevelOnly
)
```

### C++/CLI

```cpp
System.Object^ GetComponents(
   System.bool ToplevelOnly
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ToplevelOnly`: True to get only the top-level components of the FeatureManager design tree, false to get both the top-level and child components in the FeatureManager design tree

### Return Value

Array of [IComponent2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html)s (see **Remarks**)

## VBA Syntax

See [AssemblyDoc::GetComponents](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~GetComponents.html).

## Examples

[Insert MidSurface in Components (C#)](Insert_MidSurface_in_Component_Example_CSharp.htm)
[Insert MidSurface in Component (VB.NET)](Insert_MidSurface_in_Component_Example_VBNET.htm)
[Insert MidSurface in Component (VBA)](Insert_MidSurface_in_Component_Example_VB.htm)
[Get Mates (VB.NET)](Get_Mates_Example_VBNET.htm)
[Get Mates (C#)](Get_Mates_Example_CSharp.htm)

## Remarks

The components returned by this method can be in any order. You should not rely on the order to indicate anything about children or parents. If the hierarchy and order are important, then use [IModelDoc2::FirstFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~FirstFeature.html), [IFeature::GetTypeName2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetTypeName2.html), [IFeature::GetSpecificFeature2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetSpecificFeature2.html), [IComponent2::FirstFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~FirstFeature.html), and [IFeature::GetNextFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetNextFeature.html) to retrieve your information.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::IGetComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IGetComponents.html)
[IAssemblyDoc::GetComponentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetComponentCount.html)
[IComponent2::GetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetChildren.html)
[IComponent2::GetParent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetParent.html)
[IConfiguration::GetRootComponent3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetRootComponent3.html)
[IConfiguration::IGetRootComponent2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetRootComponent2.html)
[IConfigurationManager::ActiveConfiguration Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ActiveConfiguration.html)
[IAssemblyDoc::SelectiveOpen Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SelectiveOpen.html)
[IAssemblyDoc::GetComponentByID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetComponentByID.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
