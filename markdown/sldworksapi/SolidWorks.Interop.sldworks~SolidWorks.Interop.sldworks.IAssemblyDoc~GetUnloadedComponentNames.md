---
title: "GetUnloadedComponentNames Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "GetUnloadedComponentNames"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetUnloadedComponentNames.html"
---

# GetUnloadedComponentNames Method (IAssemblyDoc)

Gets the unloaded components' paths, referenced configuration names, reasons why they are unloaded, document types, and names.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUnloadedComponentNames( _
   ByRef UnloadedComponentPathNames As System.Object, _
   ByRef UnloadedComponentReferencedConfigurationNames As System.Object, _
   ByRef ReasonForUnloadingComponents As System.Object, _
   ByRef DocTypes As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim UnloadedComponentPathNames As System.Object
Dim UnloadedComponentReferencedConfigurationNames As System.Object
Dim ReasonForUnloadingComponents As System.Object
Dim DocTypes As System.Object
Dim value As System.Object

value = instance.GetUnloadedComponentNames(UnloadedComponentPathNames, UnloadedComponentReferencedConfigurationNames, ReasonForUnloadingComponents, DocTypes)
```

### C#

```csharp
System.object GetUnloadedComponentNames(
   out System.object UnloadedComponentPathNames,
   out System.object UnloadedComponentReferencedConfigurationNames,
   out System.object ReasonForUnloadingComponents,
   out System.object DocTypes
)
```

### C++/CLI

```cpp
System.Object^ GetUnloadedComponentNames(
   [Out] System.Object^ UnloadedComponentPathNames,
   [Out] System.Object^ UnloadedComponentReferencedConfigurationNames,
   [Out] System.Object^ ReasonForUnloadingComponents,
   [Out] System.Object^ DocTypes
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UnloadedComponentPathNames`: Array of the paths of the unloaded components
- `UnloadedComponentReferencedConfigurationNames`: Array of the referenced configuration names of the unloaded components
- `ReasonForUnloadingComponents`: Array indicating the reason each component is unloaded as defined by [swComponentLoadStatus_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swComponentLoadStatus_e.html)
- `DocTypes`: Array of document types as defined in [swDocumentTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)

### Return Value

Array of the names of the unloaded components

## VBA Syntax

See [AssemblyDoc::GetUnloadedComponentNames](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~GetUnloadedComponentNames.html).

## Examples

[Get Hidden Components Filenames (C#)](Get_Hidden_Components_Filenames_Example_CSharp.htm)
[Get Hidden Components Filenames (VB.NET)](Get_Hidden_Components_Filenames_Example_VBNET.htm)
[Get Hidden Components Filenames (VBA)](Get_Hidden_Components_Filenames_Example_VB.htm)

## Remarks

This method is useful when the assembly document was opened with **[Quick View/Selective open](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDocumentSpecification~Selective.html)** or [**Do not load hidden components**](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDocumentSpecification~IgnoreHiddenComponents.html).

To get whether an assembly has hidden or suppressed unloaded components, call [IAssemblyDoc::HasUnloadedComponents](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~HasUnloadedComponents.html).

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IComponent2::HasUnloadedComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~HasUnloadedComponents.html)
[IComponent2::GetUnloadedComponentNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetUnloadedComponentNames.html)
[IComponent2::GetHiddenUnloadedChildrenCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetHiddenUnloadedChildrenCount.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
