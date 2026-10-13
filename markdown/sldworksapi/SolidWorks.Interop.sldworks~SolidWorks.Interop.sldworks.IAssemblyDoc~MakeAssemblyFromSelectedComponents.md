---
title: "MakeAssemblyFromSelectedComponents Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "MakeAssemblyFromSelectedComponents"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~MakeAssemblyFromSelectedComponents.html"
---

# MakeAssemblyFromSelectedComponents Method (IAssemblyDoc)

Creates a new assembly comprised of the selected components of this assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function MakeAssemblyFromSelectedComponents( _
   ByVal FileName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim FileName As System.String
Dim value As System.Boolean

value = instance.MakeAssemblyFromSelectedComponents(FileName)
```

### C#

```csharp
System.bool MakeAssemblyFromSelectedComponents(
   System.string FileName
)
```

### C++/CLI

```cpp
System.bool MakeAssemblyFromSelectedComponents(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Path and filename of the new assembly

### Return Value

True if a new assembly is created, false if not

## VBA Syntax

See [AssemblyDoc::MakeAssemblyFromSelectedComponents](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~MakeAssemblyFromSelectedComponents.html).

## Examples

[Make Assembly From Selected Components (VB.NET)](Make_Assembly_From_Selected_Components_Example_VBNET.htm)
[Make Assembly From Selected Components (VBA)](Make_Assembly_From_Selected_Components_Example_VB.htm)
[Make Assembly From Selected Components (C#)](Make_Assembly_From_Selected_Components_Example_CSharp.htm)

## Remarks

If **Tools > Options > System Options > Assemblies > Save new components to external files** is selected, then a virtual sub-assembly is created and saved to an external file. Be sure to save the parent assembly before calling this method.

If **Tools > Options > System Options > Assemblies > Save new components to external files** is not selected, then the `FileName` input parameter is ignored, and only a virtual sub-assembly is created.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
