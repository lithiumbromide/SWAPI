---
title: "Reference Property (IRefPlaneFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRefPlaneFeatureData"
member: "Reference"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~Reference.html"
---

# Reference Property (IRefPlaneFeatureData)

Gets or sets the reference entity for the specified reference for this reference plane feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Reference( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IRefPlaneFeatureData
Dim Index As System.Integer
Dim value As System.Object

instance.Reference(Index) = value

value = instance.Reference(Index)
```

### C#

```csharp
System.object Reference(
   System.int Index
) {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Reference {
   System.Object^ get(System.int Index);
   void set (System.int Index, System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the specified reference as defined in [swRefPlaneReferenceIndex_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRefPlaneReferenceIndex_e.html)

### Property Value

Reference entity

## VBA Syntax

See [RefPlaneFeatureData::Reference](ms-its:sldworksapivb6.chm::/sldworks~RefPlaneFeatureData~Reference.html).

## Remarks

**IMPORTANT:** Reference planes created in SOLIDWORKS 2010 or later are constraint based; reference planes created in SOLIDWORKS 2009 or earlier are not. See the **Remarks** section in the [IRefPlaneFeatureData interface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlaneFeatureData.html) topic for details about reference planes and this interface.

## See Also

[IRefPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData.html)
[IRefPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData_members.html)
[IRefPlaneFeatureData::ReversedReferenceDirection Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~ReversedReferenceDirection.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
