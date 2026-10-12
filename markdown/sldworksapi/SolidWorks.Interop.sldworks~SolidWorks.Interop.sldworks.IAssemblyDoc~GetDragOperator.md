---
title: "GetDragOperator Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "GetDragOperator"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetDragOperator.html"
---

# GetDragOperator Method (IAssemblyDoc)

Gets the drag operator for dynamic drag operations in this assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDragOperator() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim value As System.Object

value = instance.GetDragOperator()
```

### C#

```csharp
System.object GetDragOperator()
```

### C++/CLI

```cpp
System.Object^ GetDragOperator();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Object for the drag operator

## VBA Syntax

See [AssemblyDoc::GetDragOperator](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~GetDragOperator.html).

## Examples

[Rotate Assembly Component on Axis Using IDragOperator::Drag (C#)](Rotate_Assembly_Component_on_Axis_Example_CSharp.htm)
[Rotate Assembly Component on Axis Using IDragOperator::Drag (VB.NET)](Rotate_Assembly_Component_on_Axis_Example_VBNET.htm)
[Rotate Assembly Component on Axis Using IDragOperator::Drag (VBA)](Rotate_Assembly_Component_on_Axis_Example_VB.htm)

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::IGetDragOperator Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IGetDragOperator.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
