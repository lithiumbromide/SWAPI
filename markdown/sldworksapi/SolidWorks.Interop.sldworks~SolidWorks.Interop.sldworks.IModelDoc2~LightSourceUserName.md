---
title: "LightSourceUserName Property (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "LightSourceUserName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~LightSourceUserName.html"
---

# LightSourceUserName Property (IModelDoc2)

Gets or sets the light source name that is displayed in the SOLIDWORKS Design user interface.

## Syntax

### Visual Basic (Declaration)

```vb
Property LightSourceUserName( _
   ByVal ID As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim ID As System.Integer
Dim value As System.String

instance.LightSourceUserName(ID) = value

value = instance.LightSourceUserName(ID)
```

### C#

```csharp
System.string LightSourceUserName(
   System.int ID
) {get; set;}
```

### C++/CLI

```cpp
property System.String^ LightSourceUserName {
   System.String^ get(System.int ID);
   void set (System.int ID, System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ID`: Light source ID

### Property Value

User name to give to the light source

## VBA Syntax

See [ModelDoc2::LightSourceUserName](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~LightSourceUserName.html).

## Examples

[Turn Lights On (VBA)](Turn_Lights_On_Example_VB.htm)

## Remarks

The light source ID ranges from 0 to n, where n = (the total number of light sources - 1). To get the total number of light sources, use [IModelDoc2::GetLightSourceCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetLightSourceCount.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::AddLightSource Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddLightSource.html)
[IModelDoc2::AddLightSourceExtProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddLightSourceExtProperty.html)
[IModelDoc2::DeleteLightSource Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeleteLightSource.html)
[IModelDoc2::GetLightSourceExtProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetLightSourceExtProperty.html)
[IModelDoc2::GetLightSourceIdFromName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetLightSourceIdFromName.html)
[IModelDoc2::GetLightSourceName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetLightSourceName.html)
[IModelDoc2::ResetLightSourceExtProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ResetLightSourceExtProperty.html)
[IModelDoc2::SetLightSourceName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetLightSourceName.html)
[IModelDoc2::SetLightSourcePropertyValuesVB Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetLightSourcePropertyValuesVB.html)
[IModelDoc2::ILightSourcePropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ILightSourcePropertyValues.html)
[IModelDoc2::LightSourcePropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~LightSourcePropertyValues.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
