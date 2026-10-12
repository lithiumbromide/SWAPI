---
title: "AddComponent4 Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "AddComponent4"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddComponent4.html"
---

# AddComponent4 Method (IAssemblyDoc)

Obsolete. Superseded by [IAssemblyDoc::AddComponent5](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~AddComponent5.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddComponent4( _
   ByVal CompName As System.String, _
   ByVal ConfigName As System.String, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As Component2
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim CompName As System.String
Dim ConfigName As System.String
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As Component2

value = instance.AddComponent4(CompName, ConfigName, X, Y, Z)
```

### C#

```csharp
Component2 AddComponent4(
   System.string CompName,
   System.string ConfigName,
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
Component2^ AddComponent4(
   System.String^ CompName,
   System.String^ ConfigName,
   System.double X,
   System.double Y,
   System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CompName`: Path name of a loaded part or assembly to add as a component (see **Remarks**)
- `ConfigName`: Name of the configuration from which to load the component (see Remarks)
- `X`: X coordinate of the component center
- `Y`: Y coordinate of the component center
- `Z`: Z coordinate of the component center

### Return Value

[IComponent2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html)

## VBA Syntax

See [AssemblyDoc::AddComponent4](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~AddComponent4.html).

## Examples

[Add Component and Mate (C++)](Add_Component_and_Mate_Example_CPlusPlus_COM.htm)

## Remarks

The specified file must be loaded in memory. A file is loaded into memory when you load the file in your SOLIDWORKS Design session ([ISldWorks::OpenDoc6](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~OpenDoc6.html)) or open an assembly that already contains the file.

If configName is empty or specifies a configuration that does not exist, then the current configuration is used.

If you want to add the component at a position relative to the root component, use [IComponent2::Transform2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~Transform2.html) to reposition the component immediately after calling this method. Or, you can use [IAssemblyDoc::AddComponents](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~AddComponents.html) or [IAssemblyDoc::AddComponents2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~IAddComponents2.html) to specify the transform when inserting a component, insert as many components as you want at once, and rotate and scale the component through the transform matrix.

IMPORTANT: The x, y, and z parameters of this method are relative to the bounding box of the component. Only use this method if you want to approximately position the component. Use IComponent2::Transform2 if you want to more precisely position the component.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::InsertEnvelope Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertEnvelope.html)
[IAssemblyDoc::ReplaceComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ReplaceComponents.html)

## Availability

SOLIDWORKS 2003 SP5, Revision Number 11.5
