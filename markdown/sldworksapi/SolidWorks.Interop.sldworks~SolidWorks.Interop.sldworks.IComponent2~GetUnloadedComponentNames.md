---
title: "GetUnloadedComponentNames Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "GetUnloadedComponentNames"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetUnloadedComponentNames.html"
---

# GetUnloadedComponentNames Method (IComponent2)

Gets the component's unloaded children components' path names, referenced configuration names, reasons why they are unloaded, document types, and names.

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
Dim instance As IComponent2
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

- `UnloadedComponentPathNames`: Array of children components' path names
- `UnloadedComponentReferencedConfigurationNames`: Array of children components' referenced configuration names
- `ReasonForUnloadingComponents`: Array indicating the reason each child component is unloaded as defined by [swComponentLoadStatus_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swComponentLoadStatus_e.html)
- `DocTypes`: Array of document types as defined in [swDocumentTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)

### Return Value

Array of children components' names

## VBA Syntax

See [Component2::GetUnloadedComponentNames](ms-its:sldworksapivb6.chm::/sldworks~Component2~GetUnloadedComponentNames.html).

## Remarks

This method is useful when the assembly document was opened with **[Quick View/Selective open](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDocumentSpecification~Selective.html)**.

To get whether a component has hidden or suppressed children components, call [IComponent2::HasUnloadedComponents](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~HasUnloadedComponents.html).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::GetHiddenUnloadedChildrenCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetHiddenUnloadedChildrenCount.html)
[IComponent2::HasUnloadedComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~HasUnloadedComponents.html)
[IAssemblyDoc::GetUnloadedComponentNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetUnloadedComponentNames.html)
[IAssemblyDoc::HasUnloadedComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~HasUnloadedComponents.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
