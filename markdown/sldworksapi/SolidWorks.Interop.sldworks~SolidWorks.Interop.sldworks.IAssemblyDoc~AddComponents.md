---
title: "AddComponents Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "AddComponents"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddComponents.html"
---

# AddComponents Method (IAssemblyDoc)

Obsolete. Superseded by [IAssemblyDoc::AddComponents3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~AddComponents3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddComponents( _
   ByVal Names As System.Object, _
   ByVal Transforms As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim Names As System.Object
Dim Transforms As System.Object
Dim value As System.Object

value = instance.AddComponents(Names, Transforms)
```

### C#

```csharp
System.object AddComponents(
   System.object Names,
   System.object Transforms
)
```

### C++/CLI

```cpp
System.Object^ AddComponents(
   System.Object^ Names,
   System.Object^ Transforms
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Names`: Array of strings component file names
- `Transforms`: Array of doubles of the component transforms

### Return Value

Array of objects of newly created components

## VBA Syntax

See [AssemblyDoc::AddComponents](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~AddComponents.html).

## Examples

[Add Components (VBA)](Add_Components_Example_VB.htm)

## Remarks

The array of file names represents all of the components that are added to the assembly. If there is more than one instance of a given component, make sure you add the file name of the component for each instance of the component.

The array of transforms consists of [count x 16] doubles. There should be one transform for each component being added.

**TIP**: See [ISldWorks::OpenDoc6](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~OpenDoc6.html) for tips on how to avoid using large amounts of memory when opening up multiple parts to add to an assembly

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::IAddComponents2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IAddComponents2.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
