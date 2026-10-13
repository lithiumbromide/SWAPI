---
title: "EditPart2 Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "EditPart2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~EditPart2.html"
---

# EditPart2 Method (IAssemblyDoc)

Edits the selected part within the context of an assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function EditPart2( _
   ByVal Silent As System.Boolean, _
   ByVal AllowReadOnly As System.Boolean, _
   ByRef Information As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim Silent As System.Boolean
Dim AllowReadOnly As System.Boolean
Dim Information As System.Integer
Dim value As System.Integer

value = instance.EditPart2(Silent, AllowReadOnly, Information)
```

### C#

```csharp
System.int EditPart2(
   System.bool Silent,
   System.bool AllowReadOnly,
   ref System.int Information
)
```

### C++/CLI

```cpp
System.int EditPart2(
   System.bool Silent,
   System.bool AllowReadOnly,
   System.int% Information
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Silent`: True to suppress messages to user, false to not
- `AllowReadOnly`: True to allow editing of read-only parts, false to not
- `Information`: Status as defined in [swEditPartCommandStatus_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swEditPartCommandStatus_e.html)

### Return Value

swEditPartSuccessful if successful

## VBA Syntax

See [AssemblyDoc::EditPart2](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~EditPart2.html).

## Examples

[Create Plane thru 3 Points In-context (VBA)](Create_Plane_Thru_3_Points_In-context_Example_VB.htm)
[Suppress Component Feature (C#)](Suppress_Component_Feature_Example_CSharp.htm)
[Suppress Component Feature (VB.NET)](Suppress_Component_Feature_Example_VBNET.htm)
[Suppress Component Feature (VBA)](Suppress_Component_Feature_Example_VB.htm)
[Insert Cavity (C#)](Insert_Cavity_Example_CSharp.htm)
[Insert Cavity (VB.NET)](Insert_Cavity_Example_VBNET.htm)
[Insert Cavity (VBA)](Insert_Cavity_Example_VB.htm)

## Remarks

This method allows you to control the display of dialog boxes and edit a read-only document. To return to editing the assembly, use [IAssemblyDoc::EditAssembly](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~EditAssembly.html).

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
