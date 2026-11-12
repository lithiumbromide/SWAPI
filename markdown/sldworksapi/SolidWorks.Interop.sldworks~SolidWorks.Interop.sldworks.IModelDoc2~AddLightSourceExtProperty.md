---
title: "AddLightSourceExtProperty Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "AddLightSourceExtProperty"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddLightSourceExtProperty.html"
---

# AddLightSourceExtProperty Method (IModelDoc2)

Stores a float, string, or integer value for the light source.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddLightSourceExtProperty( _
   ByVal ID As System.Integer, _
   ByVal PropertyExtension As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim ID As System.Integer
Dim PropertyExtension As System.Object
Dim value As System.Integer

value = instance.AddLightSourceExtProperty(ID, PropertyExtension)
```

### C#

```csharp
System.int AddLightSourceExtProperty(
   System.int ID,
   System.object PropertyExtension
)
```

### C++/CLI

```cpp
System.int AddLightSourceExtProperty(
   System.int ID,
   System.Object^ PropertyExtension
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ID`: ID of the light source
- `PropertyExtension`: Value you want to store for the light source

### Return Value

ID of the extension property (see **Remarks**)

## VBA Syntax

See [ModelDoc2::AddLightSourceExtProperty](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~AddLightSourceExtProperty.html).

## Remarks

This property extension is stored on the model document and is unique to the specified light source.

To add the property extension, you must first define the VARIANT type (float, string, or integer), give your variable a value, and then call this method to place the value on the light source for future reference.

This method returns a 1-based index of the added property. Values returned from IModelDoc2::AddLightSourceExtProperty must be decremented by 1 when used as input to [IModelDoc2::GetLightSourceExtProperty](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetLightSourceName.html). However, the error value of -1 should not be decremented.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::AddLightSource Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddLightSource.html)
[IModelDoc2::DeleteLightSource Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeleteLightSource.html)
[IModelDoc2::GetLightSourceExtProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetLightSourceExtProperty.html)
[IModelDoc2::GetLightSourceIdFromName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetLightSourceIdFromName.html)
[IModelDoc2::GetLightSourceName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetLightSourceName.html)
[IModelDoc2::ResetLightSourceExtProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ResetLightSourceExtProperty.html)
[IModelDoc2::SetLightSourceName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetLightSourceName.html)
[IModelDoc2::SetLightSourcePropertyValuesVB Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetLightSourcePropertyValuesVB.html)
[IModelDoc2::ILightSourcePropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ILightSourcePropertyValues.html)
[IModelDoc2::LightSourcePropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~LightSourcePropertyValues.html)
[IModelDoc2::LightSourceUserName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~LightSourceUserName.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
