---
title: "LeaderBendLength Property (IPMIDatumFeature)"
project: "SOLIDWORKS API Help"
interface: "IPMIDatumFeature"
member: "LeaderBendLength"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumFeature~LeaderBendLength.html"
---

# LeaderBendLength Property (IPMIDatumFeature)

Gets the length of the unbent portion of the leader to this PMI datum.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property LeaderBendLength As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIDatumFeature
Dim value As System.Double

instance.LeaderBendLength = value

value = instance.LeaderBendLength
```

### C#

```csharp
System.double LeaderBendLength {get; set;}
```

### C++/CLI

```cpp
property System.double LeaderBendLength {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Length of the unbent portion of the PMI datum leader

## VBA Syntax

See [PMIDatumFeature::LeaderBendLength](ms-its:sldworksapivb6.chm::/sldworks~PMIDatumFeature~LeaderBendLength.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## See Also

[IPMIDatumFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumFeature.html)
[IPMIDatumFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumFeature_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
