---
title: "Type Property (IRefPointFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRefPointFeatureData"
member: "Type"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData~Type.html"
---

# Type Property (IRefPointFeatureData)

Gets or sets the type of reference point.

## Syntax

### Visual Basic (Declaration)

```vb
Property Type As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRefPointFeatureData
Dim value As System.Integer

instance.Type = value

value = instance.Type
```

### C#

```csharp
System.int Type {get; set;}
```

### C++/CLI

```cpp
property System.int Type {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of reference point as defined by [swRefPointType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRefPointType_e.html)

## VBA Syntax

See [RefPointFeatureData::Type](ms-its:sldworksapivb6.chm::/sldworks~RefPointFeatureData~Type.html).

## Examples

See [IRefPointFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPointFeatureData.html) examples.

## Examples

[Insert Reference Points (VBA)](Insert_Reference_Points_Example_VB.htm)

## See Also

[IRefPointFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData.html)
[IRefPointFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
