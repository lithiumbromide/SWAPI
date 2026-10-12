---
title: "SchemaComment Property (IDimXpertManager)"
project: "SOLIDWORKS API Help"
interface: "IDimXpertManager"
member: "SchemaComment"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimXpertManager~SchemaComment.html"
---

# SchemaComment Property (IDimXpertManager)

Gets a comment for the DimXpert schema.

## Syntax

### Visual Basic (Declaration)

```vb
Property SchemaComment As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertManager
Dim value As System.String

instance.SchemaComment = value

value = instance.SchemaComment
```

### C#

```csharp
System.string SchemaComment {get; set;}
```

### C++/CLI

```cpp
property System.String^ SchemaComment {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Comment for the DimXpert schema

## VBA Syntax

See [DimXpertManager::SchemaComment](ms-its:sldworksapivb6.chm::/sldworks~DimXpertManager~SchemaComment.html).

## Remarks

This property corresponds to a Properties menu item when the right-mouse-button is clicked on a schema in the DimXpertManager tab.

## See Also

[IDimXpertManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimXpertManager.html)
[IDimXpertManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimXpertManager_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
