---
title: "GetBodyCount Method (IBodyFolder)"
project: "SOLIDWORKS API Help"
interface: "IBodyFolder"
member: "GetBodyCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~GetBodyCount.html"
---

# GetBodyCount Method (IBodyFolder)

Gets the number of bodies in the folder.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBodyCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBodyFolder
Dim value As System.Integer

value = instance.GetBodyCount()
```

### C#

```csharp
System.int GetBodyCount()
```

### C++/CLI

```cpp
System.int GetBodyCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of bodies in the folder

## VBA Syntax

See [BodyFolder::GetBodyCount](ms-its:sldworksapivb6.chm::/sldworks~BodyFolder~GetBodyCount.html).

## Examples

[Get Bodies in Body Folders (VBA)](Get_Bodies_in_Body_Folders_Example_VB.htm)
[Get Custom Properties for Configuration (VBA)](Get_Custom_Properties_for_Configuration_Example_VB.htm)
[Get Features of Multibody Sheet Metal Part (C#)](Get_Features_of_Multibody_Sheet_Metal_Part_Example_CSharp.htm)
[Get Features of Multibody Sheet Metal Part (VB.NET)](Get_Features_of_Multibody_Sheet_Metal_Part_Example_VBNET.htm)
[Get Features of Multibody Sheet Metal Part (VBA)](Get_Features_of_Multibody_Sheet_Metal_Part_Example_VB.htm)
[Get Solid Bodies from Cut-list Folders and Get Custom Properties (C#)](Get_Solid_Bodies_from_Cut-list_Folders_and_Get_Custom_Properties_Example_CSharp.htm)
[Get Solid Bodies from Cut-list Folders and Get Custom Properties (VB.NET)](Get_Solid_Bodies_from_Cut-list_Folders_and_Get_Custom_Properties_Example_VBNET.htm)
[Get Solid Bodies from Cut-list Folders and Get Custom Properties (VBA)](Get_Solid_Bodies_from_Cut-list_Folders_and_Get_Custom_Properties_Example_VB.htm)

## Remarks

Use this method before using [IBodyFolder::IGetBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBodyFolder~IGetBodies.html).

See [Accessing Bodies in Body Folders](sldworksAPIProgGuide.chm::/OVERVIEW/Accessing_Bodies_in_Body_Folders.htm) for details about the BodyFolder interface.

## See Also

[IBodyFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder.html)
[IBodyFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder_members.html)
[IBodyFolder::GetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~GetBodies.html)

## Availability

SOLIDWORKS 2005 SP2, Revision Number 13
