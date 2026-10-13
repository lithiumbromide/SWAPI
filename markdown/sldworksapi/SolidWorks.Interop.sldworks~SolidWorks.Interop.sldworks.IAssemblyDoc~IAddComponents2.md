---
title: "IAddComponents2 Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "IAddComponents2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IAddComponents2.html"
---

# IAddComponents2 Method (IAssemblyDoc)

Obsolete. Superseded by [IAssemblyDoc::IAddComponents3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~IAddComponents3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IAddComponents2( _
   ByRef Count As System.Integer, _
   ByRef Names As System.String, _
   ByRef Transforms As System.Double _
) As Component2
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim Count As System.Integer
Dim Names As System.String
Dim Transforms As System.Double
Dim value As Component2

value = instance.IAddComponents2(Count, Names, Transforms)
```

### C#

```csharp
Component2 IAddComponents2(
   ref System.int Count,
   ref System.string Names,
   ref System.double Transforms
)
```

### C++/CLI

```cpp
Component2^ IAddComponents2(
   System.int% Count,
   System.String^% Names,
   System.double% Transforms
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of components to add
- `Names`: - in-process, unmanaged C++: Pointer to an array of strings of component file names

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.
- `Transforms`: - in-process, unmanaged C++: Pointer to an array of doubles of component transforms

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

### Return Value

- in-process, unmanaged C++: Pointer to an array of [IComponent2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## VBA Syntax

See [AssemblyDoc::IAddComponents2](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~IAddComponents2.html).

## Examples

[Add Components and Transforms (C++)](Add_Components_and_Transforms_Example_CPlusPlus_COM.htm)

## Remarks

The array of file names represents all of the components that you want to add to the assembly. If there is more than one instance of a given component, make sure to specify the file name for each instance of the component that you want to add.

The array of transforms consists of [count x 16] doubles. There should be one transform for each component to be added.

The application must allocate the array of components, and it is also responsible for releasing the returned array of components.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::AddComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddComponents.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
