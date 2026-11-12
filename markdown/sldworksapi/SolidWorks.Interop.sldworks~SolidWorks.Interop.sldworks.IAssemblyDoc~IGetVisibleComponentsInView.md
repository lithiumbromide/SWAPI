---
title: "IGetVisibleComponentsInView Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "IGetVisibleComponentsInView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IGetVisibleComponentsInView.html"
---

# IGetVisibleComponentsInView Method (IAssemblyDoc)

Gets a list of visible components in this assembly to save as solid bodies.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetVisibleComponentsInView( _
   ByVal Count As System.Integer _
) As Component2
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim Count As System.Integer
Dim value As Component2

value = instance.IGetVisibleComponentsInView(Count)
```

### C#

```csharp
Component2 IGetVisibleComponentsInView(
   System.int Count
)
```

### C++/CLI

```cpp
Component2^ IGetVisibleComponentsInView(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of visible components in this assembly

### Return Value

- in-process, unmanaged C++: Pointer to an array of visible [components](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) in this assembly of size count

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

One way to save an assembly as a multibody part document is to save the visible components in the assembly document as solid bodies. This method corresponds to the Exterior Components option in the File, Save As dialog box. For more information about saving assemblies as multibody documents, see SOLIDWORKS Help.

Call [IAssemblyDoc::GetVisibleComponentsInViewCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~GetVisibleComponentsInViewCount.html) before calling this method.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::GetVisibleComponentsInView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetVisibleComponentsInView.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
