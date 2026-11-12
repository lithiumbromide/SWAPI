---
title: "GetLightSourceExtProperty Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetLightSourceExtProperty"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetLightSourceExtProperty.html"
---

# GetLightSourceExtProperty Method (IModelDoc2)

Gets a float, string, or integer value stored for the light source.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLightSourceExtProperty( _
   ByVal ID As System.Integer, _
   ByVal PropertyId As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim ID As System.Integer
Dim PropertyId As System.Integer
Dim value As System.Object

value = instance.GetLightSourceExtProperty(ID, PropertyId)
```

### C#

```csharp
System.object GetLightSourceExtProperty(
   System.int ID,
   System.int PropertyId
)
```

### C++/CLI

```cpp
System.Object^ GetLightSourceExtProperty(
   System.int ID,
   System.int PropertyId
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ID`: ID of the light source
- `PropertyId`: ID of the property extension (see **Remarks**)

### Return Value

Value stored for the light source

## VBA Syntax

See [ModelDoc2::GetLightSourceExtProperty](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetLightSourceExtProperty.html).

## Remarks

The type returned is based on the how the data was placed. See [IModelDoc2::AddLightSourceExtProperty](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~AddLightSourceExtProperty.html) for details.

Values for Id can range from 0 to n, where n = (the total number of light sources - 1). To get the total number of light sources, use [IModelDoc2::GetLightSourceCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetLightSourceCount.html).

The PropertyId parameter takes a 0-based index of the property. Values returned from IModelDoc2::AddLightSourceExtProperty must be decremented by 1 when used as input to IModelDoc2::GetLightSourceExtProperty. However, do not decrement the error value of -1.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::AddLightSource Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddLightSource.html)
[IModelDoc2::AddLightSourceExtProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddLightSourceExtProperty.html)
[IModelDoc2::DeleteLightSource Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeleteLightSource.html)
[IModelDoc2::GetLightSourceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetLightSourceCount.html)
[IModelDoc2::GetLightSourceIdFromName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetLightSourceIdFromName.html)
[IModelDoc2::GetLightSourceName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetLightSourceName.html)
[IModelDoc2::SetLightSourceName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetLightSourceName.html)
[IModelDoc2::SetLightSourcePropertyValuesVB Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetLightSourcePropertyValuesVB.html)
[IModelDoc2::ILightSourcePropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ILightSourcePropertyValues.html)
[IModelDoc2::LightSourcePropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~LightSourcePropertyValues.html)
[IModelDoc2::LightSourceUserName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~LightSourceUserName.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
