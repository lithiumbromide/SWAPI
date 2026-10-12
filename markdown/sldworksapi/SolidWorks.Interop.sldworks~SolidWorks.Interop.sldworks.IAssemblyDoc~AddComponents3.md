---
title: "AddComponents3 Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "AddComponents3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddComponents3.html"
---

# AddComponents3 Method (IAssemblyDoc)

Adds multiple components to the assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddComponents3( _
   ByVal Names As System.Object, _
   ByVal Transforms As System.Object, _
   ByVal CoordinateSystemNames As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim Names As System.Object
Dim Transforms As System.Object
Dim CoordinateSystemNames As System.Object
Dim value As System.Object

value = instance.AddComponents3(Names, Transforms, CoordinateSystemNames)
```

### C#

```csharp
System.object AddComponents3(
   System.object Names,
   System.object Transforms,
   System.object CoordinateSystemNames
)
```

### C++/CLI

```cpp
System.Object^ AddComponents3(
   System.Object^ Names,
   System.Object^ Transforms,
   System.Object^ CoordinateSystemNames
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Names`: Array of full path names of components
- `Transforms`: Array of transformation matrix doubles
- `CoordinateSystemNames`: Array of coordinate system names

### Return Value

Array of [IComponent2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) objects

## VBA Syntax

See [AssemblyDoc::AddComponents3](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~AddComponents3.html).

## Examples

[Add Components (C#)](Add_Components_Example_CSharp.htm)
[Add Components (VB.NET)](Add_Components_Example_VBNET.htm)
[Add Components (VBA)](Add_Components_Example_VB.htm)

## Remarks

Transforms contains an array of [(Names count) x 16] doubles. This parameter stores one transformation matrix of 16 doubles for each component in Names. If a component's transformation matrix is null, then the component is placed in the assembly such that the component's user-defined coordinate system coincides exactly with the default coordinate system of the assembly (no transformation). See [IMathTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html) for details about transformation matrices.

CoordinateSystemNames contains a user-defined coordinate system name for each component in Names. If a component's user-defined coordinate system is an empty string, then the component is placed in the assembly with respect to the default coordinate system of the component.

**TIP**: See [ISldWorks::OpenDoc6](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~OpenDoc6.html) for tips on how to avoid using large amounts of memory when opening up multiple parts to add to an assembly

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::IAddComponents3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IAddComponents3.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
