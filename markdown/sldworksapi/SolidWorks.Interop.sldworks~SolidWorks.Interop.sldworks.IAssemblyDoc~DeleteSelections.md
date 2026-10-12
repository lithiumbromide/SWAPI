---
title: "DeleteSelections Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "DeleteSelections"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~DeleteSelections.html"
---

# DeleteSelections Method (IAssemblyDoc)

Delete either the selected components of a subassembly or the subassembly of the selected component.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteSelections( _
   ByVal DeleteOptions As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim DeleteOptions As System.Integer
Dim value As System.Boolean

value = instance.DeleteSelections(DeleteOptions)
```

### C#

```csharp
System.bool DeleteSelections(
   System.int DeleteOptions
)
```

### C++/CLI

```cpp
System.bool DeleteSelections(
   System.int DeleteOptions
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DeleteOptions`: Type of selection to delete as defined in [swAssemblyDeleteOptions_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAssemblyDeleteOptions_e.html)

### Return Value

True if either the selected components of a subassembly are deleted or the subassembly of the selected component is deleted, false if not

## VBA Syntax

See [AssemblyDoc::DeleteSelections](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~DeleteSelections.html).

## Examples

[Delete Subassemblies (C#)](Delete_Subassemblies_Example_CSharp.htm)
[Delete Subassemblies (VB.NET)](Delete_Subassemblies_Example_VBNET.htm)
[Delete Subassemblies (VBA)](Delete_Subassemblies_Example_VB.htm)

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IModelDoc2::EditDelete Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditDelete.html)
[IModelDocExtension::DeleteSelection2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteSelection2.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
