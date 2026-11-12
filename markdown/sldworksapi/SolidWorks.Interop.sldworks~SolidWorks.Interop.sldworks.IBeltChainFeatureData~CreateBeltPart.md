---
title: "CreateBeltPart Property (IBeltChainFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBeltChainFeatureData"
member: "CreateBeltPart"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData~CreateBeltPart.html"
---

# CreateBeltPart Property (IBeltChainFeatureData)

Gets and sets whether to create a new part that contains the belt sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Property CreateBeltPart As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBeltChainFeatureData
Dim value As System.Boolean

instance.CreateBeltPart = value

value = instance.CreateBeltPart
```

### C#

```csharp
System.bool CreateBeltPart {get; set;}
```

### C++/CLI

```cpp
property System.bool CreateBeltPart {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to create a belt part, false to not

## VBA Syntax

See [BeltChainFeatureData::CreateBeltPart](ms-its:sldworksapivb6.chm::/sldworks~BeltChainFeatureData~CreateBeltPart.html).

## Examples

See the [IBeltChainFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData.html) examples.

## Remarks

If this property is set to true, use [IBeltChainFeatureData::AccessBeltPart](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData~AccessBeltPart.html) to get the belt part.

## See Also

[IBeltChainFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData.html)
[IBeltChainFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
