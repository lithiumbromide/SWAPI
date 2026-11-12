---
title: "EditAssembly Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "EditAssembly"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~EditAssembly.html"
---

# EditAssembly Method (IAssemblyDoc)

Switches back to the assembly document for editing.

## Syntax

### Visual Basic (Declaration)

```vb
Sub EditAssembly()
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc

instance.EditAssembly()
```

### C#

```csharp
void EditAssembly()
```

### C++/CLI

```cpp
void EditAssembly();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [AssemblyDoc::EditAssembly](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~EditAssembly.html).

## Examples

[Create Plane thru 3 Points In-context (VBA)](Create_Plane_Thru_3_Points_In-context_Example_VB.htm)
[Suppress Component Feature (C#)](Suppress_Component_Feature_Example_CSharp.htm)
[Suppress Component Feature (VB.NET)](Suppress_Component_Feature_Example_VBNET.htm)
[Suppress Component Feature (VBA)](Suppress_Component_Feature_Example_VB.htm)
[Insert Cavity (C#)](Insert_Cavity_Example_CSharp.htm)
[Insert Cavity (VB.NET)](Insert_Cavity_Example_VBNET.htm)
[Insert Cavity (VBA)](Insert_Cavity_Example_VB.htm)

## Remarks

This method is used with [IAssemblyDoc::EditPart2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~EditPart2.html), which allows you to edit a part within the context of an assembly.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
