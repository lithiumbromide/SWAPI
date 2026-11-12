---
title: "ReversedReferenceDirection Property (IRefPlaneFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRefPlaneFeatureData"
member: "ReversedReferenceDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~ReversedReferenceDirection.html"
---

# ReversedReferenceDirection Property (IRefPlaneFeatureData)

Gets or sets whether to reverse the direction of the specified reference for this reference plane feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReversedReferenceDirection( _
   ByVal ReferenceIndex As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRefPlaneFeatureData
Dim ReferenceIndex As System.Integer
Dim value As System.Boolean

instance.ReversedReferenceDirection(ReferenceIndex) = value

value = instance.ReversedReferenceDirection(ReferenceIndex)
```

### C#

```csharp
System.bool ReversedReferenceDirection(
   System.int ReferenceIndex
) {get; set;}
```

### C++/CLI

```cpp
property System.bool ReversedReferenceDirection {
   System.bool get(System.int ReferenceIndex);
   void set (System.int ReferenceIndex, System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ReferenceIndex`: Index of the reference whose direction to set as defined in [swRefPlaneReferenceIndex_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRefPlaneReferenceIndex_e.html)

### Property Value

True to reverse the direction of the specified reference, false to not

## VBA Syntax

See [RefPlaneFeatureData::ReversedReferenceDirection](ms-its:sldworksapivb6.chm::/sldworks~RefPlaneFeatureData~ReversedReferenceDirection.html).

## Remarks

**IMPORTANT:** Reference planes created in SOLIDWORKS 2010 or later are constraint based; reference planes created in SOLIDWORKS 2009 or earlier are not. See the **Remarks** section in the [IRefPlaneFeatureData interface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlaneFeatureData.html) topic for details about reference planes and this interface.

## See Also

[IRefPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData.html)
[IRefPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData_members.html)
[IRefPlaneFeatureData::Reference Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~Reference.html)

## Availability

SOLIDWORKS 2018 SP04, Revision Number 26.4
