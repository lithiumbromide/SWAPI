---
title: "SchemaDescription Property (IDimXpertManager)"
project: "SOLIDWORKS API Help"
interface: "IDimXpertManager"
member: "SchemaDescription"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimXpertManager~SchemaDescription.html"
---

# SchemaDescription Property (IDimXpertManager)

Gets the description of the DimXpert schema.

## Syntax

### Visual Basic (Declaration)

```vb
Property SchemaDescription As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertManager
Dim value As System.String

instance.SchemaDescription = value

value = instance.SchemaDescription
```

### C#

```csharp
System.string SchemaDescription {get; set;}
```

### C++/CLI

```cpp
property System.String^ SchemaDescription {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

The description of the DimXpert schema

## VBA Syntax

See [DimXpertManager::SchemaDescription](ms-its:sldworksapivb6.chm::/sldworks~DimXpertManager~SchemaDescription.html).

## Remarks

This property corresponds to a Properties menu item when the right-mouse-button is clicked on a schema in the DimXpertManager tab.

## See Also

[IDimXpertManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimXpertManager.html)
[IDimXpertManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimXpertManager_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
