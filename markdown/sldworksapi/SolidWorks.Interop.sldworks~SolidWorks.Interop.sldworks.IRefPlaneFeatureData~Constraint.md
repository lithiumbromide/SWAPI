---
title: "Constraint Property (IRefPlaneFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRefPlaneFeatureData"
member: "Constraint"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~Constraint.html"
---

# Constraint Property (IRefPlaneFeatureData)

Gets or sets the constraint for the specified [reference](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlaneFeatureData~Reference.html) for this reference plane feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Constraint( _
   ByVal Index As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRefPlaneFeatureData
Dim Index As System.Integer
Dim value As System.Integer

instance.Constraint(Index) = value

value = instance.Constraint(Index)
```

### C#

```csharp
System.int Constraint(
   System.int Index
) {get; set;}
```

### C++/CLI

```cpp
property System.int Constraint {
   System.int get(System.int Index);
   void set (System.int Index, System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the specified [reference](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlaneFeatureData~Reference.html) as defined in [swRefPlaneReferenceIndex_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRefPlaneReferenceIndex_e.html)

### Property Value

Constraint as defined in [swRefPlaneReferenceConstraints_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRefPlaneReferenceConstraints_e.html)

## VBA Syntax

See [RefPlaneFeatureData::Constraint](ms-its:sldworksapivb6.chm::/sldworks~RefPlaneFeatureData~Constraint.html).

## Remarks

**IMPORTANT:** Reference planes created in SOLIDWORKS 2010 or later are constraint based; reference planes created in SOLIDWORKS 2009 or earlier are not. See the **Remarks** section in the [IRefPlaneFeatureData interface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlaneFeatureData.html) topic for details about reference planes and this interface.

## See Also

[IRefPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData.html)
[IRefPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData_members.html)
[IRefPlaneFeatureData::Reference Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~Reference.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
