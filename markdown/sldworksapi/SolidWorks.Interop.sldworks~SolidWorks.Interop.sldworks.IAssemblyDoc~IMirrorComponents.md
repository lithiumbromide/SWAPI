---
title: "IMirrorComponents Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "IMirrorComponents"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IMirrorComponents.html"
---

# IMirrorComponents Method (IAssemblyDoc)

Obsolete. Superseded by [IAssemblyDoc::MirrorComponents2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~MirrorComponents2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IMirrorComponents( _
   ByVal Plane As System.Object, _
   ByVal InstanceCount As System.Integer, _
   ByRef ComponentsToInstance As Component2, _
   ByVal MirrorCount As System.Integer, _
   ByRef ComponentsToMirror As Component2, _
   ByVal NameCount As System.Integer, _
   ByRef MirroredComponentFilenames As System.String, _
   ByVal RecreateMates As System.Boolean, _
   ByVal ComponentModifier As System.Integer, _
   ByVal ComponentNameModifier As System.String, _
   ByVal MirroredFileLocation As System.String, _
   ByVal CopyCustomProperties As System.Boolean _
) As Component2
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim Plane As System.Object
Dim InstanceCount As System.Integer
Dim ComponentsToInstance As Component2
Dim MirrorCount As System.Integer
Dim ComponentsToMirror As Component2
Dim NameCount As System.Integer
Dim MirroredComponentFilenames As System.String
Dim RecreateMates As System.Boolean
Dim ComponentModifier As System.Integer
Dim ComponentNameModifier As System.String
Dim MirroredFileLocation As System.String
Dim CopyCustomProperties As System.Boolean
Dim value As Component2

value = instance.IMirrorComponents(Plane, InstanceCount, ComponentsToInstance, MirrorCount, ComponentsToMirror, NameCount, MirroredComponentFilenames, RecreateMates, ComponentModifier, ComponentNameModifier, MirroredFileLocation, CopyCustomProperties)
```

### C#

```csharp
Component2 IMirrorComponents(
   System.object Plane,
   System.int InstanceCount,
   ref Component2 ComponentsToInstance,
   System.int MirrorCount,
   ref Component2 ComponentsToMirror,
   System.int NameCount,
   ref System.string MirroredComponentFilenames,
   System.bool RecreateMates,
   System.int ComponentModifier,
   System.string ComponentNameModifier,
   System.string MirroredFileLocation,
   System.bool CopyCustomProperties
)
```

### C++/CLI

```cpp
Component2^ IMirrorComponents(
   System.Object^ Plane,
   System.int InstanceCount,
   Component2^% ComponentsToInstance,
   System.int MirrorCount,
   Component2^% ComponentsToMirror,
   System.int NameCount,
   System.String^% MirroredComponentFilenames,
   System.bool RecreateMates,
   System.int ComponentModifier,
   System.String^ ComponentNameModifier,
   System.String^ MirroredFileLocation,
   System.bool CopyCustomProperties
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Plane`: Plane or planar face about which to mirror the components
- `InstanceCount`: Number of instances of the components to mirror
- `ComponentsToInstance`: Array of instances of the [component](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) to mirror
- `MirrorCount`: Number of components to mirror
- `ComponentsToMirror`: Array of [components](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) to mirror
- `NameCount`: Number of filenames for the newly created mirrored assemblies or parts
- `MirroredComponentFilenames`: Array of filenames for the newly created mirrored assemblies or parts
- `RecreateMates`: True to preserve any mates between the selected components if more than one component is to be mirrored, false to not
- `ComponentModifier`: Prefix or suffix for the newly mirrored components if MirroredComponentFilenames is not specified, as defined by [swMirrorComponentNameModifier_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMirrorComponentNameModifier_e.html)
- `ComponentNameModifier`: String to add to the prefix or suffix of the name of the newly mirrored components if MirroredComponentFilenames is not specified
- `MirroredFileLocation`: Name of the folder where to store the file of the newly created mirrored components
- `CopyCustomProperties`: True to copy the custom properties from the selected components to the mirrored components, false to not

### Return Value

- in-process, unmanaged C++: Pointer to an array of newly created [components](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## VBA Syntax

See [AssemblyDoc::IMirrorComponents](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~IMirrorComponents.html).

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::MirrorComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~MirrorComponents.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
