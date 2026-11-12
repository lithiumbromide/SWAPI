---
title: "InsertNewVirtualAssembly Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "InsertNewVirtualAssembly"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertNewVirtualAssembly.html"
---

# InsertNewVirtualAssembly Method (IAssemblyDoc)

Creates a new assembly from this assembly and saves it internally as a virtual component.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertNewVirtualAssembly( _
   ByRef InsertedComponent As Component2 _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim InsertedComponent As Component2
Dim value As System.Integer

value = instance.InsertNewVirtualAssembly(InsertedComponent)
```

### C#

```csharp
System.int InsertNewVirtualAssembly(
   out Component2 InsertedComponent
)
```

### C++/CLI

```cpp
System.int InsertNewVirtualAssembly(
   [Out] Component2^ InsertedComponent
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `InsertedComponent`: New assembly inserted as virtual component

### Return Value

Error code as defined by [swInsertNewPartErrorCode_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInsertNewPartErrorCode_e.html)

## VBA Syntax

See [AssemblyDoc::InsertNewVirtualAssembly](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~InsertNewVirtualAssembly.html).

## Examples

[Insert New Virtual Assembly (VBA)](Insert_New_Virtual_Assembly_Example_VB.htm)
[Insert New Virtual Assembly (VB.NET)](Insert_New_Virtual_Assembly_Example_VBNET.htm)
[Insert New Virtual Assembly (C#)](Insert_New_Virtual_Assembly_Example_CSharp.htm)

## Remarks

If nothing is pre-selected, this method inserts the virtual assembly into the main assembly. If a sub-assembly is pre-selected, it inserts the virtual assembly into the sub-assembly.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::InsertNewVirtualPart Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertNewVirtualPart.html)
[IComponent2::IsVirtual Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsVirtual.html)
[IModelDocExtension::IsVirtualComponent3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IsVirtualComponent3.html)
[IAssemblyDoc::InsertNewAssembly Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertNewAssembly.html)
[IComponent2::MakeVirtual Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~MakeVirtual.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
