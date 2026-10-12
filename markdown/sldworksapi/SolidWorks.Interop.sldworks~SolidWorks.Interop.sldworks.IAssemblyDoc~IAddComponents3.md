---
title: "IAddComponents3 Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "IAddComponents3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IAddComponents3.html"
---

# IAddComponents3 Method (IAssemblyDoc)

Adds multiple components to the assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function IAddComponents3( _
   ByVal Count As System.Integer, _
   ByRef Names As System.String, _
   ByRef Transforms As System.Double, _
   ByVal CoordinateSystemNameCount As System.Integer, _
   ByRef CoordinateSystemNames As System.String _
) As Component2
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim Count As System.Integer
Dim Names As System.String
Dim Transforms As System.Double
Dim CoordinateSystemNameCount As System.Integer
Dim CoordinateSystemNames As System.String
Dim value As Component2

value = instance.IAddComponents3(Count, Names, Transforms, CoordinateSystemNameCount, CoordinateSystemNames)
```

### C#

```csharp
Component2 IAddComponents3(
   System.int Count,
   ref System.string Names,
   ref System.double Transforms,
   System.int CoordinateSystemNameCount,
   ref System.string CoordinateSystemNames
)
```

### C++/CLI

```cpp
Component2^ IAddComponents3(
   System.int Count,
   System.String^% Names,
   System.double% Transforms,
   System.int CoordinateSystemNameCount,
   System.String^% CoordinateSystemNames
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of components to add
- `Names`: - in-process, unmanaged C++: Pointer to an array of strings of full path names of components to add

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.
- `Transforms`: - in-process, unmanaged C++: Pointer to an array of doubles of component transforms

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.
- `CoordinateSystemNameCount`: Number of coordinate system names in CoordinateSystemNames; include in the count all empty strings
- `CoordinateSystemNames`: - in-process, unmanaged C++: Pointer to an array of strings of coordinate system names

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

### Return Value

- in-process, unmanaged C++: Pointer to an array of [IComponent2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## VBA Syntax

See [AssemblyDoc::IAddComponents3](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~IAddComponents3.html).

## Remarks

Transforms contains an array of [Count x 16] doubles. This parameter stores one transformation matrix of 16 doubles for each component in Names. If a component's transformation matrix is null, then the component is placed in the assembly such that the component's user-defined coordinate system coincides exactly with the default coordinate system of the assembly (no transformation). See [IMathTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html) for details about transformation matrices.

CoordinateSystemNames contains a user-defined coordinate system name for each component in Names. If a component's user-defined coordinate system is an empty string, then the component is placed in the assembly with respect to the default coordinate system of the component.

The application must allocate the array of components, and it is also responsible for releasing the returned array of components.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::AddComponents3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddComponents3.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
