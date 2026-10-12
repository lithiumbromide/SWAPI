---
title: "Offset Property (ISMNormalCutFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISMNormalCutFeatureData"
member: "Offset"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData~Offset.html"
---

# Offset Property (ISMNormalCutFeatureData)

Obsolete. See [ISMNormalCutFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property Offset As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISMNormalCutFeatureData
Dim value As System.Double

instance.Offset = value

value = instance.Offset
```

### C#

```csharp
System.double Offset {get; set;}
```

### C++/CLI

```cpp
property System.double Offset {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0.0 <= offset <= 1.0

## VBA Syntax

See [SMNormalCutFeatureData::Offset](ms-its:sldworksapivb6.chm::/sldworks~SMNormalCutFeatureData~Offset.html).

## Examples

See the [IFeatureManager::AddSMNormalCutType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~AddSMNormalCutType.html) example.

## Remarks

This property allows you to adjust the profile of the Normal Cut. Setting this property to 0.0 sets the profile to the circular edge on one side of the body. Setting it to 1.0 sets the profile to the circular edge on the opposite side of the body. A value in between 0.0 and 1.0 sets the profile to a circular edge somewhere in the middle of the body.

## See Also

[ISMNormalCutFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData.html)
[ISMNormalCutFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
