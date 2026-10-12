---
title: "EditRebuild3 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "EditRebuild3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.html"
---

# EditRebuild3 Method (IModelDoc2)

Rebuilds only those features that need to be rebuilt in the active configuration in the model.

## Syntax

### Visual Basic (Declaration)

```vb
Function EditRebuild3() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Boolean

value = instance.EditRebuild3()
```

### C#

```csharp
System.bool EditRebuild3()
```

### C++/CLI

```cpp
System.bool EditRebuild3();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if only those features that need to be rebuilt are rebuilt in the active configuration in the model, false if not

## VBA Syntax

See [ModelDoc2::EditRebuild3](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~EditRebuild3.html).

## Examples

[Calculate Closest Distance Between Faces (VBA)](Calculate_Closest_Distance_Between_Faces_Example_VB.htm)
[Change Dimensions of Gear Mate (VBA)](Change_Dimensions_of_Gear_Mate_Example_VB.htm)
[Find Outside Edges of Face (VBA)](Find_Outside_Edges_of_Face_Example_VB.htm)
[Get Intersecting Face and Edge (VBA)](Get_Intersecting_Face_and_Edge_Example_VB.htm)
[Get Intersecting Faces (VBA)](Get_Intersecting_Faces_Example_VB.htm)
[Insert DXF File and Add Dimension (VBA)](Insert_DXF_File_and_Add_Dimension_Example_VB.htm)
[Rebuild Model (VBA)](Rebuild_Example_VB.htm)
[Traverse Bodies (C++)](Traverse_Bodies_Example_CPlusPlusCLI.htm)
[Modify Surface-cut Feature (C#)](Modify_Surface_Cut_Feature_Example_CSharp.htm)
[Modify Surface-cut Feature (VB.NET)](Modify_Surface_Cut_Feature_Example_VBNET.htm)
[Modify Surface-cut Feature (VBA)](Modify_Surface_Cut_Feature_Example_VB.htm)

## Remarks

This method only works in-context of the active document.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::ForceRebuild3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ForceRebuild3.html)
[IModelDoc2::Rebuild Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Rebuild.html)
[IModelDocExtension::NeedsRebuild2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~NeedsRebuild2.html)
[IModelDocExtension::EditRebuildAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~EditRebuildAll.html)
[IModelDocExtension::ForceRebuildAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ForceRebuildAll.html)
[IConfiguration::AddRebuildSaveMark Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddRebuildSaveMark.html)
[IConfiguration::NeedsRebuild Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~NeedsRebuild.html)
[IConfigurationManager::AddRebuildSaveMark Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~AddRebuildSaveMark.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
