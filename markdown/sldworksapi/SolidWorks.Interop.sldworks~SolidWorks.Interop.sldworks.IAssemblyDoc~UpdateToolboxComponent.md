---
title: "UpdateToolboxComponent Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "UpdateToolboxComponent"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~UpdateToolboxComponent.html"
---

# UpdateToolboxComponent Method (IAssemblyDoc)

Updates SOLIDWORKS Toolbox components in the specified assembly level using the current information in Toolbox settings.

## Syntax

### Visual Basic (Declaration)

```vb
Function UpdateToolboxComponent( _
   ByVal AssemblyLevelToUpdate As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim AssemblyLevelToUpdate As System.Integer
Dim value As System.Integer

value = instance.UpdateToolboxComponent(AssemblyLevelToUpdate)
```

### C#

```csharp
System.int UpdateToolboxComponent(
   System.int AssemblyLevelToUpdate
)
```

### C++/CLI

```cpp
System.int UpdateToolboxComponent(
   System.int AssemblyLevelToUpdate
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AssemblyLevelToUpdate`: Level in which to update SOLIDWORKS Toolbox components as defined in [swAssemblyLevelToUpdate_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAssemblyLevelToUpdate_e.html)

### Return Value

Status of updating the SOLIDWORKS Toolbox components as defined in [swAssemblyUpdateToolboxComponentStatus_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAssemblyUpdateToolboxComponentStatus_e.html)

## VBA Syntax

See [AssemblyDoc::UpdateToolboxComponent](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~UpdateToolboxComponent.html).

## Examples

[Update All Toolbox Components (C#)](Update_All_Toolbox_Components_Example_CSharp.htm)
[Update All Toolbox Components (VB.NET)](Update_All_Toolbox_Components_Example_VBNET.htm)
[Update All Toolbox Components (VBA)](Update_All_Toolbox_Components_Example_VB.htm)

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
