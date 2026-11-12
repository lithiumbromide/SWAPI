---
title: "IAssemblyDoc Interface"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html"
---

# IAssemblyDoc Interface

Allows access to functions that perform assembly operations; for example, adding new components, adding mate conditions, hiding, and exploding components.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IAssemblyDoc
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
```

### C#

```csharp
public interface IAssemblyDoc
```

### C++/CLI

```cpp
public interface class IAssemblyDoc
```

## VBA Syntax

See [AssemblyDoc](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc.html).

## Examples

[Run Interference Detection (C#)](Run_Interference_Detection_Example_CSharp.htm)
[Run Interference Detection (VB.NET)](Run_Interference_Detection_Example_VBNET.htm)
[Run Interference Detection (VBA)](Run_Interference_Detection_Example_VB.htm)
[Insert and Save Virtual Assembly (C#)](Insert_and_Save_Virtual_Assembly_Example_CSharp.htm)
[Insert and Save Virtual Assembly (VB.NET)](Insert_and_Save_Virtual_Assembly_Example_VBNET.htm)
[Insert and Save Virtual Assembly (VBA)](Insert_and_Save_Virtual_Assembly_Example_VB.htm)
[Add Components (C#)](Add_Components_Example_CSharp.htm)
[Add Components (VB.NET)](Add_Components_Example_VBNET.htm)
[Add Components (VBA)](Add_Components_Example_VB.htm)
[Add Component and Mate (C++)](Add_Component_and_Mate_Example_CPlusPlus_COM.htm)
[Add Component and Mate (VBA)](Add_Component_and_Mate_Example_VB.htm)
[Insert MidSurface in Assembly (C#)](Insert_MidSurface_in_Component_Example_CSharp.htm)
[Insert MidSurface in Component (VB.NET)](Insert_MidSurface_in_Component_Example_VBNET.htm)
[Insert MidSurface in Component (VBA)](Insert_MidSurface_in_Component_Example_VB.htm)
[Create Auto Route (VBA)](Create_Auto_Route_Example_VB.htm)
[Create Auto Route (VB.NET)](Create_Auto_Route_Example_VBNET.htm)
[Create Auto Route (C#)](Create_Auto_Route_Example_CSharp.htm)
[Add Component and Mate (VB.NET)](Add_Component_and_Mate_Example_VBNET.htm)
[Add Component and Mate Example (C#)](Add_Component_and_Mate_Example_CSharp.htm)

## Remarks

The SOLIDWORKS API includes functions that are common to all document types; for example, determining the file name associated with a document is a common operation. To expose common document-level functions, the SOLIDWORKS API uses the [IModelDoc2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) object.

Events are implemented with delegates in the Microsoft .NET Framework. See the [Overview](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks_namespace.html) topic for a list of delegates for this interface.

## Accessors

[ICollisionDetectionManager::GetAssembly](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager~GetAssembly.html)

## Access Diagram

[AssemblyDoc](SWObjectModel.pdf#AssemblyDoc)

## See Also

[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
