---
title: "DimXpertManager Property (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "DimXpertManager"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~DimXpertManager.html"
---

# DimXpertManager Property (IConfiguration)

Gets the DimXpert schema for this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property DimXpertManager( _
   ByVal CreateSchema As System.Boolean _
) As DimXpertManager
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim CreateSchema As System.Boolean
Dim value As DimXpertManager

value = instance.DimXpertManager(CreateSchema)
```

### C#

```csharp
DimXpertManager DimXpertManager(
   System.bool CreateSchema
) {get;}
```

### C++/CLI

```cpp
property DimXpertManager^ DimXpertManager {
   DimXpertManager^ get(System.bool CreateSchema);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CreateSchema`: True to create DimXpert schema if it does not already exist; false otherwise

### Property Value

Pointer to [IDimXpertManager](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimXpertManager.html) object

## VBA Syntax

See [Configuration::DimXpertManager](ms-its:sldworksapivb6.chm::/sldworks~Configuration~DimXpertManager.html).

## Examples

[Get DimXpertManager Info (VBA)](Get_DimXpertManager_Info_Example_VB.htm)
[Get DimXpertManager Info (VB.NET)](Get_DimXpertManager_Info_Example_VBNET.htm)

## Remarks

This interface retrieves the DimXpert schema information for opened parts which can be accessed in SOLIDWORKS via either the DimXpertManager tab of the Management Panel or the DimXpert tab of the CommandManager.

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
