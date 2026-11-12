---
title: "GetFeatureCount Method (IFeatureFolder)"
project: "SOLIDWORKS API Help"
interface: "IFeatureFolder"
member: "GetFeatureCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureFolder~GetFeatureCount.html"
---

# GetFeatureCount Method (IFeatureFolder)

Gets the number of features in this feature folder.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFeatureCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureFolder
Dim value As System.Integer

value = instance.GetFeatureCount()
```

### C#

```csharp
System.int GetFeatureCount()
```

### C++/CLI

```cpp
System.int GetFeatureCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of features in the folder

## VBA Syntax

See [FeatureFolder::GetFeatureCount](ms-its:sldworksapivb6.chm::/sldworks~FeatureFolder~GetFeatureCount.html).

## Examples

[Get Contents of FeatureFolder (C#)](Get_Contents_of_FeatureFolder_Example_CSharp.htm)
[Get Contents of FeatureFolder (VB.NET)](Get_Contents_of_FeatureFolder_Example_VBNET.htm)
[Get Contents of FeatureFolder (VBA)](Get_Contents_of_FeatureFolder_Example_VB.htm)

## See Also

[IFeatureFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureFolder.html)
[IFeatureFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureFolder_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
