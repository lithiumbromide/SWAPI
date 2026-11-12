---
title: "GetFeatures Method (IFeatureFolder)"
project: "SOLIDWORKS API Help"
interface: "IFeatureFolder"
member: "GetFeatures"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureFolder~GetFeatures.html"
---

# GetFeatures Method (IFeatureFolder)

Gets the features in this feature folder.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFeatures() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureFolder
Dim value As System.Object

value = instance.GetFeatures()
```

### C#

```csharp
System.object GetFeatures()
```

### C++/CLI

```cpp
System.Object^ GetFeatures();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) objects

## VBA Syntax

See [FeatureFolder::GetFeatures](ms-its:sldworksapivb6.chm::/sldworks~FeatureFolder~GetFeatures.html).

## Examples

[Get Contents of FeatureFolder (C#)](Get_Contents_of_FeatureFolder_Example_CSharp.htm)
[Get Contents of FeatureFolder (VB.NET)](Get_Contents_of_FeatureFolder_Example_VBNET.htm)
[Get Contents of FeatureFolder (VBA)](Get_Contents_of_FeatureFolder_Example_VB.htm)

## Remarks

Before calling this method, call [IFeatureFolder::GetFeatureCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureFolder~GetFeatureCount.html) to get the size of the array returned by this method.

## See Also

[IFeatureFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureFolder.html)
[IFeatureFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureFolder_members.html)
[IFeatureFolder::IGetFeatures Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureFolder~IGetFeatures.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
