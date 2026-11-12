---
title: "SuitCaseType Property (ISMCornerReliefData)"
project: "SOLIDWORKS API Help"
interface: "ISMCornerReliefData"
member: "SuitCaseType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData~SuitCaseType.html"
---

# SuitCaseType Property (ISMCornerReliefData)

Gets and sets the suitcase type of this corner relief slot.

## Syntax

### Visual Basic (Declaration)

```vb
Property SuitCaseType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISMCornerReliefData
Dim value As System.Integer

instance.SuitCaseType = value

value = instance.SuitCaseType
```

### C#

```csharp
System.int SuitCaseType {get; set;}
```

### C++/CLI

```cpp
property System.int SuitCaseType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Corner relief suitcase type as defined by [swCornerReliefSuitCaseType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerReliefSuitCaseType_e.html)

## VBA Syntax

See [SMCornerReliefData::SuitCaseType](ms-its:sldworksapivb6.chm::/sldworks~SMCornerReliefData~SuitCaseType.html).

## See Also

[ISMCornerReliefData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData.html)
[ISMCornerReliefData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
