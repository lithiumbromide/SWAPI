---
title: "InstanceCount Property (IPMIGtolData)"
project: "SOLIDWORKS API Help"
interface: "IPMIGtolData"
member: "InstanceCount"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolData~InstanceCount.html"
---

# InstanceCount Property (IPMIGtolData)

Gets the number of times this PMI Gtol is repeated.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property InstanceCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIGtolData
Dim value As System.Integer

instance.InstanceCount = value

value = instance.InstanceCount
```

### C#

```csharp
System.int InstanceCount {get; set;}
```

### C++/CLI

```cpp
property System.int InstanceCount {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of repeated instances of this Gtol

## VBA Syntax

See [PMIGtolData::InstanceCount](ms-its:sldworksapivb6.chm::/sldworks~PMIGtolData~InstanceCount.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## See Also

[IPMIGtolData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolData.html)
[IPMIGtolData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
