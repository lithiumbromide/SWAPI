---
title: "GetVisibleComponentsInView Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "GetVisibleComponentsInView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetVisibleComponentsInView.html"
---

# GetVisibleComponentsInView Method (IAssemblyDoc)

Gets a list of visible components in this assembly to save as solid bodies.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetVisibleComponentsInView() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim value As System.Object

value = instance.GetVisibleComponentsInView()
```

### C#

```csharp
System.object GetVisibleComponentsInView()
```

### C++/CLI

```cpp
System.Object^ GetVisibleComponentsInView();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of visible [components](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) in this assembly

## VBA Syntax

See [AssemblyDoc::GetVisibleComponentsInView](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~GetVisibleComponentsInView.html).

## Remarks

One way to save an assembly as a multibody part document is to save the visible components in the assembly document as solid bodies. This method corresponds to the Exterior Components option in the File, Save As dialog box. For more information about saving assemblies as multibody documents, see SOLIDWORKS Help.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::IGetVisibleComponentsInView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IGetVisibleComponentsInView.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
