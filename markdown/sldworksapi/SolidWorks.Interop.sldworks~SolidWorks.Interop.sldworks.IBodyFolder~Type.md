---
title: "Type Property (IBodyFolder)"
project: "SOLIDWORKS API Help"
interface: "IBodyFolder"
member: "Type"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~Type.html"
---

# Type Property (IBodyFolder)

Gets the type of body folder.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Type As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBodyFolder
Dim value As System.Integer

value = instance.Type
```

### C#

```csharp
System.int Type {get;}
```

### C++/CLI

```cpp
property System.int Type {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of body folder as defined in [swBodyFolderFeatureType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBodyFolderFeatureType_e.html)

## VBA Syntax

See [BodyFolder::Type](ms-its:sldworksapivb6.chm::/sldworks~BodyFolder~Type.html).

## Examples

[Get Bodies in Body Folders (VBA)](Get_Bodies_in_Body_Folders_Example_VB.htm)
[Get SolidBodies from Cut-list Folders and Get Custom Properties (VBA)](Get_Solid_Bodies_from_Cut-list_Folders_and_Get_Custom_Properties_Example_VB.htm)
[Get Bodies in Body Folders (VB.NET)](Get_Bodies_in_Body_Folders_Example_VBNET.htm)
[Get Bodies in Body Folders (C#)](Get_Bodies_in_Body_Folders_Example_CSharp.htm)

## Remarks

See [Accessing Bodies in Body Folders](sldworksAPIProgGuide.chm::/OVERVIEW/Accessing_Bodies_in_Body_Folders.htm) for details about the BodyFolder interface.

## See Also

[IBodyFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder.html)
[IBodyFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder_members.html)

## Availability

SOLIDWORKS 2005 SP2, Revision Number 13
