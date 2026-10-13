---
title: "InsertNewAssembly Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "InsertNewAssembly"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertNewAssembly.html"
---

# InsertNewAssembly Method (IAssemblyDoc)

Creates a new virtual sub-assembly and optionally saves it to the specified file.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertNewAssembly( _
   ByVal FileName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim FileName As System.String
Dim value As System.Integer

value = instance.InsertNewAssembly(FileName)
```

### C#

```csharp
System.int InsertNewAssembly(
   System.string FileName
)
```

### C++/CLI

```cpp
System.int InsertNewAssembly(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Full pathname of new sub-assembly document (**see Remarks**)

### Return Value

Error code as defined by [swInsertNewAssemblyErrorCode_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInsertNewAssemblyErrorCode_e.html)

## VBA Syntax

See [AssemblyDoc::InsertNewAssembly](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~InsertNewAssembly.html).

## Examples

[Insert and Save Virtual Assembly (C#)](Insert_and_Save_Virtual_Assembly_Example_CSharp.htm)
[Insert and Save Virtual Assembly (VB.NET)](Insert_and_Save_Virtual_Assembly_Example_VBNET.htm)
[Insert and Save Virtual Assembly (VBA)](Insert_and_Save_Virtual_Assembly_Example_VB.htm)

## Remarks

If **Tools > Options > System Options > Assemblies > Save new components to external files** is:

- selected, then this API creates a virtual sub-assembly and saves it to the file specified in FileName.
- not selected, then this API ignores FileName, does not save the sub-assembly, and creates only a virtual sub-assembly in the FeatureManager design tree.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::InsertNewVirtualAssembly Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertNewVirtualAssembly.html)
[IComponent2::SaveVirtualComponent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SaveVirtualComponent.html)
[IComponent2::IsVirtual Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsVirtual.html)
[IModelDocExtension::IsVirtualComponent3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IsVirtualComponent3.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
