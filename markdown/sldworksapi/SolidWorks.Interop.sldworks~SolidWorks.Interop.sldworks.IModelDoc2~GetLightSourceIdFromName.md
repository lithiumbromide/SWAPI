---
title: "GetLightSourceIdFromName Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetLightSourceIdFromName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetLightSourceIdFromName.html"
---

# GetLightSourceIdFromName Method (IModelDoc2)

Gets the ID of the specified light source.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLightSourceIdFromName( _
   ByVal LightName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim LightName As System.String
Dim value As System.Integer

value = instance.GetLightSourceIdFromName(LightName)
```

### C#

```csharp
System.int GetLightSourceIdFromName(
   System.string LightName
)
```

### C++/CLI

```cpp
System.int GetLightSourceIdFromName(
   System.String^ LightName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `LightName`: Internal name of the light source

### Return Value

ID for the light source

## VBA Syntax

See [ModelDoc2::GetLightSourceIdFromName](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetLightSourceIdFromName.html).

## Remarks

The ID for the light source can range from 0 to n, where n = (the total number of light sources - 1). To get the total number of light sources, use [IModelDoc2::GetLightSourceCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetLightSourceCount.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::AddLightSource Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddLightSource.html)
[IModelDoc2::AddLightSourceExtProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddLightSourceExtProperty.html)
[IModelDoc2::DeleteLightSource Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeleteLightSource.html)
[IModelDoc2::GetLightSourceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetLightSourceCount.html)
[IModelDoc2::GetLightSourceExtProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetLightSourceExtProperty.html)
[IModelDoc2::GetLightSourceName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetLightSourceName.html)
[IModelDoc2::ResetLightSourceExtProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ResetLightSourceExtProperty.html)
[IModelDoc2::SetLightSourceName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetLightSourceName.html)
[IModelDoc2::SetLightSourcePropertyValuesVB Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetLightSourcePropertyValuesVB.html)
[IModelDoc2::ILightSourcePropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ILightSourcePropertyValues.html)
[IModelDoc2::LightSourcePropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~LightSourcePropertyValues.html)
[IModelDoc2::LightSourceUserName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~LightSourceUserName.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
