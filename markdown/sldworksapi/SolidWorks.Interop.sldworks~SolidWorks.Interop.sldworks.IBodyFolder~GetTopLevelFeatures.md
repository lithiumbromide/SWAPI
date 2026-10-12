---
title: "GetTopLevelFeatures Method (IBodyFolder)"
project: "SOLIDWORKS API Help"
interface: "IBodyFolder"
member: "GetTopLevelFeatures"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~GetTopLevelFeatures.html"
---

# GetTopLevelFeatures Method (IBodyFolder)

Gets the top-level features in this body folder.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTopLevelFeatures() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBodyFolder
Dim value As System.Object

value = instance.GetTopLevelFeatures()
```

### C#

```csharp
System.object GetTopLevelFeatures()
```

### C++/CLI

```cpp
System.Object^ GetTopLevelFeatures();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of top-level [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)s

## VBA Syntax

See [BodyFolder::GetTopLevelFeatures](ms-its:sldworksapivb6.chm::/sldworks~BodyFolder~GetTopLevelFeatures.html).

## Remarks

Use [IBodyFolder::GetTopLevelFeatureCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~GetTopLevelFeatureCount.html) to determine the size of this method's returned array.

## See Also

[IBodyFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder.html)
[IBodyFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
