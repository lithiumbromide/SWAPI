---
title: "GetComponentByID Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "GetComponentByID"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetComponentByID.html"
---

# GetComponentByID Method (IAssemblyDoc)

Gets a top-level assembly component using its component ID.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetComponentByID( _
   ByVal ID As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim ID As System.Integer
Dim value As System.Object

value = instance.GetComponentByID(ID)
```

### C#

```csharp
System.object GetComponentByID(
   System.int ID
)
```

### C++/CLI

```cpp
System.Object^ GetComponentByID(
   System.int ID
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ID`: Component ID of top-level assembly component (see **Remarks**)

### Return Value

Top-level [component](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)

## VBA Syntax

See [AssemblyDoc::GetComponentByID](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~GetComponentByID.html).

## Examples

[Get Top-level Components Using Component IDs (C#)](Get_Top-level_Component_Using_Component_IDs_Example_CSharp.htm)
[Get Top-level Components Using Component IDs (VB.NET)](Get_Top-level_Component_Using_Component_IDs_Example_VBNET.htm)
[Get Top-level Components Using Component IDs (VBA)](Get_Top-level_Component_Using_Component_IDs_Example_VB.htm)

## Remarks

Call [IComponent2::GetID](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetID.html) before calling this method to get the component ID of the top-level assembly component to pass to this method.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::GetComponentByName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetComponentByName.html)
[IAssemblyDoc::GetComponents Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetComponents.html)
[IAssemblyDoc::IGetComponents Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IGetComponents.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
