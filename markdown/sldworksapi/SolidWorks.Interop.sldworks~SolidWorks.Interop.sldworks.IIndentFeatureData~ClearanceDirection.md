---
title: "ClearanceDirection Property (IIndentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IIndentFeatureData"
member: "ClearanceDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~ClearanceDirection.html"
---

# ClearanceDirection Property (IIndentFeatureData)

Gets or sets the direction of the [clearance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~Clearance.html) for this indent feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ClearanceDirection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IIndentFeatureData
Dim value As System.Boolean

instance.ClearanceDirection = value

value = instance.ClearanceDirection
```

### C#

```csharp
System.bool ClearanceDirection {get; set;}
```

### C++/CLI

```cpp
property System.bool ClearanceDirection {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to reverse the direction of clearance, false to not

## VBA Syntax

See [IndentFeatureData::ClearanceDirection](ms-its:sldworksapivb6.chm::/sldworks~IndentFeatureData~ClearanceDirection.html).

## See Also

[IIndentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData.html)
[IIndentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
