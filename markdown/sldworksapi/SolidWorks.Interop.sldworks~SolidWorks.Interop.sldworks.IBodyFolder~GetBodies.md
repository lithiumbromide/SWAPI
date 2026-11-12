---
title: "GetBodies Method (IBodyFolder)"
project: "SOLIDWORKS API Help"
interface: "IBodyFolder"
member: "GetBodies"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~GetBodies.html"
---

# GetBodies Method (IBodyFolder)

Gets the bodies in the folder.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBodies() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBodyFolder
Dim value As System.Object

value = instance.GetBodies()
```

### C#

```csharp
System.object GetBodies()
```

### C++/CLI

```cpp
System.Object^ GetBodies();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [IBody2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) objects

## VBA Syntax

See [BodyFolder::GetBodies](ms-its:sldworksapivb6.chm::/sldworks~BodyFolder~GetBodies.html).

## Examples

## Examples

[Get Bodies in Body Folders (VBA)](Get_Bodies_in_Body_Folders_Example_VB.htm)
[Get Features of Multibody Sheet Metal Part (C#)](Get_Features_of_Multibody_Sheet_Metal_Part_Example_CSharp.htm)
[Get Features of Multibody Sheet Metal Part (VB.NET)](Get_Features_of_Multibody_Sheet_Metal_Part_Example_VBNET.htm)
[Get Features of Multibody Sheet Metal Part (VBA)](Get_Features_of_Multibody_Sheet_Metal_Part_Example_VB.htm)
[Get Solid Bodies from Cut-list Folders and Get Custom Properties (C#)](Get_Solid_Bodies_from_Cut-list_Folders_and_Get_Custom_Properties_Example_CSharp.htm)
[Get Solid Bodies from Cut-list Folders and Get Custom Properties (VB.NET)](Get_Solid_Bodies_from_Cut-list_Folders_and_Get_Custom_Properties_Example_VBNET.htm)
[Get Solid Bodies from Cut-list Folders and Get Custom Properties (VBA)](Get_Solid_Bodies_from_Cut-list_Folders_and_Get_Custom_Properties_Example_VB.htm)

## Remarks

This method gets the bodies in the folder in the order in which they appear in the FeatureManager design tree; it does not get the bodies in any subfolders. See [Accessing Bodies in Body Folders](sldworksAPIProgGuide.chm::/OVERVIEW/Accessing_Bodies_in_Body_Folders.htm) for details about the IBodyFolder interface.

## See Also

[IBodyFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder.html)
[IBodyFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder_members.html)
[IBodyFolder::IGetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~IGetBodies.html)
[IBodyFolder::GetBodyCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~GetBodyCount.html)

## Availability

SOLIDWORKS 2005 SP2, Revision Number 13
