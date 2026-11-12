---
title: "DimXpertManager Property (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "DimXpertManager"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DimXpertManager.html"
---

# DimXpertManager Property (IModelDocExtension)

Gets the DimXpert schema for this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property DimXpertManager( _
   ByVal Configuration As System.String, _
   ByVal CreateSchema As System.Boolean _
) As DimXpertManager
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Configuration As System.String
Dim CreateSchema As System.Boolean
Dim value As DimXpertManager

value = instance.DimXpertManager(Configuration, CreateSchema)
```

### C#

```csharp
DimXpertManager DimXpertManager(
   System.string Configuration,
   System.bool CreateSchema
) {get;}
```

### C++/CLI

```cpp
property DimXpertManager^ DimXpertManager {
   DimXpertManager^ get(System.String^ Configuration, System.bool CreateSchema);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Configuration`: Name of the configuration for which to retrieve the DimXpert schema
- `CreateSchema`: True to create DimXpert schema if it does not already exist; false otherwise

### Property Value

[IDimXpertManager](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimXpertManager.html) object

## VBA Syntax

See [ModelDocExtension::DimXpertManager](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~DimXpertManager.html).

## Examples

[Get DimXpertManager Info (VBA)](Get_DimXpertManager_Info_Example_VB.htm)
[Get DimXpertManager Info (VB.NET)](Get_DimXpertManager_Info_Example_VBNET.htm)

## Remarks

This interface retrieves the DimXpert schema information for opened parts which can be accessed in SOLIDWORKS via either the DimXpertManager tab of the Management Panel or the DimXpert tab of the CommandManager.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
