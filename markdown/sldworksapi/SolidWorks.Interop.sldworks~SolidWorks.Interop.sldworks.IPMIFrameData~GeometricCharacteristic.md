---
title: "GeometricCharacteristic Property (IPMIFrameData)"
project: "SOLIDWORKS API Help"
interface: "IPMIFrameData"
member: "GeometricCharacteristic"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIFrameData~GeometricCharacteristic.html"
---

# GeometricCharacteristic Property (IPMIFrameData)

Gets the geometric characteristic of this Gtol frame.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property GeometricCharacteristic As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIFrameData
Dim value As System.Integer

instance.GeometricCharacteristic = value

value = instance.GeometricCharacteristic
```

### C#

```csharp
System.int GeometricCharacteristic {get; set;}
```

### C++/CLI

```cpp
property System.int GeometricCharacteristic {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Geometric characteristic as defined in [swGeometricCharacteristic_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swGeometricCharacteristic_e.html)

## VBA Syntax

See [PMIFrameData::GeometricCharacteristic](ms-its:sldworksapivb6.chm::/sldworks~PMIFrameData~GeometricCharacteristic.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## See Also

[IPMIFrameData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIFrameData.html)
[IPMIFrameData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIFrameData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
