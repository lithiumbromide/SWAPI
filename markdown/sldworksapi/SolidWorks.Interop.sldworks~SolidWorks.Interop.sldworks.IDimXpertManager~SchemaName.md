---
title: "SchemaName Property (IDimXpertManager)"
project: "SOLIDWORKS API Help"
interface: "IDimXpertManager"
member: "SchemaName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimXpertManager~SchemaName.html"
---

# SchemaName Property (IDimXpertManager)

Gets the name of the DimXpertSchema.

## Syntax

### Visual Basic (Declaration)

```vb
Property SchemaName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertManager
Dim value As System.String

instance.SchemaName = value

value = instance.SchemaName
```

### C#

```csharp
System.string SchemaName {get; set;}
```

### C++/CLI

```cpp
property System.String^ SchemaName {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

The name of the DimXpert schema

## VBA Syntax

See [DimXpertManager::SchemaName](ms-its:sldworksapivb6.chm::/sldworks~DimXpertManager~SchemaName.html).

## Remarks

This property corresponds to a Properties menu item when the right-mouse-button is clicked on a schema in the DimXpertManager tab.

## See Also

[IDimXpertManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimXpertManager.html)
[IDimXpertManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimXpertManager_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
