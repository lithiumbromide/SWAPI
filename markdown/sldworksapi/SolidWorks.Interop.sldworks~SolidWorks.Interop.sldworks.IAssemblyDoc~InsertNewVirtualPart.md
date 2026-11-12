---
title: "InsertNewVirtualPart Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "InsertNewVirtualPart"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertNewVirtualPart.html"
---

# InsertNewVirtualPart Method (IAssemblyDoc)

Creates a new part in the context of an assembly and saves the part internally in the assembly file as a virtual component.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertNewVirtualPart( _
   ByVal FaceOrPlaneToSelect As System.Object, _
   ByRef InsertedComponent As Component2 _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim FaceOrPlaneToSelect As System.Object
Dim InsertedComponent As Component2
Dim value As System.Integer

value = instance.InsertNewVirtualPart(FaceOrPlaneToSelect, InsertedComponent)
```

### C#

```csharp
System.int InsertNewVirtualPart(
   System.object FaceOrPlaneToSelect,
   out Component2 InsertedComponent
)
```

### C++/CLI

```cpp
System.int InsertNewVirtualPart(
   System.Object^ FaceOrPlaneToSelect,
   [Out] Component2^ InsertedComponent
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FaceOrPlaneToSelect`: Plane or planar face
- `InsertedComponent`: New part inserted as virtual component

### Return Value

Error as defined by [swInsertNewPartErrorCode_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInsertNewPartErrorCode_e.html)

## VBA Syntax

See [AssemblyDoc::InsertNewVirtualPart](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~InsertNewVirtualPart.html).

## Examples

[Insert New Virtual Component (VB.NET)](Insert_New_Virtual_Component_Example_VBNET.htm)
[Insert New Virtual Component (VBA)](Insert_New_Virtual_Component_Example_VB.htm)
[Insert New Virtual Component (C#)](Insert_New_Virtual_Component_Example_CSharp.htm)
[Insert New Instance of Virtual Component (VBA)](Insert_New_Instance_of_Virtual_Component_Example_VB.htm)
[Insert New Instance of Virtual Component (VB.NET)](Insert_New_Instance_of_Virtual_Component_Example_VBNET.htm)
[Insert New Instance of Virtual Component (C#)](Insert_New_Instance_of_Virtual_Component_Example_CSharp.htm)

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IComponent2::IsVirtual Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsVirtual.html)
[IModelDocExtension::IsVirtualComponent3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IsVirtualComponent3.html)
[IAssemblyDoc::InsertNewVirtualAssembly Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertNewVirtualAssembly.html)
[IAssemblyDoc::InsertNewAssembly Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertNewAssembly.html)
[IComponent2::MakeVirtual Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~MakeVirtual.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
