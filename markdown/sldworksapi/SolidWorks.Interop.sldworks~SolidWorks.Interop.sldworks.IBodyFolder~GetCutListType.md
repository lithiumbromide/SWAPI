---
title: "GetCutListType Method (IBodyFolder)"
project: "SOLIDWORKS API Help"
interface: "IBodyFolder"
member: "GetCutListType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~GetCutListType.html"
---

# GetCutListType Method (IBodyFolder)

Gets the type of cut list.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCutListType() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBodyFolder
Dim value As System.Integer

value = instance.GetCutListType()
```

### C#

```csharp
System.int GetCutListType()
```

### C++/CLI

```cpp
System.int GetCutListType();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Type of cut list as defined in [swCutListType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCutListType_e.html)

## VBA Syntax

See ms-its:sldworksapivb6.chm::/sldworks~BodyFolder~GetBodyCount.html[BodyFolder::GetCutListType](ms-its:sldworksapivb6.chm::/sldworks~BodyFolder~GetCutListType.html).

## Examples

[Get Features of Multibody Sheet Metal Part (VBA)](Get_Features_of_Multibody_Sheet_Metal_Part_Example_VB.htm)
[Get Features of Multibody Sheet Metal Part (VB.NET)](Get_Features_of_Multibody_Sheet_Metal_Part_Example_VBNET.htm)
[Get Features of Multibody Sheet Metal Part (C#)](Get_Features_of_Multibody_Sheet_Metal_Part_Example_CSharp.htm)

## See Also

[IBodyFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder.html)
[IBodyFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder_members.html)
[IBodyFolder::GetAutomaticCutList Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~GetAutomaticCutList.html)
[IBodyFolder::SetAutomaticCutList Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~SetAutomaticCutList.html)
[IBodyFolder::UpdateCutList Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~UpdateCutList.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
