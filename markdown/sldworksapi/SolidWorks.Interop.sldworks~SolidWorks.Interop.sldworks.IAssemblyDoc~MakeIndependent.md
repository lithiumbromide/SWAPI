---
title: "MakeIndependent Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "MakeIndependent"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~MakeIndependent.html"
---

# MakeIndependent Method (IAssemblyDoc)

Makes the selected component independent.

## Syntax

### Visual Basic (Declaration)

```vb
Function MakeIndependent( _
   ByVal FileName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim FileName As System.String
Dim value As System.Boolean

value = instance.MakeIndependent(FileName)
```

### C#

```csharp
System.bool MakeIndependent(
   System.string FileName
)
```

### C++/CLI

```cpp
System.bool MakeIndependent(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Path and file name where to save the new part (see **Remarks**)

### Return Value

True if the component is made independent, false if not

## VBA Syntax

See [AssemblyDoc::MakeIndependent](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~MakeIndependent.html).

## Examples

[Make Component Independent (C#)](Make_Component_Independent_Example_CSharp.htm)
[Make Component Independent (VB.NET)](Make_Component_Independent_Example_VBNET.htm)
[Make Component Independent (VBA)](Make_Component_Independent_Example_VB.htm)

## Remarks

Making a component independent saves the component as a new file within the assembly and to the specified path and file name. The new part is referenced in the assembly.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::ReplaceComponents2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ReplaceComponents2.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
