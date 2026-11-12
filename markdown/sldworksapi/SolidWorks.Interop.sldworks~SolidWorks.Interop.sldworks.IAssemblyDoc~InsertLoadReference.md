---
title: "InsertLoadReference Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "InsertLoadReference"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertLoadReference.html"
---

# InsertLoadReference Method (IAssemblyDoc)

Creates a mate load reference to the specified or selected mate.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertLoadReference( _
   ByVal Mate As Mate2 _
) As MateLoadReference
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim Mate As Mate2
Dim value As MateLoadReference

value = instance.InsertLoadReference(Mate)
```

### C#

```csharp
MateLoadReference InsertLoadReference(
   Mate2 Mate
)
```

### C++/CLI

```cpp
MateLoadReference^ InsertLoadReference(
   Mate2^ Mate
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Mate`: [Mate](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMate2.html) to which to add a mate load reference; if NULL passed in, then the mate must already be selected

### Return Value

[IMateLoadReference](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMateLoadReference.html)

## VBA Syntax

See [AssemblyDoc::InsertLoadReference](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~InsertLoadReference.html).

## Examples

[Insert Mate Load Reference (C#)](Insert_Mate_Load_Reference_Example_CSharp.htm)
[Insert Mate Load Reference (VB.NET)](Insert_Mate_Load_Reference_Example_VBNET.htm)
[Insert Mate Load Reference (VBA)](Insert_Mate_Load_Reference_Example_VB.htm)

## Remarks

The supplemental faces for the mate load reference must be selected before using this method. SOLIDWORKS determines which components own the selected supplemental faces and matches them to the components associated with the specified or selected mate. If the component of a selected supplemental face does not match either of the components of the mate, then that face is ignored.

This method rebuilds the FeatureManager design tree, which can be a time-consuming operation if the FeatureManage design tree is large. If using this method to add many load references at once, use [IFeatureManager::EnableFeatureTree](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~EnableFeatureTree.html) before and after using IAssemblyDoc::InsertLoadReference to disable and then re-enable rebuilding the FeatureManager design tree.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
