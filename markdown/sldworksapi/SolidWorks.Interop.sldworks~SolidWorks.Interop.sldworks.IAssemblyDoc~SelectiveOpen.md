---
title: "SelectiveOpen Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "SelectiveOpen"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SelectiveOpen.html"
---

# SelectiveOpen Method (IAssemblyDoc)

Selectively opens the components of an assembly that is opened in Large Design Review mode.

## Syntax

### Visual Basic (Declaration)

```vb
Function SelectiveOpen( _
   ByVal SelectedComponents As System.Boolean, _
   ByVal OpenLightWeight As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim SelectedComponents As System.Boolean
Dim OpenLightWeight As System.Boolean
Dim value As System.Boolean

value = instance.SelectiveOpen(SelectedComponents, OpenLightWeight)
```

### C#

```csharp
System.bool SelectiveOpen(
   System.bool SelectedComponents,
   System.bool OpenLightWeight
)
```

### C++/CLI

```cpp
System.bool SelectiveOpen(
   System.bool SelectedComponents,
   System.bool OpenLightWeight
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SelectedComponents`: True to open only the components in the current selection list, false to open all of the components in the assembly
- `OpenLightWeight`: True to open the components in lightweight mode, false to not

### Return Value

True if successful, false if not (see **Remarks**)

## VBA Syntax

See [AssemblyDoc::SelectiveOpen](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~SelectiveOpen.html).

## Examples

[Open Assembly in Large Design Review Mode (VBA)](Open_Assembly_in_Large_Design_Review_Mode_Example_VB.htm)
[Open Assembly in Large Design Review Mode (VB.NET)](Open_Assembly_in_Large_Design_Review_Mode_Example_VBNET.htm)
[Open Assembly in Large Design Review Mode (C#)](Open_Assembly_in_Large_Design_Review_Mode_Example_CSharp.htm)

## Remarks

This method only works for assemblies that are opened in Large Design Review mode.

To open an assembly in Large Design Review mode:

1. Call [ISldWorks::GetOpenDocSpec](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetOpenDocSpec.html) to create an instance of [IDocumentSpecification](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDocumentSpecification.html).
2. Set [IDocumentSpecification::ViewOnly](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDocumentSpecification~ViewOnly.html) to true.
3. Call [ISldWorks::OpenDoc7](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~OpenDoc7.html), passing it the instance of IDocumentSpecification.

Before calling this method, call [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) to select the components that you want to open.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[ISldWorks::OpenDoc6 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc6.html)
[IAssemblyDoc::GetComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetComponents.html)
[IAssemblyDoc::GetLightWeightComponentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetLightWeightComponentCount.html)
[IAssemblyDoc::MakeLightWeight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~MakeLightWeight.html)
[IAssemblyDoc::ResolveAllLightweight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ResolveAllLightweight.html)
[IAssemblyDoc::ResolveAllLightWeightComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ResolveAllLightWeightComponents.html)
[IAssemblyDoc::ResolveOutOfDateLightWeightComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ResolveOutOfDateLightWeightComponents.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
