---
title: "Clearance Property (IIndentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IIndentFeatureData"
member: "Clearance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~Clearance.html"
---

# Clearance Property (IIndentFeatureData)

Gets or sets the clearance between the target and tool bodies in this indent feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Clearance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IIndentFeatureData
Dim value As System.Double

instance.Clearance = value

value = instance.Clearance
```

### C#

```csharp
System.double Clearance {get; set;}
```

### C++/CLI

```cpp
property System.double Clearance {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Clearance between the target and tool bodies

## VBA Syntax

See [IndentFeatureData::Clearance](ms-its:sldworksapivb6.chm::/sldworks~IndentFeatureData~Clearance.html).

## See Also

[IIndentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData.html)
[IIndentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData_members.html)
[IIndentFeatureData::ClearanceDirection Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~ClearanceDirection.html)
[IIndentFeatureData::TargetBody Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~TargetBody.html)
[IIndentFeatureData::ToolBodyRegion Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~ToolBodyRegion.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
