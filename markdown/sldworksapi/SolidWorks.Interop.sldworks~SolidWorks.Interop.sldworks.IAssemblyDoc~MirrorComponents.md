---
title: "MirrorComponents Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "MirrorComponents"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~MirrorComponents.html"
---

# MirrorComponents Method (IAssemblyDoc)

Obsolete. Superseded by [IAssemblyDoc::MirrorComponents2.](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~MirrorComponents2.html)

## Syntax

### Visual Basic (Declaration)

```vb
Function MirrorComponents( _
   ByVal Plane As System.Object, _
   ByVal ComponentsToInstance As System.Object, _
   ByVal ComponentsToMirror As System.Object, _
   ByVal MirroredComponentFilenames As System.Object, _
   ByVal RecreateMates As System.Boolean, _
   ByVal ComponentModifier As System.Integer, _
   ByVal ComponentNameModifier As System.String, _
   ByVal MirroredFileLocation As System.String, _
   ByVal CopyCustomProperties As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim Plane As System.Object
Dim ComponentsToInstance As System.Object
Dim ComponentsToMirror As System.Object
Dim MirroredComponentFilenames As System.Object
Dim RecreateMates As System.Boolean
Dim ComponentModifier As System.Integer
Dim ComponentNameModifier As System.String
Dim MirroredFileLocation As System.String
Dim CopyCustomProperties As System.Boolean
Dim value As System.Object

value = instance.MirrorComponents(Plane, ComponentsToInstance, ComponentsToMirror, MirroredComponentFilenames, RecreateMates, ComponentModifier, ComponentNameModifier, MirroredFileLocation, CopyCustomProperties)
```

### C#

```csharp
System.object MirrorComponents(
   System.object Plane,
   System.object ComponentsToInstance,
   System.object ComponentsToMirror,
   System.object MirroredComponentFilenames,
   System.bool RecreateMates,
   System.int ComponentModifier,
   System.string ComponentNameModifier,
   System.string MirroredFileLocation,
   System.bool CopyCustomProperties
)
```

### C++/CLI

```cpp
System.Object^ MirrorComponents(
   System.Object^ Plane,
   System.Object^ ComponentsToInstance,
   System.Object^ ComponentsToMirror,
   System.Object^ MirroredComponentFilenames,
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
- `ComponentsToInstance`: Array of instances of the component to mirror
- `ComponentsToMirror`: Array of [components](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) to mirror
- `MirroredComponentFilenames`: Array of filenames for the newly created mirrored assemblies or parts
- `RecreateMates`: True to preserve any mates between the selected components if more than one component is to be mirrored, false to not
- `ComponentModifier`: Prefix or suffix for the newly mirrored components if MirroredComponentFilenames is not specified, as defined by [swMirrorComponentNameModifier_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMirrorComponentNameModifier_e.html)
- `ComponentNameModifier`: String to add to the prefix or suffix of the name of the newly mirrored component if MirroredComponentFilenames is not specified
- `MirroredFileLocation`: Name of the folder where to store the file of the newly created mirrored components
- `CopyCustomProperties`: True to copy the custom properties from the selected components to the mirrored components, false to not

### Return Value

Array of the newly created [components](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html)

## VBA Syntax

See [AssemblyDoc::MirrorComponents](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~MirrorComponents.html).

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
