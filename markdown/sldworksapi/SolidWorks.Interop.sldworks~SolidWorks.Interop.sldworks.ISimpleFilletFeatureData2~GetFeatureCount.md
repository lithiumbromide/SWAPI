---
title: "GetFeatureCount Method (ISimpleFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: "GetFeatureCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetFeatureCount.html"
---

# GetFeatureCount Method (ISimpleFilletFeatureData2)

Gets the number of features on which to create a simple radius fillet.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFeatureCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData2
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

Number of features

## VBA Syntax

See [SimpleFilletFeatureData2::GetFeatureCount](ms-its:sldworksapivb6.chm::/sldworks~SimpleFilletFeatureData2~GetFeatureCount.html).

## Remarks

Call this method before calling [ISimpleFilletFeatureData2::IGetFeatures](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleFilletFeatureData2~IGetFeatures.html) to get the size of the array for that method.

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)
[ISimpleFilletFeatureData2::ISetFeatures Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetFeatures.html)
[ISimpleFilletFeatureData2::Features Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~Features.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
