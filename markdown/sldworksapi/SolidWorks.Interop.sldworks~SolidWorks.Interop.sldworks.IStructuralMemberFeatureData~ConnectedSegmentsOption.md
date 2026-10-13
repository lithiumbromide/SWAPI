---
title: "ConnectedSegmentsOption Property (IStructuralMemberFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IStructuralMemberFeatureData"
member: "ConnectedSegmentsOption"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~ConnectedSegmentsOption.html"
---

# ConnectedSegmentsOption Property (IStructuralMemberFeatureData)

Gets or sets the connected segments option.

## Syntax

### Visual Basic (Declaration)

```vb
Property ConnectedSegmentsOption As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IStructuralMemberFeatureData
Dim value As System.Integer

instance.ConnectedSegmentsOption = value

value = instance.ConnectedSegmentsOption
```

### C#

```csharp
System.int ConnectedSegmentsOption {get; set;}
```

### C++/CLI

```cpp
property System.int ConnectedSegmentsOption {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Connected segments option as defined in [swConnectedSegmentsOption_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swConnectedSegmentsOption_e.html)

## VBA Syntax

See [StructuralMemberFeatureData::ConnectedSegmentsOption](ms-its:sldworksapivb6.chm::/sldworks~StructuralMemberFeatureData~ConnectedSegmentsOption.html).

## See Also

[IStructuralMemberFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData.html)
[IStructuralMemberFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
