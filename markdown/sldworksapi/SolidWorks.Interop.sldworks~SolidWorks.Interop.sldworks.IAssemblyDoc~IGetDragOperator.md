---
title: "IGetDragOperator Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "IGetDragOperator"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IGetDragOperator.html"
---

# IGetDragOperator Method (IAssemblyDoc)

Gets the drag operator for dynamic drag operations in this assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetDragOperator() As DragOperator
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim value As DragOperator

value = instance.IGetDragOperator()
```

### C#

```csharp
DragOperator IGetDragOperator()
```

### C++/CLI

```cpp
DragOperator^ IGetDragOperator();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IDragOperator](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~IGetDragOperator.html)

## VBA Syntax

See [AssemblyDoc::IGetDragOperator](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~IGetDragOperator.html).

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::GetDragOperator Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetDragOperator.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
