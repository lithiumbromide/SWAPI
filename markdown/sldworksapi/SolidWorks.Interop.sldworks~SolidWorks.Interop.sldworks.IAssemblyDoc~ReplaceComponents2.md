---
title: "ReplaceComponents2 Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "ReplaceComponents2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ReplaceComponents2.html"
---

# ReplaceComponents2 Method (IAssemblyDoc)

Replaces one or more selected components with another model.

## Syntax

### Visual Basic (Declaration)

```vb
Function ReplaceComponents2( _
   ByVal FileName As System.String, _
   ByVal ConfigName As System.String, _
   ByVal ReplaceAllInstance As System.Boolean, _
   ByVal UseConfigChoice As System.Integer, _
   ByVal ReAttachMates As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim FileName As System.String
Dim ConfigName As System.String
Dim ReplaceAllInstance As System.Boolean
Dim UseConfigChoice As System.Integer
Dim ReAttachMates As System.Boolean
Dim value As System.Boolean

value = instance.ReplaceComponents2(FileName, ConfigName, ReplaceAllInstance, UseConfigChoice, ReAttachMates)
```

### C#

```csharp
System.bool ReplaceComponents2(
   System.string FileName,
   System.string ConfigName,
   System.bool ReplaceAllInstance,
   System.int UseConfigChoice,
   System.bool ReAttachMates
)
```

### C++/CLI

```cpp
System.bool ReplaceComponents2(
   System.String^ FileName,
   System.String^ ConfigName,
   System.bool ReplaceAllInstance,
   System.int UseConfigChoice,
   System.bool ReAttachMates
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Path and file name of the replacement component
- `ConfigName`: Name of a configuration in the replacement component; an empty string indicates the default configuration of the replacement component
- `ReplaceAllInstance`: True to replace all instances of the selected components with the replacement component, false to not
- `UseConfigChoice`: Configuration to use as defined in [swReplaceComponentsConfiguration_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swReplaceComponentsConfiguration_e.html)
- `ReAttachMates`: True to reattach existing mates to the replacement component, false to not

### Return Value

True if the selected components are replaced, false if not

## VBA Syntax

See [AssemblyDoc::ReplaceComponents2](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~ReplaceComponents2.html).

## Examples

[Replace Component (C#)](Replace_Component_Example_CSharp.htm)
[Replace Component (VB.NET)](Replace_Component_Example_VBNET.htm)
[Replace Component (VBA)](Replace_Component_Example_VB.htm)

## Remarks

You cannot replace a selected component with a component of the same name even if the components reside in different folders.

The component must be a top-level component. It cannot be a component of a sub-assembly. If your application needs to replace a component of a sub-assembly, then your application must open the sub-assembly and get the component from that assembly.

This method closes any component files when called in an assembly. If components were modified, then those modifications are not automatically saved. You must save any modifications before closing the files.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IModelDoc2::ReloadOrReplace Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ReloadOrReplace.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
