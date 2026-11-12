---
title: "GetJoinedPartsCount Method (IJoinFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IJoinFeatureData"
member: "GetJoinedPartsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData~GetJoinedPartsCount.html"
---

# GetJoinedPartsCount Method (IJoinFeatureData)

Gets the number of joined parts.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetJoinedPartsCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IJoinFeatureData
Dim value As System.Integer

value = instance.GetJoinedPartsCount()
```

### C#

```csharp
System.int GetJoinedPartsCount()
```

### C++/CLI

```cpp
System.int GetJoinedPartsCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of joined parts

## VBA Syntax

See [JoinFeatureData::GetJoinedPartsCount](ms-its:sldworksapivb6.chm::/sldworks~JoinFeatureData~GetJoinedPartsCount.html).

## Examples

[Insert Join Feature (C#)](Insert_Join_Feature_Example_CSharp.htm)
[Insert Join Feature (VB.NET)](Insert_Join_Feature_Example_VBNET.htm)
[Insert Join Feature (VBA)](Insert_Join_Feature_Example_VB.htm)

## Remarks

Call this method before calling [IJoinFeatureData::IGetJoinedParts](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IJoinFeatureData~IGetJoinedParts.html) to determine the size of the array.

## See Also

[IJoinFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData.html)
[IJoinFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData_members.html)
[IJoinFeatureData::ISetJoinedParts Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData~ISetJoinedParts.html)
[IJoinFeatureData::JoinedParts Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData~JoinedParts.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
