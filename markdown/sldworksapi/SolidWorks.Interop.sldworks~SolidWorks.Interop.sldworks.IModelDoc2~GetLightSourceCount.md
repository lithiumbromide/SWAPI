---
title: "GetLightSourceCount Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetLightSourceCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetLightSourceCount.html"
---

# GetLightSourceCount Method (IModelDoc2)

Gets the number of light sources.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLightSourceCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Integer

value = instance.GetLightSourceCount()
```

### C#

```csharp
System.int GetLightSourceCount()
```

### C++/CLI

```cpp
System.int GetLightSourceCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of light sources

## VBA Syntax

See [ModelDoc2::GetLightSourceCount](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetLightSourceCount.html).

## Examples

[Turn Lights On (VBA)](Turn_Lights_On_Example_VB.htm)

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::GetLightSourceExtProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetLightSourceExtProperty.html)
[IModelDoc2::GetLightSourceIdFromName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetLightSourceIdFromName.html)
[IModelDoc2::GetLightSourceName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetLightSourceName.html)
[IModelDoc2::SetLightSourceName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetLightSourceName.html)
[IModelDoc2::SetLightSourcePropertyValuesVB Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetLightSourcePropertyValuesVB.html)
[IModelDoc2::ILightSourcePropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ILightSourcePropertyValues.html)
[IModelDoc2::LightSourcePropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~LightSourcePropertyValues.html)
[IModelDoc2::LightSourceUserName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~LightSourceUserName.html)
[IModelDoc2::AddLightSource Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddLightSource.html)
[IModelDoc2::AddLightSourceExtProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddLightSourceExtProperty.html)
[IModelDoc2::DeleteLightSource Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeleteLightSource.html)
[IModelDoc2::ResetLightSourceExtProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ResetLightSourceExtProperty.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
